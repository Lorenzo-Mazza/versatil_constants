"""Wire protocol observation keys for the Multimodal Ant world."""

from enum import Enum


class MultimodalAntProprioKey(str, Enum):
    """Proprioceptive observation and action keys for Multimodal Ant."""

    QPOS = "ant_qpos"
    QVEL = "ant_qvel"
    GOAL_COORDS = "ant_goal_coords"
    ACHIEVED = "ant_achieved"
    TORQUE_ACTION = "ant_torque_action"
