import pygame
from constants import (
    BUTTON_WIDTH,
    BUTTON_HEIGHT,
    BASE_ICON_FOLDER,
    MARGIN,
    DEFAULT_BUTTON_COLOR,
)


class Button(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.rect = pygame.rect.Rect(50, 50, BUTTON_WIDTH, BUTTON_HEIGHT)
        self.image = self.load_image()
        self.color = DEFAULT_BUTTON_COLOR

        self.help_message = ""

    def load_image(self, image="error.png"):
        return pygame.transform.scale(
            pygame.image.load(f"{BASE_ICON_FOLDER}/{image}").convert_alpha(),
            (BUTTON_WIDTH, BUTTON_HEIGHT),
        )

    def define_position(self, index):
        return MARGIN * index + (index - 1) * BUTTON_HEIGHT

    def press(self):
        raise NotImplementedError

    def mark_as_pressed(self):
        if self.help_message:
            print(self.help_message)
        self.color = "coral"

    def reset(self):
        self.color = DEFAULT_BUTTON_COLOR


class ButtonShapes(Button):
    def __init__(self):
        super().__init__()


class ButtonAction(Button):
    def __init__(self):
        super().__init__()
