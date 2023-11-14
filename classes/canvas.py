import pygame
import pickle

from classes.buttons import HelpButton, ClearAllButton
from classes.buttons_shape import RectButton, CircleButton, LineButton

FILE_TO_SAVE = "data.pickle"


class Initializer:
    def init_buttons(self):
        button_help = HelpButton(index=1)
        button_rect = RectButton(index=2)
        button_circle = CircleButton(index=3)
        button_line = LineButton(index=4)
        button_clear_all = ClearAllButton(index=5)
        buttons = [
            button_clear_all,
            button_help,
            button_rect,
            button_circle,
            button_line,
        ]

        for button in buttons:
            group = pygame.sprite.GroupSingle()
            group.add(button)

        button_help.press()
        return buttons


class ShapeFactory:
    def make(self, shapes: [], pressed_button, mouse_positions):
        shapes_: [] = shapes.copy()
        if isinstance(pressed_button, RectButton) and len(mouse_positions) == 2:
            shape = pressed_button.press(mouse_positions)
            shapes_.append(shape)

        if isinstance(pressed_button, CircleButton) and len(mouse_positions) == 2:
            shape = pressed_button.press(mouse_positions)
            shapes_.append(shape)

        if isinstance(pressed_button, LineButton) and len(mouse_positions) == 2:
            shape = pressed_button.press(mouse_positions)
            shapes_.append(shape)

        if isinstance(pressed_button, HelpButton):
            pressed_button.press()

        if isinstance(pressed_button, ClearAllButton):
            pass

        if len(shapes_) > len(shapes):
            return shapes_


class Canvas:
    def __init__(self):
        pygame.init()
        self.__screen = pygame.display.set_mode((500, 500))
        pygame.display.set_caption("PyCAD")
        self.__buttons = Initializer().init_buttons()
        self.__shape_factory = ShapeFactory()
        self.pressed_button = None
        self.mouse_positions = []
        self.__shapes = []

    def clear_all(self):
        self.__shapes = []

    def check_button_pressed(self, mouse_pos):
        for button in self.__buttons:
            if button.rect.collidepoint(mouse_pos):
                self.pressed_button = button
                self.pressed_button.mark_as_pressed()
                break

    def update(self):
        shapes = self.__shape_factory.make(
            self.__shapes, self.pressed_button, self.mouse_positions
        )
        if shapes:
            self.__shapes = shapes
            self.reset_all()

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
