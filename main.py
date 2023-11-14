import pygame
from classes.canvas import Canvas
from constants import FPS


def main():
    canvas = Canvas()
    clock = pygame.time.Clock()
    canvas.load_file()

    while True:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                canvas.dump_to_file()
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if canvas.pressed_button:
                    canvas.mouse_positions.append(event.pos)
                else:
                    canvas.check_button_pressed(event.pos)
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_ESCAPE]:
                    canvas.reset_all()

        canvas.update()
        canvas.draw()


if __name__ == "__main__":
    main()
