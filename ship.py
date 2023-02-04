import pygame

class space_ship():

    def __init__(self, screen, ai_settings):
        """ Initialize athe ship and set its starting position. """
        self.screen = screen
        self.ai_settings = ai_settings
        
        # Load the ship image and get its rect.
        self.image = pygame.image.load('D:/PYTHON/Alien_Invasion/images/alien_ship.png')

        # rect attribute - it's an attribute that pygame treat it as element like rectangle.
        # get the ship's rect attribute
        self.ship_rect = self.image.get_rect()
        
        # get the screen's rect attribute
        self.screen_rect = screen.get_rect()

        # Set position of space-ship at the bottom center of the screen.
        self.ship_rect.centerx = self.screen_rect.centerx 
        self.ship_rect.bottom = self.screen_rect.bottom
        # centerx = gives x-coordinate of the rectangle object's center
        # bottom = gives y-coordinate of the rectangle object's bottom

        # Store a decimal value for the ship's center
        self.center = float(self.ship_rect.centerx)

        # movement flag
        self.moving_right = False
        self.moving_left = False

    def update_ship(self):
        # if right arrow key is still pressed then move ship to right
        # Update the ship's center value, not the rect
        if self.moving_right and self.ship_rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed
            # self.ship_rect.centerx += 1
            # print('ship move one step right')
        
        if self.moving_left and self.ship_rect.left > 0:
            self.center -= self.ai_settings.ship_speed
            # self.ship_rect.centerx -= 1
            # print('ship move one step left')
        
        # Update rect object from self.center
        self.ship_rect.centerx = self.center

        """ 
            in this we can use if and elif block 
            but is user pressed both the first it will increase and the decrease by 1
            hence, ship will standing still at same position.
        """

    def set_ship(self):
        """ draw the image to the screen at the position specified by 'self.img_rect' """
        self.screen.blit(self.image, self.ship_rect)

