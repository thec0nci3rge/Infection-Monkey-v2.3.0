import threading
from unittest.mock import MagicMock

import pytest
from flask import Response

from common.event_queue import IAgentEventQueue
from common.types import PingScanData, PluginType
from infection_monkey.i_puppet import UnknownPluginError
from infection_monkey.master.plugin_registry import PluginRegistry
from infection_monkey.puppet.puppet import EMPTY_FINGERPRINT, Puppet


def test_puppet_run_payload_success():
    p = Puppet(
        agent_event_queue=MagicMock(spec=IAgentEventQueue),
        plugin_registry=PluginRegistry(MagicMock()),
    )

    payload = MagicMock()
    payload_name = "PayloadOne"

    p.load_plugin(payload_name, payload, PluginType.PAYLOAD)
    p.run_payload(payload_name, {}, threading.Event())

    payload.run.assert_called_once()


def test_puppet_run_multiple_payloads():
    p = Puppet(
        agent_event_queue=MagicMock(spec=IAgentEventQueue),
        plugin_registry=PluginRegistry(MagicMock()),
    )

    payload_1 = MagicMock()
    payload1_name = "PayloadOne"

    payload_2 = MagicMock()
    payload2_name = "PayloadTwo"

    payload_3 = MagicMock()
    payload3_name = "PayloadThree"

    p.load_plugin(payload1_name, payload_1, PluginType.PAYLOAD)
    p.load_plugin(payload2_name, payload_2, PluginType.PAYLOAD)
    p.load_plugin(payload3_name, payload_3, PluginType.PAYLOAD)

    p.run_payload(payload1_name, {}, threading.Event())
    payload_1.run.assert_called_once()

    p.run_payload(payload2_name, {}, threading.Event())
    payload_2.run.assert_called_once()

    p.run_payload(payload3_name, {}, threading.Event())
    payload_3.run.assert_called_once()


def test_fingerprint_exception_handling(monkeypatch):
    p = Puppet(
        agent_event_queue=MagicMock(spec=IAgentEventQueue),
        plugin_registry=PluginRegistry(MagicMock()),
    )
    p._plugin_registry.get_plugin = MagicMock(side_effect=Exception)
    assert p.fingerprint("", "", PingScanData("windows", False), {}, {}) == EMPTY_FINGERPRINT


class StubIslandAPIClient:
    def get_plugin(self, _, __):
        return Response(status=404)


def test_load_plugin_not_found(monkeypatch):
    p = Puppet(
        agent_event_queue=MagicMock(spec=IAgentEventQueue),
        plugin_registry=PluginRegistry(StubIslandAPIClient()),
    )

    with pytest.raises(UnknownPluginError):
        p.run_credential_collector("Ghost", {})
