import pygame


class BaseGameStates:
    def __init__(self, game):
        self.game = game
        self.is_running = False

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
        self.handle_event()

    def render(self):
        # отрисовка
        pass

    def loop(self):
        # изменение величин при каждой отрисовке(или нет)
        pass

    def handle_event(self):
        # обработка событий
        pass
