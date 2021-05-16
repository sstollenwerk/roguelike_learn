from typing import Iterable, Any
from dataclasses import dataclass, asdict

from tcod.context import Context
from tcod.console import Console

from actions import EscapeAction, MovementAction
from entity import Entity
from input_handlers import EventHandler
from game_map import GameMap


class Engine:
    def __init__(
        self,
        entities: list[Entity],
        event_handler: EventHandler,
        game_map: GameMap,
        player: Entity,
    ):
        if player not in entities:
            entities += [player]
        self.entities = entities
        self.event_handler = event_handler
        self.player = player
        self.game_map = game_map

    def handle_events(self, events: Iterable[Any]) -> None:
        for event in events:
            action = self.event_handler.dispatch(event)

            if action is None:
                continue

            action.perform(self, self.player)

    def render(self, console: Console, context: Context) -> None:
        self.game_map.render(console)

        for entity in self.entities:
            console.print(**asdict(entity))

        context.present(console)

        console.clear()
