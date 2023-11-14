import pygame
import pickle

from classes.buttons import RectButton, HelpButton, ClearAllButton, CircleButton

FILE_TO_SAVE = "data.pickle"


class Canvas:
    def __init__(self):
        pygame.init()
        self.__screen = pygame.display.set_mode((500, 500))
        pygame.display.set_caption("PyCAD")
        self.__buttons_init()
        self.pressed_button = None
        self.mouse_positions = []
        self.__shapes = []

    def __buttons_init(self):
        self.__button_help = HelpButton(index=1)
        self.__button_rect = RectButton(index=2)
        self.__button_circle = CircleButton(index=3)
        self.button_clear_all = ClearAllButton(index=4)
        self.__buttons = [
            self.button_clear_all,
            self.__button_help,
            self.__button_rect,
            self.__button_circle,
        ]

        for button in self.__buttons:
            group = pygame.sprite.GroupSingle()
            group.add(button)

        self.__button_help.press()

    def clear_all(self):
        print("Deleted all shapes")
        self.__shapes = []

    def check_button_pressed(self, mouse_pos):
        if self.__button_rect.rect.collidepoint(mouse_pos):
            self.__button_rect.mark_as_pressed("Rectangle requires two points")
            self.pressed_button = self.__button_rect

        if self.__button_circle.rect.collidepoint(mouse_pos):
            self.__button_circle.mark_as_pressed("Circle requires two points")
            self.pressed_button = self.__button_circle

        if self.__button_help.rect.collidepoint(mouse_pos):
            self.__button_help.press()
            self.reset_all()

        if self.button_clear_all.rect.collidepoint(mouse_pos):
            self.clear_all()

    def update(self):
        if (
            isinstance(self.pressed_button, RectButton)
            and len(self.mouse_positions) == 2
        ):
            shape = self.__button_rect.press(self.mouse_positions)
            self.__shapes.append(shape)
            self.mouse_reset()
        if (
            isinstance(self.pressed_button, CircleButton)
            and len(self.mouse_positions) == 2
        ):
            shape = self.__button_circle.press(self.mouse_positions)
            self.__shapes.append(shape)
            self.mouse_reset()

    def draw(self):
        self.__screen.fill("black")

        for shape in self.__shapes:
            shape.draw(self.__screen)

        for mouse_position in self.mouse_positions:
            pygame.draw.line(self.__screen, "white", mouse_position, mouse_position)

        for button in self.__buttons:
            pygame.draw.rect(self.__screen, button.color, button, border_radius=5)

            self.__screen.blit(
                button.image,
                (button.rect.x, button.rect.y),
            )

        pygame.display.flip()

    def mouse_reset(self):
        self.mouse_positions = []

    def action_reset(self):
        self.pressed_button = None

    def reset_all(self):
        if self.pressed_button:
            self.pressed_button.reset()
        self.mouse_reset()
        self.action_reset()
        self.pressed_button = None

    def dump_to_file(self):
        with open(FILE_TO_SAVE, "wb") as f:
            pickle.dump(self.__shapes, f, pickle.HIGHEST_PROTOCOL)

    def load_file(self):
        content = []
        try:
            with open(FILE_TO_SAVE, "rb") as f:
                content = pickle.load(f)
        except (FileNotFoundError, EOFError):
            pass
        self.__shapes = content
