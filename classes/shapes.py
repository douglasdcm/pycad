import pygame
import math


class Shape:
    def __init__(self) -> None:
        super().__init__()
        self.shape = None
        self.rect = ""
        self.image = ""

    def has_collision(mouse_position):
        raise NotImplemented

    def draw(self):
        raise NotImplementedError


class Rectangle(Shape):
    def draw(self, screen):
        pygame.draw.rect(screen, "blue", self.shape)

    def has_collision(self, mouse_position):
        return pygame.rect.Rect(*self.shape).collidepoint(mouse_position)


class Circle(Shape):
    def draw(self, screnn):
        pygame.draw.circle(screnn, "yellow", *self.shape)

    def has_collision(self, mouse_position):
        # circle shape: (center, radius)
        center = self.shape[0]
        radius = self.shape[1]
        if math.dist(center, mouse_position) <= radius:
            return True
        return False


class Line(Shape):
    def draw(self, screnn):
        pygame.draw.line(screnn, "red", *self.shape)

    def has_collision(self, mouse_position):
        error = 5
        # line shape: ((x1, y1), (x2, y2))
        start_line = self.shape[0]
        end_line = self.shape[1]
        dist_start = math.dist(start_line, mouse_position)
        dist_end = math.dist(mouse_position, end_line)
        dist_line = math.dist(start_line, end_line)
        if dist_start + dist_end <= dist_line + error:
            return True
        return False
