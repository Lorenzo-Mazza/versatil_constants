"""Constants for the Libero simulation world."""

from enum import Enum


class LiberoCamera(str, Enum):
    """Camera identifiers for Libero environments."""

    AGENTVIEW = "agentview_rgb"
    EYE_IN_HAND = "eye_in_hand_rgb"
    IMAGE = "observation.images.image"
    IMAGE_2 = "observation.images.image2"
    FRONT = "observation.images.front"
    WRIST = "observation.images.wrist"


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


class LiberoGymKey(str, Enum):
    """Gym environment observation keys for Libero."""

    AGENTVIEW_IMAGE = "agentview_image"
    EYE_IN_HAND_IMAGE = "robot0_eye_in_hand_image"
    EE_POS = "robot0_eef_pos"
    EE_QUAT = "robot0_eef_quat"
    GRIPPER_QPOS = "robot0_gripper_qpos"
    JOINT_POS = "robot0_joint_pos"


class LiberoTrajectoryColumn(str, Enum):
    """Column names for Libero trajectory data."""

    EE_POS_X = "ee_pos_x"
    EE_POS_Y = "ee_pos_y"
    EE_POS_Z = "ee_pos_z"
    EE_QUAT_X = "ee_quat_x"
    EE_QUAT_Y = "ee_quat_y"
    EE_QUAT_Z = "ee_quat_z"
    EE_QUAT_W = "ee_quat_w"
    GRIPPER_QPOS_0 = "gripper_qpos_0"
    GRIPPER_QPOS_1 = "gripper_qpos_1"


class TaskSuiteName(str, Enum):
    """Libero task suite identifiers."""

    LIBERO_SPATIAL = "libero_plus_spatial"
    LIBERO_OBJECT = "libero_plus_object"
    LIBERO_GOAL = "libero_plus_goal"
    LIBERO_10 = "libero_plus_10"
    LIBERO_90 = "libero_90"
    LIBERO_ALL = "libero_plus_all"
