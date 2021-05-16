from dataclasses import dataclass


@dataclass
class Action:
    pass


@dataclass
class EscapeAction(Action):
    pass


@dataclass
class MovementAction(Action):
    dx: int
    dy: int
