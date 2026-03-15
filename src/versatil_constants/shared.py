"""Constants shared across all worlds in the VersatIL ecosystem."""

from enum import Enum


class ObsKey(str, Enum):
    """Observation keys common to all environments."""

    LANGUAGE = "language_instruction"
    PHASE_LABEL = "phase_label"


class GripperType(str, Enum):
    """Gripper actuation type."""

    BINARY = "binary"
    CONTINUOUS = "continuous"


class BinaryGripperRange(str, Enum):
    """Value range for binary gripper commands."""

    ZERO_ONE = "zero_one"
    MINUS_ONE_ONE = "minus_one_one"


class ActionComputationMethod(str, Enum):
    """Method for computing actions from observations."""

    NEXT_TIMESTEP = "next_timestep"
    DELTA = "delta"


class CoordinateSystem(str, Enum):
    """Reference frame for spatial coordinates."""

    ROBOT_BASE = "robot_base"
    ROBOT_EE = "robot_ee"
    CAMERA = "camera"
    UNKNOWN = "unknown"


class OrientationRepresentation(str, Enum):
    """Rotation representation format."""

    ROLL = "roll"
    EULER = "euler"
    QUATERNION = "quaternion"
