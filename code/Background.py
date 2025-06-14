#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import WIN_WIDTH, ENTITY_SPEED
from code.Entity import Entity


class Background(Entity):
    """A class representing a background entity that moves horizontally across the screen."""
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        """Move the background entity to the left."""
        self.rect.centerx -= ENTITY_SPEED[self.name]
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH
