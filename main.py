#!/usr/bin/env python3
from dataclasses import dataclass, asdict


import tcod


from actions import EscapeAction, MovementAction
from input_handlers import EventHandler
from entity import Entity
from engine import Engine


def main() -> None:
    screen_width = 80
    screen_height = 50

    player = Entity(screen_width // 2, screen_height // 2, "@", (255, 255, 255))
    npc = Entity(screen_width // 2 - 5, screen_height // 2, "@", (255, 255, 0))

    entities = [npc, player]

    event_handler = EventHandler()

    engine = Engine(entities=entities, event_handler=event_handler, player=player)

    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title="Yet Another Roguelike Tutorial",
        vsync=True,
    ) as context:
        root_console = tcod.Console(screen_width, screen_height, order="F")
        while True:
            engine.render(console=root_console, context=context)

            events = tcod.event.wait()

            engine.handle_events(events)


if __name__ == "__main__":
    main()
