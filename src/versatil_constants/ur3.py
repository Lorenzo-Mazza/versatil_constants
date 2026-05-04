"""Wire protocol observation keys for the UR3 block-pushing world."""

from enum import Enum


class UR3ProprioKey(str, Enum):
    """Proprioceptive observation and action keys for UR3 block-pushing."""

    EE_POS = "ur3_ee_pos"
    BLOCK1_POS = "ur3_block1_pos"
    BLOCK2_POS = "ur3_block2_pos"
    EE_TARGET_ACTION = "ur3_ee_target_action"
