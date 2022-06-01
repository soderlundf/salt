"""
Bully SaltStack engine.

:configuration:

    Example configuration

    .. code-block:: yaml

        engines:
          - bully

:depends: nothing
"""

import logging

log = logging.getLogger(__name__)

def start():
    """Start method is required."""

    # let's bully the salt-master log file with debug logging the entire __opts__ dunder.
    # don't use this in production... :P
    log.debug(__opts__)
