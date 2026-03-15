"""Wire protocol observation keys for the MetaWorld simulation world."""

from enum import Enum


class MetaWorldCamera(str, Enum):
    """Camera observation keys for MetaWorld environments."""

    AGENTVIEW = "agentview_rgb"


class MetaWorldProprioKey(str, Enum):
    """Proprioceptive action keys for MetaWorld environments."""

    EE_POS_ACTION = "ee_pos_action"
    GRIPPER_STATE_ACTION = "gripper_state_action"
