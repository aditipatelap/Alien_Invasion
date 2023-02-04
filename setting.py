class Settings():
    """ A class which stores all settings of alien invasion. """

    def __init__(self):
        """ Initialize the settings """

        # screen settings
        self.screen_width = 800
        self.screen_height = 550
        self.background_color = (220, 200, 178)

        # ship settings
        self.ship_speed = 0.3

        # bullet settings
        self.bullet_speed = 0.2
        self.bullet_width = 2
        self.bullet_height = 10
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 5

