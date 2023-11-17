import pygame
import math
from classes.shapes import Rectangle, Circle, Line
from classes.buttons import ButtonShapes

from constants import (
    BUTTON_WIDTH,
    BUTTON_HEIGHT,
    MARGIN,
)


class RectButton(ButtonShapes):
    def __init__(self, index):
        super().__init__()
        self.rect = pygame.rect.Rect(
            MARGIN, self.define_position(index), BUTTON_WIDTH, BUTTON_HEIGHT
        )
        self.image = self.load_image("rectangle.png")
        self.help_message = "Rectangle requires two points"

    def press(self, mouse_positions):
        x1 = mouse_positions[0][0]
        y1 = mouse_positions[0][1]

        x2 = mouse_positions[1][0]
        y2 = mouse_positions[1][1]

        width = abs(x1 - x2)
        height = abs(y1 - y2)

        rect = Rectangle()
        rect.shape = pygame.rect.Rect(*mouse_positions[0], width, height)
        if x1 <= x2:
            if y1 <= y2:
                rect.shape.bottomright = (x2, y2)
            else:
                rect.shape.topright = (x2, y2)
        else:
            if y1 <= y2:
                rect.shape.bottomleft = (x2, y2)
            else:
                rect.shape.topleft = (x2, y2)
        return rect


class CircleButton(ButtonShapes):
    def __init__(self, index):
        super().__init__()
        self.rect = pygame.rect.Rect(
            MARGIN,
            self.define_position(index),
            BUTTON_WIDTH,
            BUTTON_HEIGHT,
        )
        self.image = self.load_image("oval.png")
        self.help_message = "Circle requires two points"

    def press(self, mouse_positions):
        x1 = mouse_positions[0][0]
        y1 = mouse_positions[0][1]

        x2 = mouse_positions[1][0]
        y2 = mouse_positions[1][1]

        radius = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

        shape = Circle()
        shape.shape = ((x1, y1), radius)
        return shape


class LineButton(ButtonShapes):
    def __init__(self, index):
        super().__init__()
        self.rect = pygame.rect.Rect(
            MARGIN,
            self.define_position(index),
            BUTTON_WIDTH,
            BUTTON_HEIGHT,
        )
        self.image = self.load_image("diagonal-line.png")
        self.help_message = "Line requires two points"

    def press(self, mouse_positions):
        x1 = mouse_positions[0][0]
        y1 = mouse_positions[0][1]

        x2 = mouse_positions[1][0]
        y2 = mouse_positions[1][1]

        shape = Line()
        shape.shape = ((x1, y1), (x2, y2))
        return shape
