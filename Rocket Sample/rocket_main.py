import pygame
import sys

from rocket_ship import RocketShip

class RocketMain:

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        pygame.display.set_caption("Rocket Sample")
        self.rocket_ship = RocketShip(self)
        self.bg_color = (230,230,230)


    def run_game(self):
        while True:

            self._check_events()
            self.rocket_ship.update()
            self.screen.fill(self.bg_color)
            self.rocket_ship.blitme()
            pygame.display.flip()
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.rocket_ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.rocket_ship.moving_left = True
                elif event.key == pygame.K_UP:
                    self.rocket_ship.moving_up = True
                elif event.key == pygame.K_DOWN:
                    self.rocket_ship.moving_down = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.rocket_ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.rocket_ship.moving_left = False
                elif event.key == pygame.K_UP:
                    self.rocket_ship.moving_up = False
                elif event.key == pygame.K_DOWN:
                    self.rocket_ship.moving_down = False
                elif event.key == pygame.K_q:
                    sys.exit()
if __name__ =='__main__':
    ai = RocketMain()
    ai.run_game()