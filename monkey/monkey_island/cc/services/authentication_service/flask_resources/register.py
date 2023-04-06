import logging
import time
from http import HTTPStatus

from flask import Response, make_response, request
from flask.typing import ResponseValue
from flask_security.views import register

from monkey_island.cc.flask_utils import AbstractResource, responses

from ..authentication_facade import AuthenticationFacade
from .utils import (
    add_expiration_time_to_response,
    get_username_password_from_request,
    include_auth_token,
)

logger = logging.getLogger(__name__)


class Register(AbstractResource):
    """
    A resource for user registration
    """

    urls = ["/api/register"]

    def __init__(self, authentication_facade: AuthenticationFacade):
        self._authentication_facade = authentication_facade

    # Can't be secured, used for registration
    @include_auth_token
    def post(self):
        """
        Registers a new user using flask security register

        """
        if not self._authentication_facade.needs_registration():
            return {
                "errors": ["A user already exists. Only a single user can be registered."]
            }, HTTPStatus.CONFLICT

        try:
            username, password = get_username_password_from_request(request)
        except Exception:
            return responses.make_response_to_invalid_request()

        registration_time = int(time.time())
        response: ResponseValue = register()

        # Register view treat the request as form submit which may return something
        # that it is not a response
        if not isinstance(response, Response):
            return responses.make_response_to_invalid_request()

        if response.status_code == HTTPStatus.OK:
            self._authentication_facade.handle_successful_registration(username, password)
            token_expiration_time = self._authentication_facade.calculate_token_expiration_time(
                registration_time
            )
            response = add_expiration_time_to_response(response, token_expiration_time)

        return make_response(response)
