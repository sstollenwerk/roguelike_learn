import numpy as np  # type: ignore

from basic_types import Color, graphic_dt, tile_dt


def new_tile(
    *,  # Enforce the use of keywords, so that parameter order doesn't matter.
    walkable: bool,
    transparent: bool,
    dark: tuple[int, Color, Color],
) -> np.ndarray:
    """Helper function for defining individual tile types"""
    return np.array((walkable, transparent, dark), dtype=tile_dt)


floor = new_tile(
    walkable=True,
    transparent=True,
    dark=(ord(" "), (255, 255, 255), (50, 50, 150)),
)
wall = new_tile(
    walkable=False,
    transparent=False,
    dark=(ord(" "), (255, 255, 255), (0, 0, 100)),
)
