from random import random

# * * * * * * * * * * * conway * * * * * * * * * * *
#
# Example of a grid rule. This rule gets applied to
# each grid cell, inspecting its state and the states
# of its eight neighbor cells, and is used to determine
# its next state.
#
# This particular rule encodes the behavior of Conway's
# game of life simulation.  It takes two parameters:
#
#   cntr: the state of the grid cell being inspected
#
#   nbrs: collection of states of the 8 grid neighbors
#         that sit around the cell being inspected
#
# This rule interprets states of 0 as "dead" and
# states of 1 and above as being "alive".
#
# Live cells die if they have too many or too many
# living neighbors.
#
# Dead cells come alive if they have just the
# right number of live neighbors.
#
# See the if/else below for details.
#
def conway(cntr,nbrs):

  # live
  #
  # Helper function that returns 1/0 if live/dead.
  def life(cell_value):
    if cell_value > 0:
      return 1
    else:
      return 0

  #
  # count the number of living neighbors
  #
  living = life(nbrs.NW) + life(nbrs.N) + life(nbrs.NE) \
           + life(nbrs.W) + life(nbrs.E) \
           + life(nbrs.SW) + life(nbrs.S) + life(nbrs.SE)

  #
  # determine next state
  #
  # if alive...
  if life(cntr) == 1:
    # and there are two or three live neighbors...
    if living == 2 or living == 3:
      # survive
      return cntr
    else:
      # otherwise, die.
      return 0
  #
  # if dead...
  else:
    # but there are three live neighbors...
    if living == 3:
      # come alive.
      return 100
    else:
      return 0
#
#
# * * * * * * * * * * * conway * * * * * * * * * * *



# * * * * * * * * * generational * * * * * * * * * * *
#
# This performs Conway's game of life except, when a
# cell is alive (1-100), its value is interpreted as
# its "generation".  This means that, when a live cell
# is born, it takes on the value that's one more than
# the max value of its live neighbors.
#
def generational(cntr,nbrs):

  # live
  #
  # Helper function that returns 1/0 if live/dead.
  def life(cell_value):
    if cell_value > 0:
      return 1
    else:
      return 0

  #
  # count the number of living neighbors
  #
  living = life(nbrs.NW) + life(nbrs.N) + life(nbrs.NE) \
           + life(nbrs.W) + life(nbrs.E) \
           + life(nbrs.SW) + life(nbrs.S) + life(nbrs.SE)

  largest = max(nbrs.NW,nbrs.N,nbrs.NE,nbrs.W,
                nbrs.SE,nbrs.S,nbrs.SW,nbrs.E)
  #
  # determine next state
  #
  # if alive...
  if life(cntr) == 1:
    # and there are two or three live neighbors...
    if living == 2 or living == 3:
      # survive
      return cntr
    else:
      # otherwise, die.
      return 0
  #
  # if dead...
  else:
    # but there are three live neighbors...
    if living == 3:
      # come alive, marking your new generation
      return 1+largest
    else:
      return 0
#
#
# * * * * * * * * * generational * * * * * * * * * * *

# * * * * * * * * * * * blur * * * * * * * * * * * * *
#
# Example of an image processing rule.  This blurs an
# image.  A cell becomes the average of itself with
# the average value of its neighbors.  This "blends"
# greys and "smooths" out sharp transitions.  The
# effect of a bright pixel is spread over an area
# of the image, centered at that pixel.

def blur(cntr,nbrs):

  # compute the average value of my neighbors
  avg = (nbrs.N + nbrs.E + nbrs.S + nbrs.W)//4

  # change state so that I'm closer to their average
  return (cntr + avg) // 2

#
#
# * * * * * * * * * * * blur * * * * * * * * * * * * *

# * * * * * * * * * * negative * * * * * * * * * * * *
#
# This inverts brightness to darkness, and vice versa,
# in an image.  The effect makes the image look like
# a photographic negative.
#
def negative(cntr,nbrs):
   return 255 - cntr
#
#
# * * * * * * * * * * negative * * * * * * * * * * * *

#mmmmy codes

# * * * * * * * * * ages and dies * * * * * * * * * * *
#
def ages(cntr,nbrs):

    if (cntr == 100):
        cntr=0
    elif(cntr>0):
        cntr+=1

    return cntr
#works
# * * * * * * * * * ages and dies * * * * * * * * * * *

