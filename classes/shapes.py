import pygame


class Shape:
    def __init__(self) -> None:
        self.shape = None

    def draw(self):
        raise NotImplementedError


class Rectangle(Shape):
    def draw(self, screen):
        pygame.draw.rect(screen, "blue", self.shape)


class Circle(Shape):
    def draw(self, screnn):
        pygame.draw.circle(screnn, "yellow", *self.shape)
