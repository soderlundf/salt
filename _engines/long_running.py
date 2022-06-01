"""
Long running SaltStack engine.

:configuration:

    Example configuration
    This will log a new message every 3 seconds.

    .. code-block:: yaml

        engines:
          - long_running:
              log_interval: 3

    Example configuration
    This will log a new message every 10 seconds.

    .. code-block:: yaml

        engines:
          - long_running

:depends: nothing
"""

import logging
import time

log = logging.getLogger(__name__)

def start(log_interval=10):
    """
    Start method is required.

    This will be started by the salt-master and continue to run until it is killed.
    You can check this by running ps -ef and it can be killed like any other process.
    If killed, the salt-master will restart it.

    log_interval

        Interval in seconds between each log message.
    """

    while True:
        time.sleep(log_interval)
        log.debug(f"Slept for {log_interval} seconds.")
