"""Wire protocol observation keys for the Franka Kitchen simulation world."""

from enum import Enum


class KitchenCamera(str, Enum):
    """Camera observation keys for Franka Kitchen environments."""

    AGENTVIEW = "agentview_rgb"


class KitchenProprioKey(str, Enum):
    """Proprioceptive observation and action keys for Franka Kitchen."""

    ARM_QPOS = "kitchen_arm_qpos"
    OBJECT_QPOS = "kitchen_object_qpos"
    TASK_GOAL = "kitchen_task_goal"
    ARM_ACTION = "kitchen_arm_action"
