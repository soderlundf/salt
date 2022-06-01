"""
Redis SaltStack engine.
An engine that increments seen events based on function name.
Perhaps useful for usage purposes?

:configuration:

    Example configuration

    .. code-block:: yaml

        engines:
          - redis:
              host: localhost
              port: 6379
              db: 0

:depends: https://pypi.org/project/redis/
"""

import logging
import salt.utils.event
import redis

log = logging.getLogger(__name__)

def start(host="localhost", port=6379, db=0):
    """
    Start method is required.

    host
        Redis host to connect to.

    port
        Port exposed by Redis to connect to.

    db
        Redis database to use.
    """

    if __opts__.get("id").endswith("_master"):
        instance = "master"
    else:
        instance = "minion"
    with salt.utils.event.get_event(
        instance,
        sock_dir=__opts__["sock_dir"],
        transport=__opts__["transport"],
        opts=__opts__,
    ) as event_bus:
        while True:
            event = event_bus.get_event(full=True)
            if event is not None:
                if "data" in event:
                    if "fun" in event["data"]:
                        r = redis.Redis(host=host, port=port, db=db)
                        ret = r.incr(event["data"]["fun"])
