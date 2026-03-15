"""Wire protocol observation keys for the Libero simulation world."""

from enum import Enum


class LiberoCamera(str, Enum):
    """Camera observation keys for Libero environments."""

    AGENTVIEW = "agentview_rgb"
    EYE_IN_HAND = "eye_in_hand_rgb"


class LiberoProprioKey(str, Enum):
    """Proprioceptive observation and action keys for Libero environments."""

    EE_POS = "ee_pos"
    EE_ORI = "ee_ori"
    EE_STATES = "ee_states"
    JOINT_STATES = "joint_states"
    EE_POS_ACTION = "ee_pos_action"
    EE_ORI_ACTION = "ee_ori_action"
    GRIPPER_STATE = "gripper_state_obs"
    GRIPPER_STATE_ACTION = "gripper_state_action"
