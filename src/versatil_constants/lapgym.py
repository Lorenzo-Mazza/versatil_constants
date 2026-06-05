"""Constants for LapGym datasets."""

from enum import Enum


class LapGymCamera(str, Enum):
    """Camera identifiers for LapGym demonstrations."""

    STEREO_LEFT = "stereo_left"
    STEREO_RIGHT = "stereo_right"
    WRIST = "wrist"
    DEPTH = "depth"
