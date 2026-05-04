"""Wire protocol observation keys for the BlockPush simulation world."""

from enum import Enum


class BlockPushProprioKey(str, Enum):
    """Proprioceptive observation and action keys for BlockPush."""

    EE_POS = "ee_pos"
    EE_POS_ACTION = "ee_pos_action"
    BLOCK1_POS = "block_push_block1_pos"
    BLOCK1_ANGLE = "block_push_block1_angle"
    BLOCK2_POS = "block_push_block2_pos"
    BLOCK2_ANGLE = "block_push_block2_angle"
    EE_COMMANDED = "block_push_ee_commanded"
    TARGET1_POS = "block_push_target1_pos"
    TARGET1_ANGLE = "block_push_target1_angle"
    TARGET2_POS = "block_push_target2_pos"
    TARGET2_ANGLE = "block_push_target2_angle"
