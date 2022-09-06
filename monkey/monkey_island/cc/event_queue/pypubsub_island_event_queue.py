import logging
from typing import Any

from pubsub.core import Publisher

from common.event_queue import PyPubSubPublisherWrapper

from . import IIslandEventQueue, IslandEventSubscriber, IslandEventTopic

logger = logging.getLogger(__name__)


class PyPubSubIslandEventQueue(IIslandEventQueue):
    def __init__(self, pypubsub_publisher: Publisher):
        self._pypubsub_publisher_wrapped = PyPubSubPublisherWrapper(pypubsub_publisher)

    def subscribe(self, topic: IslandEventTopic, subscriber: IslandEventSubscriber):
        topic_name = topic.name  # needs to be a string for pypubsub
        self._pypubsub_publisher_wrapped.subscribe(topic_name, subscriber)

    def publish(self, topic: IslandEventTopic, event: Any = None):
        topic_name = topic.name  # needs to be a string for pypubsub
        logger.debug(f"Publishing {topic_name} event")
        self._pypubsub_publisher_wrapped.publish(topic_name, event)
