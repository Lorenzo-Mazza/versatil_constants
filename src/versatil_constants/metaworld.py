"""Constants for the MetaWorld simulation world."""

from enum import Enum


class MetaWorldCamera(str, Enum):
    """Camera identifiers for MetaWorld environments."""

    AGENTVIEW = "agentview_rgb"
    IMAGE_LEROBOT = "observation.image"


class MetaWorldProprioKey(str, Enum):
    """Proprioceptive action keys for MetaWorld environments."""

    EE_POS_ACTION = "ee_pos_action"
    GRIPPER_STATE_ACTION = "gripper_state_action"


class MetaWorldGymKey(str, Enum):
    """Gym environment observation and info keys for MetaWorld."""

    AGENT_VIEW = "agent_view"
    AGENT_POS = "agent_pos"
    AGENT_GRIPPER = "agent_gripper"
    RAW_OBS = "raw_obs"
    FINAL_INFO = "final_info"
    FINAL_OBSERVATION = "final_observation"
    SUCCESS = "success"


class MetaWorldTrajectoryColumn(str, Enum):
    """Column names for MetaWorld trajectory data."""

    EE_POS_X = "ee_pos_x"
    EE_POS_Y = "ee_pos_y"
    EE_POS_Z = "ee_pos_z"
    GRIPPER = "gripper"


class BenchmarkName(str, Enum):
    """MetaWorld benchmark difficulty levels."""

    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"
    VERY_HARD = "very_hard"
    MT50 = "mt50"
