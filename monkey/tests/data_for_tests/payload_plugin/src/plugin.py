import logging
import time
from threading import Event, current_thread
from typing import Any, Dict

import mock_dependency

from common.agent_events import AgentEventTag, FileEncryptionEvent
from common.event_queue import IAgentEventPublisher
from common.types import AgentID
from infection_monkey.i_puppet import PayloadResult
from infection_monkey.utils.threading import interruptible_iter

logger = logging.getLogger(__name__)


class Plugin:
    def __init__(
        self,
        *,
        plugin_name="",
        agent_id: AgentID,
        agent_event_publisher: IAgentEventPublisher,
        **kwargs,
    ):
        self._agent_id = agent_id
        self._agent_event_publisher = agent_event_publisher

    def run(
        self,
        *,
        options: Dict[str, Any],
        interrupt: Event,
        **kwargs,
    ):
        logger.info(f"Main thread name {current_thread().name}")
        logger.info(f"Mock dependency package version: {mock_dependency.__version__}")

        Plugin._log_options(options)
        Plugin._sleep(options.get("sleep_duration", 0), interrupt)

        return self._run_payload(options)

    @staticmethod
    def _log_options(options: Dict[str, Any]):
        logger.info("Plugin options:")

        random_boolean = options.get("random_boolean", None)
        logger.info(f"Random boolean: {random_boolean}")

    @staticmethod
    def _sleep(duration: float, interrupt: Event):
        logger.info(f"Sleeping for {duration} seconds")
        for time_passed in interruptible_iter(range(int(duration)), interrupt):
            logger.info(f"Passed {time_passed} seconds")
            time.sleep(1)

    def _run_payload(self, options: Dict[str, Any]) -> PayloadResult:
        payload_result = PayloadResult(run_success=True)

        self._agent_event_publisher.publish(
            FileEncryptionEvent(
                source=self._agent_id,
                file_path="filepath",
                success=True,
                error_message="error",
                tags=frozenset({AgentEventTag("payload-tag")}),
            )
        )

        return payload_result
