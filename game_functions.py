import sys
import pygame
from bullet import Bullet
# sys module to exit the game when the player quits.

def check_events(ship, screen, ai_setting, bullets):
    """ Event loop - watch keyboard and mouse events and 
        take appropriate action on particular event. """
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # when key pressed make moving flag true, according to the direction
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship, screen, ai_setting, bullets)

        # when key released make moving flag false, according to the direction
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
            

def check_keydown_events(event, ship, screen, ai_setting, bullets):
    """Respond to keypresses."""
    # if right arrow key is pressed
    if event.key == pygame.K_RIGHT:
        # print("right arrow key pressed")
        ship.moving_right = True
    
    # if left arrow key is pressed
    elif event.key == pygame.K_LEFT:
        # print("left arrow key pressed")
        ship.moving_left = True
    
    # if space bar is pressed
    elif event.key == pygame.K_SPACE:
        fire_bullets(screen, ship, ai_setting, bullets)


def fire_bullets(screen, ship, ai_setting, bullets):
    """ Fire a bullet if limit not reached yet. """
    # Create a new bullet and add it to the bullets group
    if len(bullets) < ai_setting.bullets_allowed:
        new_bullet = Bullet(screen, ship, ai_setting)
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
    """ Respond to key releases. """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def update_bullets(bullets):
    """ Update position of bullets and get rid of old bullets. """

    # bullets.update() calls bullet.update() for each bullet we place in the group bullets.
    bullets.update()

    # Get rid of bullets that have disappeared
    for bullet in bullets.copy():
        if bullet.bullet_rect.bottom <= 0:
            bullets.remove(bullet)
        # print(len(bullets))


def update_screen(screen, ai_setting, ship, bullets):
    """ Update images on the screen and flip to the new screen. """

    # redraw the screen during each pass through the loop.
    screen.fill(ai_setting.background_color)
    
    # Redraw all bullets behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # call set_ship() after filling the background, so the ship appears on top of the background
    # set ship on top of the screen 
    ship.set_ship()

    # Make the most recently drawn screen visible using this command.
    pygame.display.flip()
    