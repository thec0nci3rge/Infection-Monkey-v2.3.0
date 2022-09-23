import logging
import socket
from contextlib import suppress
from dataclasses import dataclass
from typing import Dict, Iterable, Iterator, List, Optional, Tuple

from common.common_consts.timeouts import LONG_REQUEST_TIMEOUT
from common.types import SocketAddress
from infection_monkey.island_api_client import (
    AbstractIslandAPIClientFactory,
    IIslandAPIClient,
    IslandAPIConnectionError,
    IslandAPIError,
    IslandAPITimeoutError,
)
from infection_monkey.network.relay import RELAY_CONTROL_MESSAGE_REMOVE_FROM_WAITLIST
from infection_monkey.utils.threading import (
    ThreadSafeIterator,
    create_daemon_thread,
    run_worker_threads,
)

logger = logging.getLogger(__name__)

# The number of Island servers to test simultaneously. 32 threads seems large enough for all
# practical purposes. Revisit this if it's not.
NUM_FIND_SERVER_WORKERS = 32


@dataclass
class IslandAPISearchResult:
    server: SocketAddress
    client: Optional[IIslandAPIClient]


IslandAPISearchResults = List[IslandAPISearchResult]


def find_available_island_apis(
    servers: Iterable[SocketAddress], island_api_client_factory: AbstractIslandAPIClientFactory
) -> IslandAPISearchResults:
    server_list = list(servers)
    server_iterator = ThreadSafeIterator(enumerate(server_list.__iter__()))
    results: Dict[int, IslandAPISearchResult] = {}

    run_worker_threads(
        _find_island_server,
        "FindIslandServer",
        args=(server_iterator, results, island_api_client_factory),
        num_workers=NUM_FIND_SERVER_WORKERS,
    )

    return [results[i] for i in sorted(results.keys())]


def _find_island_server(
    servers: Iterator[Tuple[int, SocketAddress]],
    server_results: Dict[int, IslandAPISearchResult],
    island_api_client_factory: AbstractIslandAPIClientFactory,
):
    with suppress(StopIteration):
        index, server = next(servers)
        server_results[index] = IslandAPISearchResult(
            server, _check_if_island_server(server, island_api_client_factory)
        )


def _check_if_island_server(
    server: SocketAddress, island_api_client_factory: AbstractIslandAPIClientFactory
) -> Optional[IIslandAPIClient]:
    logger.debug(f"Trying to connect to server: {server}")

    try:
        client = island_api_client_factory.create_island_api_client()
        client.connect(server)

        return client
    except IslandAPIConnectionError as err:
        logger.error(f"Unable to connect to server/relay {server}: {err}")
    except IslandAPITimeoutError as err:
        logger.error(f"Timed out while connecting to server/relay {server}: {err}")
    except IslandAPIError as err:
        logger.error(
            f"Exception encountered when trying to connect to server/relay {server}: {err}"
        )

    return None


def send_remove_from_waitlist_control_message_to_relays(servers: Iterable[str]):
    for i, server in enumerate(servers, start=1):
        server_address = SocketAddress.from_string(server)
        t = create_daemon_thread(
            target=notify_disconnect,
            name=f"SendRemoveFromWaitlistControlMessageToRelaysThread-{i:02d}",
            args=(server_address,),
        )
        t.start()


def notify_disconnect(server_address: SocketAddress):
    """
    Tell upstream relay that we no longer need the relay

    :param server_address: The address of the server to notify
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as d_socket:
        d_socket.settimeout(LONG_REQUEST_TIMEOUT)

        try:
            d_socket.connect((str(server_address.ip), server_address.port))
            d_socket.sendall(RELAY_CONTROL_MESSAGE_REMOVE_FROM_WAITLIST)
            logger.info(f"Control message was sent to the server/relay {server_address}")
        except OSError as err:
            logger.error(f"Error connecting to socket {server_address}: {err}")
