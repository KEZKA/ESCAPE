import sys
import pygame


class BaseGame:
    def __init__(self, width, height):
        pygame.init()
        self.width, self.height = width, height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.FPS = 60

    def terminate(self):
        pygame.quit()
        sys.exit()
