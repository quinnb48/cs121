from myRules import *
from Grid import Grid, GREYS, COLORS

print('Hit [DELETE] to reset.')
print('Hit [SPACE] to step.')
print('Hit [RETURN] to run.')
print('Hit \'q\' to quit.')


Grid(ages,
     '1. This runs a version of the game of life where color is\
      used to show a living cells age.',
     pattern='patterns/rpentamino.pat', generations=100)

Grid(decay,
     '2. This runs a version of the game of life where "bodies" of living cells\
 remain and decay through the color spectrum.',
     pattern='patterns/glider.pat', generations=98)

Grid(contrast,'3. This increase contrast in an image. Please hold down the space bar.',
    pattern='images/reed.pgm')

Grid(sharpen,'4. This will sharpen an image. Please hold down the space bar.',
    pattern='images/reed-square.pgm')

Grid(shadow,'5. This creates a shadow under a white square.',
    pattern='patterns/bounds.pat', generations=1)

Grid(fill,'6. This fills an empty white shape with a color placed in the middle.',
    pattern='patterns/fill.pat')

Grid(flashflood,'7. Floods across the screen from a starting point.\
    Bit of an epilepsy warning if you hold down the space bar.', pattern='patterns/glider.pat')

Grid(glow,'8. Expands out in a glow from a shape drawn.',
    pattern='patterns/spots.pat')
