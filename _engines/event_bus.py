"""
Event bus SaltStack engine.
An engine that listens for events on the event bus
and logs them to the salt-master logfile.

:configuration:

    Example configuration

    .. code-block:: yaml

        engines:
          - event_bus

:depends: nothing
"""

import logging
import salt.utils.event

log = logging.getLogger(__name__)

def start():
    """
    Start method is required.
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
            # log the event to salt-master logfile
            # don't use in production... :P
            log.debug(f"Observed event: {event}")
        
