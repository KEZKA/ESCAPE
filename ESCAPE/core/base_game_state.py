import pygame

from ESCAPE.sprites.arrow import Arrow


class BaseGameStates:
    def __init__(self, game):
        self.all_sprites = pygame.sprite.Group()
        self.game = game
        self.FPS = game.FPS
        self.screen = self.game.screen
        self.arrow = pygame.sprite.Group()
        Arrow(self, 0,0)
        self.is_running = False
        pygame.mouse.set_visible(False)

    def start(self):
        self.is_running = True
        self.execution()

    def stop(self):
        self.is_running = False

    def execution(self):
        while self.is_running:
            for event in pygame.event.get():
                self._handle_event(event)
            self.game.clock.tick(self.game.FPS)
            self.loop()
            self.render()
            pygame.display.flip()

    def _handle_event(self, event):
        if event.type == pygame.QUIT:
            self.stop()
            self.game.terminate()
        if event.type == pygame.MOUSEMOTION:
            self.arrow.update(event.pos)
        self.handle_event()

    def render(self):
        pass

    def loop(self):
        # изменение величин при каждой отрисовке(или нет)
        pass

    def handle_event(self):
        # обработка событий
        pass
