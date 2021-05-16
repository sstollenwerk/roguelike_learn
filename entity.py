from dataclasses import dataclass, asdict, replace

from actions import EscapeAction, MovementAction
from basic_types import Color


@dataclass
class Entity:
    x: int
    y: int
    string: str  # len == 1
    fg: Color

    def move(self, action: MovementAction):
        ##return replace(self, x=self.x + action.dx, y=self.y + action.dy)
        self.x += action.dx
        self.y += action.dy
