import pygame
from pygame.sprite import Group
from setting import Settings
from ship import space_ship
import game_functions as gf

def run_game():
    # Initialization of the game
    pygame.init()

    # create a instance of setting of alien invasion
    ai_setting = Settings()

    # create a screen object. It also know as surface
    screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a ship.
    ship = space_ship(screen, ai_setting)

    # make a group to store bullets.
    bullets = Group()

    # Start the main loop for the game. surface automatically redraw on every pass through the loop.
    while True:

        # Respond to keypresses and mouse events.
        gf.check_events(ship, screen, ai_setting, bullets)

        # if right key is still pressed then move ship to the right/left
        ship.update_ship()

        # update bullet position
        gf.update_bullets(bullets)

        # update screen directly through module
        gf.update_screen(screen, ai_setting, ship, bullets)


# initialize the game and start the main loop.
run_game()
print("Starting game")