import pygame
import math
from classes.shapes import Rectangle, Circle

BUTTON_WIDTH = 40
BUTTON_HEIGHT = 40
MARGIN = 10
DEFAULT_BUTTON_COLOR = "gray"
BASE_ICON_FOLDER = "./icons"


class Button(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.rect = pygame.rect.Rect(50, 50, BUTTON_WIDTH, BUTTON_HEIGHT)
        self.image = pygame.transform.scale(
            pygame.image.load(f"{BASE_ICON_FOLDER}/error.png").convert(),
            (BUTTON_WIDTH, BUTTON_HEIGHT),
        )
        self.color = DEFAULT_BUTTON_COLOR

    def call_position(self, index):
        return MARGIN * index + (index - 1) * BUTTON_HEIGHT

    def press(self):
        raise NotImplementedError

    def draw(self):
        raise NotImplementedError

    def mark_as_pressed(self, help_message):
        print(help_message)
        self.color = "coral"

    def reset(self):
        self.color = DEFAULT_BUTTON_COLOR
        self.is_pressed = False


class HelpButton(Button):
    def __init__(self, index):
        super().__init__()
        self.rect = pygame.rect.Rect(
            MARGIN, self.call_position(index), BUTTON_WIDTH, BUTTON_HEIGHT
        )
        self.image = pygame.transform.scale(
            pygame.image.load(f"{BASE_ICON_FOLDER}/question.png").convert_alpha(),
            (BUTTON_WIDTH, BUTTON_HEIGHT),
        )

    def press(self):
        print("\nClick the shapes to draw\nESCAPE: aborts the current command")


class RectButton(Button):
    def __init__(self, index):
        super().__init__()
        self.rect = pygame.rect.Rect(
            MARGIN, self.call_position(index), BUTTON_WIDTH, BUTTON_HEIGHT
        )
        self.image = pygame.transform.scale(
            pygame.image.load(f"{BASE_ICON_FOLDER}/rectangle.png").convert_alpha(),
            (BUTTON_WIDTH, BUTTON_HEIGHT),
        )

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


class CircleButton(Button):
    def __init__(self, index):
        super().__init__()
        self.rect = pygame.rect.Rect(
            MARGIN,
            self.call_position(index),
            BUTTON_WIDTH,
            BUTTON_HEIGHT,
        )
        self.image = pygame.transform.scale(
            pygame.image.load(f"{BASE_ICON_FOLDER}/oval.png").convert_alpha(),
            (BUTTON_WIDTH, BUTTON_HEIGHT),
        )

    def press(self, mouse_positions):
        x1 = mouse_positions[0][0]
        y1 = mouse_positions[0][1]

        x2 = mouse_positions[1][0]
        y2 = mouse_positions[1][1]

        radius = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

        shape = Circle()
        shape.shape = ((x1, y1), radius)
        return shape


class ClearAllButton(Button):
    def __init__(self, index):
        super().__init__()
        self.rect = pygame.rect.Rect(
            MARGIN,
            self.call_position(index),
            BUTTON_WIDTH,
            BUTTON_HEIGHT,
        )
        self.image = pygame.transform.scale(
            pygame.image.load(f"{BASE_ICON_FOLDER}/dust.png").convert_alpha(),
            (BUTTON_WIDTH, BUTTON_HEIGHT),
        )
