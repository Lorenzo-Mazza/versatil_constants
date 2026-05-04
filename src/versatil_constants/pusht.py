"""Wire protocol observation keys for the PushT simulation world."""

from enum import Enum


class PushTCamera(str, Enum):
    """Camera observation keys for PushT environments."""

    AGENTVIEW = "agentview_rgb"


class PushTProprioKey(str, Enum):
    """Proprioceptive observation and action keys for PushT environments."""

    AGENT_POS = "ee_pos"
    AGENT_POS_ACTION = "ee_pos_action"
    BLOCK_POS = "pusht_block_pos"
    BLOCK_ANGLE = "pusht_block_angle"
    KEYPOINTS = "pusht_keypoints"
    CONTACTS = "pusht_contacts"
