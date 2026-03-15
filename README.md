# versatil_constants

Shared domain constants for the VersatIL imitation learning ecosystem. Zero dependencies.

Each "world" (TSO robot testbed, Libero simulation, MetaWorld simulation) has its own module defining observation keys, action keys, and environment-specific constants. Shared constants (language keys, gripper types, coordinate systems) live in `shared`.

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
from versatil_constants.libero import LiberoCamera, LiberoProprioKey, LiberoGymKey

# MetaWorld simulation
from versatil_constants.metaworld import MetaWorldCamera, MetaWorldGymKey
```

## Modules

| Module | Contents |
|--------|----------|
| `shared` | `ObsKey`, `GripperType`, `BinaryGripperRange`, `ActionComputationMethod`, `CoordinateSystem`, `OrientationRepresentation` |
| `tso` | `TSOCamera`, `TSOProprioKey` |
| `libero` | `LiberoCamera`, `LiberoProprioKey`, `LiberoGymKey`, `LiberoTrajectoryColumn`, `TaskSuiteName` |
| `metaworld` | `MetaWorldCamera`, `MetaWorldProprioKey`, `MetaWorldGymKey`, `MetaWorldTrajectoryColumn`, `BenchmarkName` |