# * * * * * * * * * * * decays * * * * * * * * * * * * *
#
def decay(cntr,nbrs):
    # live
    #
    # Helper function that returns 1/0 if live/dead.
    def life(cell_value):
        if cell_value == 100:
            return 1
        else:
            return 0

            #
    # count the number of living neighbors
    #
    living = life(nbrs.NW) + life(nbrs.N) + life(nbrs.NE) \
            + life(nbrs.W) + life(nbrs.E) \
            + life(nbrs.SW) + life(nbrs.S) + life(nbrs.SE)

            #
    # determine next state
    #
    # if alive...
    if life(cntr) == 1:
        # and there are two or three live neighbors...
        if living == 2 or living == 3:
            # survive
            return cntr
        else:
            # otherwise, die.
            return cntr-1
            #
            # if dead...
    else:
            # but there are three live neighbors...
        if living == 3:
        # come alive.
            return 100
        else:
            return cntr-1
#works
# * * * * * * * * * * * decays * * * * * * * * * * * * *

# * * * * * * * * * * * contrast * * * * * * * * * * * * *
#
def contrast(cntr,nbrs):
    if(cntr<=50):
        cntr-=1
        return cntr
    else:
        cntr+=1
        return cntr
#works
# * * * * * * * * * * * contrast * * * * * * * * * * * * *

# * * * * * * * * * * * sharpen * * * * * * * * * * * * *
#
def sharpen(cntr,nbrs):
      # compute the average value of my neighbors
      avg = (nbrs.N + nbrs.E + nbrs.S + nbrs.W)//4

      if(cntr>=avg):
          return (cntr + 1)
      else:
          return (cntr - 1)
#works
# * * * * * * * * * * * sharpen * * * * * * * * * * * * *

# * * * * * * * * * * * shadow * * * * * * * * * * * * *
#
def shadow(cntr,nbrs):
    # live
    #
    # Helper function that returns 1/0 if live/dead.
    def life(cell_value):
        if cell_value == 100:
            return 1
        else:
            return 0
    #
    if(life(nbrs.NW)==1 and life(cntr)!=1):
        return 50
    else:
        return cntr
#works
# * * * * * * * * * * * shadow * * * * * * * * * * * * *

# * * * * * * * * * * * fill * * * * * * * * * * * * *
#
def fill(cntr,nbrs):
    if(cntr!=100):
        if(nbrs.N>0 and nbrs.N<100):
            return nbrs.N
        elif(nbrs.S>0 and nbrs.S<100):
            return nbrs.S
        elif(nbrs.W>0 and nbrs.W<100):
            return nbrs.W
        elif(nbrs.E>0 and nbrs.E<100):
            return nbrs.E
        else:
            return cntr
    else:
        return cntr
#works
# * * * * * * * * * * * fill * * * * * * * * * * * * *

# * * * * * * * programmer's choice 1 * * * * * * * * *
#
def flashflood(cntr,nbrs):
    #blinkingggg colors- draw two blobs of different colors. watch it go
    # Helper function that returns 1/0 if live/dead.
    def life(cell_value):
        if cell_value > 0:
            return 1
        else:
            return 0
    # count the number of living neighbors
    #
    living = life(nbrs.NW) + life(nbrs.N) + life(nbrs.NE) \
            + life(nbrs.W) + life(nbrs.E) \
            + life(nbrs.SW) + life(nbrs.S) + life(nbrs.SE)
    #
    average = (nbrs.NW + nbrs.N + nbrs.NE + nbrs.W + nbrs.E \
            + nbrs.SW + nbrs.S + nbrs.SE)/8
    #
    largest = max(nbrs.NW,nbrs.N,nbrs.NE,nbrs.W,
                  nbrs.SE,nbrs.S,nbrs.SW,nbrs.E)
    #
    if(life(cntr)==1):
        if(cntr<largest):
            return largest-1
        else:
            return cntr-5
    else:
        if(living==3):
            return 100
        else:
            return cntr

#
# * * * * * * * programmer's choice 1 * * * * * * * * *

# * * * * * * * programmer's choice 2 * * * * * * * * *
#expanding square that spreads color outwards in a square shape
def glow(cntr,nbrs):
    #
    largest = max(nbrs.NW,nbrs.N,nbrs.NE,nbrs.W,
                  nbrs.SE,nbrs.S,nbrs.SW,nbrs.E)
    #
    touchingColor= False
    #
    def between(x):
        if(x>0 and x<=100):
            return True
        else:
            return False
    #
    if(between(nbrs.NW)):
        touchingColor=True
    elif(between(nbrs.N)):
        touchingColor=True
    elif(between(nbrs.NE)):
        touchingColor=True
    elif(between(nbrs.W)):
        touchingColor=True
    elif(between(nbrs.SW)):
        touchingColor=True
    elif(between(nbrs.S)):
        touchingColor=True
    elif(between(nbrs.SE)):
        touchingColor=True
    elif(between(nbrs.E)):
        touchingColor=True
    #
    if(cntr==0):
        if(touchingColor):
            return largest
        else:
            return cntr
    elif(cntr==5):
        return 100
    else:
        return cntr-5

#
# * * * * * * * programmer's choice 2 * * * * * * * * *
