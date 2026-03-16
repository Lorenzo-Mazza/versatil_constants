# versatil_constants

[![Tests](https://github.com/Lorenzo-Mazza/versatil_constants/actions/workflows/test.yml/badge.svg)](https://github.com/Lorenzo-Mazza/versatil_constants/actions/workflows/test.yml)
[![PyPI](https://img.shields.io/pypi/v/versatil-constants)](https://pypi.org/project/versatil-constants/)
[![Python](https://img.shields.io/pypi/pyversions/versatil-constants)](https://pypi.org/project/versatil-constants/)

Shared domain constants for the VersatIL imitation learning ecosystem. Zero dependencies.

Each "world" (TSO robot testbed, Libero simulation, MetaWorld simulation, etc.) has its own module defining observation and action keys that cross the wire between inference clients and environment servers. Shared constants (language keys, gripper types, coordinate systems) live in `shared`.

## Installation

```bash
pip install versatil-constants
```

## Usage

```python
# Shared across all worlds
from versatil_constants.shared import ObsKey, GripperType, BinaryGripperRange

# TSO Robot Testbed
from versatil_constants.tso import TSOCamera, TSOProprioKey

# Libero simulation
from versatil_constants.libero import LiberoCamera, LiberoProprioKey

# MetaWorld simulation
from versatil_constants.metaworld import MetaWorldCamera, MetaWorldProprioKey
```

## Modules

| Module | Contents |
|--------|----------|
| `shared` | `ObsKey`, `GripperType`, `BinaryGripperRange`, `ActionComputationMethod`, `CoordinateSystem`, `OrientationRepresentation`, `ActionComponent`, `ActionMetadataField` |
| `tso` | `TSOCamera`, `TSOProprioKey` |
| `libero` | `LiberoCamera`, `LiberoProprioKey` |
| `metaworld` | `MetaWorldCamera`, `MetaWorldProprioKey` |
