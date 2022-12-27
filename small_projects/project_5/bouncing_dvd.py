"""Bouncing DVD Logo, by Hideaki Fukami
A boucing DVD logo animation. You have to be "of a certain age" to appreciate this. Press Ctrl-C to stop.

NOTE: Do not resize the terminal window while this program is running."""

import sys, random, time

try:
    import bext
except imporError:
    print('This program requires the bext module, which you\ncan install by following the instructions at\nhttps://pypi.org/project/Bext/')
    sys.exit()

# Set up the constants:
WIDTH, HEIGH = bext.size()

# We can't print to the last column on Window without it adding a newline automatically, so reduce the width by one:
WIDTH -= 1

NUMBER_OF_LOGOS = 5
PAUSE_AMOUNT = 0.2
COLORS = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

UP_RIGHT = 'ur'
UP_LEFT = 'ul'
DOWN_RIGHT = 'dr'
DOWN_LEFT = 'dl'
DIRECTIONS = (UP_RIGHT, UP_LEFT, DOWN_RIGHT, DOWN_LEFT)

# Key names for logo dictionaries:
COLOR = 'color'
X = 'x'
Y = 'y'
DIR = 'direction'

def main():
    bext.clear()

    # Generate some logos.
    logos = []
    for i in range(NUMBER_OF_LOGOS):
        logos.append({COLOR: random.choice(COLORS),
                    X: random.randint(1, WIDTH - 4),
                    Y: random.randint(1, HEIGH - 4),
                    DIR: random.choice(DIRECTIONS)})
        if logos[-1][X] % 2 == 1:
            # X is even so it can hit the corner
            logos[-1][X] -= 1
    
    cornerBounces = 0 # Count how many times a logo hits a corner.
    while True:
        for logo in logos:
            bext.goto(logo[X], logo[Y])
            print('    ', end='')

            originalDirection = logo[DIR]

            # See if the logo bounces off the corners:
            if logo[X] == 0 and logo[Y] == 0:
                logo[DIR] = DOWN_RIGHT
                cornerBounces += 1
            elif logo[X] == 0 and logo[Y] == HEIGH-1:
                logo[DIR] = UP_RIGHT
                cornerBounces += 1
            elif logo[X] == WIDTH - 3 and logo[Y] == 0:
                logo[DIR] = DOWN_LEFT
                cornerBounces += 1
            elif logo[X] == WIDTH - 3 and logo[Y] == HEIGH - 1:
                logo[DIR] = UP_LEFT
                cornerBounces += 1
            
            # See if the logo bounces off the left edge:
            elif logo[X] == 0 and logo[DIR] == UP_LEFT:
                logo[DIR] = UP_RIGHT
            elif logo[X] == 0 and logo[DIR] == DOWN_LEFT:
                logo[DIR] = DOWN_RIGHT