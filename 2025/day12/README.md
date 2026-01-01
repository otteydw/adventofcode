# Notes on the Solution

My puzzle input (and I assume most puzzle inputs) contained regions that were large enough to hold gifts that were **full blocks** of size **3×3**, meaning there was no need to worry about internal “holes.”
Because of that, I provide a **simplified solver** that runs very quickly and avoids unnecessary complexity.

However, the **example input** included regions that did *not* support this shortcut. In that case, the gifts actually need to be *packed* correctly. To handle this, I used the third-party **[polyomino](https://github.com/jwg4/polyomino)** package:

## Files

- [`day12.py`](./day12.py) — Full solution that handles arbitrary shapes using proper polyomino packing.
- [`day12_simplified.py`](./day12_simplified.py) — Optimized version that assumes 3×3 full-block placement and skips hole handling.
