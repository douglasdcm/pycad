import pygame
from classes.buttons import ButtonAction
from constants import BUTTON_WIDTH, BUTTON_HEIGHT, MARGIN, DEFAULT_BUTTON_COLOR


class HelpButton(ButtonAction):
    def __init__(self, index):
        super().__init__()
        self.rect = pygame.rect.Rect(
            MARGIN, self.define_position(index), BUTTON_WIDTH, BUTTON_HEIGHT
        )
        self.image = self.load_image("question.png")

    def press(self):
        print("\nESCAPE: abort action\nClick the pictures to draw")


class CanvasCleanerButton(ButtonAction):
    def __init__(self, index):
        super().__init__()
        self.rect = pygame.rect.Rect(
            MARGIN,
            self.define_position(index),
            BUTTON_WIDTH,
            BUTTON_HEIGHT,
        )
        self.image = self.load_image("dust.png")
        self.help_message = "Deleted all shapes"

    def press(self):
        pass


class ShapeEraserButton(ButtonAction):
    def __init__(self, index):
        super().__init__()
        self.rect = pygame.rect.Rect(
            MARGIN,
            self.define_position(index),
            BUTTON_WIDTH,
            BUTTON_HEIGHT,
        )
        self.image = self.load_image("eraser.png")
        self.help_message = "Select shape to delete"

    def press(self):
        pass
