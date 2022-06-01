"""
SaltStack engine taking one argument.

:configuration:

    Example configuration

    .. code-block:: yaml

        engines:
          - one_arg:
            name: test

:depends: nothing
"""

def start(name=None):
    """
    Start method is required.

    The value from the engine config key 'name' will automatically be passed to this method.
    """
    pass
