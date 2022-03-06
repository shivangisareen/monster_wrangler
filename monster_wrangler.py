from winsound import PlaySound
import pygame, random

# initialise pygame
pygame.init()

# create the display
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Monster Wrangler!")

# set FPS and clock
FPS = 60
clock = pygame.time.Clock()


# define classes
class Game():
    """A class to control game play"""
    def __init__ (self):
        """Initialise the game object"""
        pass

    def update(self):
        """Update the game object"""
        pass

    def draw(self):
        """Draw the HUD to the display"""
        pass

    def check_collisions(self):
        """Check for collisions between the player and monsters"""
        pass

    def start_new_round(self):
        """Populate display with new monsters"""
        pass

    def choose_target_monster(self):
        """Choose a new target monster for the player"""
        pass
    
    def pause_game(self):
        """Pause the game"""
        pass

    def reset_game(self):
        """Reset the game"""
        pass


class Player(pygame.sprite.Sprite):
    """A player class that the user can control """
    def __init__(self):
        """Initialise the player"""
        pass

    def update(self):
        """Update the player"""
        pass

    def warp(self):
        """Warp the player to the bottom of the display (safe zone)"""
        pass

    def reset_player(self):
        """Resets the player position"""
        pass


class Monster(pygame.sprite.Sprite):
    """Class to create enemy monster objects"""
    def __init__(self):
        """Initialise the monster"""
        pass

    def update(self):
        """Update the monster"""
        pass



# main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    # update the display and tick the clock
    display_surface.update()
    clock.tick(FPS)



pygame.quit()