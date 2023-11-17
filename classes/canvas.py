import pygame
import pickle

from classes.buttons import ButtonAction, ButtonShapes
from classes.buttons_action import CanvasCleanerButton, HelpButton, ShapeEraserButton
from classes.buttons_shape import (
    RectButton,
    CircleButton,
    LineButton,
)
from constants import FILE_TO_SAVE, SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_CAPTION


class Initializer:
    def init_buttons(self):
        button_line = LineButton(index=1)
        button_rect = RectButton(index=2)
        button_circle = CircleButton(index=3)
        button_shape_remover = ShapeEraserButton(index=4)
        button_clear_all = CanvasCleanerButton(index=8)
        button_help = HelpButton(index=9)
        buttons = [
            button_clear_all,
            button_help,
            button_rect,
            button_circle,
            button_line,
            button_shape_remover,
        ]

        for button in buttons:
            group = pygame.sprite.GroupSingle()
            group.add(button)

        button_help.press()
        return buttons


class Canvas:
    def __init__(self):
        pygame.init()
        self.__screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(SCREEN_CAPTION)
        self.__buttons = Initializer().init_buttons()
        self.__canvas_handler = CanvasHandler()
        self.pressed_button = None
        self.mouse_positions = []
        self.shapes = []
        self.selected_shape = None

    def clear_all(self):
        self.shapes = []

    def check_button_pressed(self, mouse_pos):
        for button in self.__buttons:
            if button.rect.collidepoint(mouse_pos):
                self.pressed_button = button
                self.pressed_button.mark_as_pressed()
                break

    def update(self):
        if isinstance(self.pressed_button, ButtonShapes):
            self = self.__canvas_handler.make_shape(self)

        if isinstance(self.pressed_button, ButtonAction):
            self.__canvas_handler.do_action(self)

    def draw(self):
        self.__screen.fill("black")

        for shape in self.shapes:
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

    def reset_mouse(self):
        self.mouse_positions = []

    def __action_reset(self):
        self.pressed_button = None

    def reset_all_buttons(self):
        if self.pressed_button:
            self.pressed_button.reset()
        self.reset_mouse()
        self.__action_reset()
        self.pressed_button = None

    def dump_to_file(self):
        with open(FILE_TO_SAVE, "wb") as f:
            pickle.dump(self.shapes, f, pickle.HIGHEST_PROTOCOL)

    def load_file(self):
        content = []
        try:
            with open(FILE_TO_SAVE, "rb") as f:
                content = pickle.load(f)
        except (FileNotFoundError, EOFError):
            pass
        self.shapes = content


class CanvasHandler:
    def do_action(self, canvas: Canvas):
        canvas.pressed_button.press()
        if isinstance(canvas.pressed_button, HelpButton):
            canvas.pressed_button.reset()
            canvas.pressed_button = None

        if isinstance(canvas.pressed_button, CanvasCleanerButton):
            canvas.shapes = []
            canvas.reset_all_buttons()

        if isinstance(canvas.pressed_button, ShapeEraserButton):
            for shape in canvas.shapes:
                if canvas.mouse_positions:
                    if shape.has_collision(canvas.mouse_positions[-1]):
                        canvas.shapes.remove(shape)
                        canvas.reset_mouse()
                        break

    def make_shape(self, canvas: Canvas):
        if len(canvas.mouse_positions) == 2 and type(canvas.pressed_button) in [
            RectButton,
            CircleButton,
            LineButton,
        ]:
            self.__make(canvas)
        return canvas

    def __make(self, canvas: Canvas):
        shape = canvas.pressed_button.press(canvas.mouse_positions)
        canvas.shapes.append(shape)
        canvas.reset_mouse()
