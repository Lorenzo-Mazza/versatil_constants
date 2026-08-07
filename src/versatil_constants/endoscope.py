"""Constants for endoscope guidance tasks."""

from enum import Enum


class EndoscopeProprioKey(str, Enum):
    """Proprioceptive observation and action keys for endoscope guidance."""

    ROLL_ACTION = "endoscope_roll_action"
