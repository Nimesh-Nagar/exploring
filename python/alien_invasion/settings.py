''' A class to store all settings for Alien Invasion. '''
class Settings:

    def __init__(self):

        #screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230) # white 
        # self.bg_color = (0, 0, 255) # blue

        # Ship settings
        self.ship_speed = 1.5
        
        #Bullet Settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60) # dark gray

        