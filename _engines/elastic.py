import logging
import salt.utils.event
import salt.utils.http
import salt.utils.json
from elasticsearch import Elasticsearch

log = logging.getLogger(__name__)

__virtualname__ = "elastic"

def _publish(event, api_key, api_id, url, index, verify_certs=True):
    es = Elasticsearch(url, verify_certs=verify_certs,
        api_key=(api_id, api_key))
    try:
        es.index(index=index, document=event)
    except (Exception) as ex:
        log.warning(f"Failed to publish event to elastic for index {index}. {ex}")


def _handle_event(event, api_key, api_id, url, verify_certs=True):
    if not "data" in event:
        return
    if not "fun" in event["data"]:
        return
    if not "return" in event["data"]:
        return
    index = f"salt_{event['data']['fun']}"
    return _publish(event, api_key, api_id, url, index, verify_certs)


def start(url=None, api_key=None, api_id=None, verify_certs=True):
    log.info(f"Engine {__virtualname__} started.")
    if api_key is None:
        log.warning("No api key specified in config. Nothing will be published to elastic.")
        return
    if url is None:
        log.warning("No url specified in config. Nothing will be published to elastic")
        return
    with salt.utils.event.get_event(
        "master",
        sock_dir=__opts__["sock_dir"],
        transport=__opts__["transport"],
        opts=__opts__,
    ) as event_bus:
        while True:
            event = event_bus.get_event(full=True)
            if not event is None and "data" in event:
                _handle_event(event, api_key, api_id, url, verify_certs)
