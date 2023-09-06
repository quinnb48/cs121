# * * * * * * * * * ages and dies * * * * * * * * * * *
#
def ages(cntr,nbrs):
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
        #and has lived to 100...
        if(cntr==100):
            cntr=0
            #die
            # otherwise, if there are two or three live neighbors...
        elif living == 2 or living == 3:
            # go up one value
            cntr+=1
        else:
            # otherwise, die.
            cntr=0
        #
        # if dead...
    else:
        # but there are three live neighbors...
        if living == 3:
            # come alive, + one value.
            cntr+=1
        else:
            # otherwise do nothing
            cntr = cntr

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
