import random
import tkinter
random.seed()

def plot(xvals, yvals):
    # This is a function for creating a simple scatter plot.  You will use it,
    # but you can ignore the internal workings.
    root = tkinter.Tk()
    c = tkinter.Canvas(root, width=700, height=400, bg='white') # Was 350 x 280
    c.grid()
    # Create the x-axis.
    c.create_line(50,350,650,350, width=3)
    for i in range(5):
        x = 50 + (i * 150)
        c.create_text(x,355,anchor='n', text='%s'% (.5*(i+2) ) )
    # Create the y-axis.
    c.create_line(50,350,50,50, width=3)
    for i in range(5):
        y = 350 - (i * 75)
        c.create_text(45,y, anchor='e', text='%s'% (.25*i))
    # Plot the points.
    for i in range(len(xvals)):
        x, y = xvals[i], yvals[i]
        xpixel = int(50 + 300*(x-1))
        ypixel = int(350 - 300*y)
        c.create_oval(xpixel-3,ypixel-3,xpixel+3,ypixel+3, width=1, fill='red')
    root.mainloop()

# Constants: setting these values controls the parameters of your experiment.
injurycost     = 10   # Cost of losing a fight
displaycost    = 1   # Cost of displaying between two passive birds
foodbenefit    = 8   # Value of the food being fought over
init_hawk      = 0
init_dove      = 0
init_defensive = 0
init_evolving  = 150

########
# Your code here
########

class World:
    def __init__(self):
        self.birds=[]
        self.numBirds=0

    def update(self):
        for i in self.birds:
            i.update()

    def free_food(self,num):
        while num > 0:
            b=random.randrange(len(self.birds))
            self.birds[b].eat()
            num-=1

    def conflict(self,num):
        while num > 0:
            b1=random.randrange(len(self.birds))
            b2=random.randrange(len(self.birds))
            while(b1==b2):
                b2=random.randrange(len(self.birds))
            self.birds[b1].encounter(self.birds[b2])
            num-=1

    def status(self):
        doves=0
        hawks=0
        defense=0
        for i in self.birds:
            if(i.species == "Dove"):
                doves+=1
            elif(i.species == "Hawk"):
                hawks+=1
            elif(i.species == "Defensive"):
                defense+=1
        print("Number of doves: " + str(doves))
        print("Number of hawks: " + str(hawks))
        print("Number of defensives: " + str(defense))

    def evolvingPlot(self):
        weights=[]
        aggro=[]
        for i in self.birds:
            weights.append(i.weight)
            aggro.append(i.aggression)
        plot(weights,aggro)

class Bird:
    def __init__(self,world):
        world.birds.append(self)
        world.numBirds+=1
        self.world=world
        self.health=100

    def eat(self):
        self.health+=foodbenefit

    def injured(self):
        self.health-=injurycost

    def display(self):
        self.health-=displaycost

    def die(self):
        self.world.birds.remove(self)

    def update(self):
        self.health-=1
        if(self.health<=0):
            self.die()
        return self

class Dove(Bird):
    def __init__(self,world):
        Bird.__init__(self,world)
        self.species="Dove"

    def update(self):
        Bird.update(self)
        if(self.health>=200):
            self.health-=100
            Dove(self.world)
        return self

    def defend_choice(self):
        return False

    def encounter(self,otherBird):
        if(otherBird.defend_choice()):
            #run away
            otherBird.eat()
        else:
            #display for food, one eats
            self.display()
            otherBird.display()
            picked=random.randrange(1,3)
            if(picked==2):
                self.eat()
            else:
                otherBird.eat()
        return self

class Hawk(Bird):
    def __init__(self,world):
        Bird.__init__(self,world)
        self.species="Hawk"

    def update(self):
        Bird.update(self)
        if(self.health>=200):
            self.health-=100
            Hawk(self.world)
        return self

    def defend_choice(self):
        return True

    def encounter(self,otherBird):
        if(otherBird.defend_choice()==False):
            #chase away other bird, eat
            self.eat()
        else:
            #fight, random one gets injured, other gets to eat
            picked=random.randrange(1,3)
            if(picked==2):
                self.eat()
                otherBird.injured()
            else:
                otherBird.eat()
                self.injured()
        return self

class Defensive(Dove):
    def __init__(self,world):
        Bird.__init__(self,world)
        self.species="Defensive"

    def defend_choice(self):
        return True

    def update(self):
        Bird.update(self)
        if(self.health>=200):
            self.health-=100
            Defensive(self.world)
        return self

class Evolving(Bird):
    def __init__(self,world,parent):
        Bird.__init__(self,world)
        self.species="Evolving"
        self.parent=parent
        if(parent == None):
            self.aggression=random.random()
            self.weight=random.uniform(1,3)
        else:
            self.aggression = self.parent.aggression + random.uniform(-0.05,0.05)
            if(self.aggression>1):
                self.aggression=1
            elif(self.aggression<0):
                self.aggression=0
            self.weight = self.parent.weight + random.uniform(-0.1,0.1)
            if(self.weight>3):
                self.weight=3
            elif(self.weight<1):
                self.weight=1

    def update(self):
        self.health -= .4 + .6*self.weight
        if(self.health<=0):
            self.die()
        if(self.health>=200):
            self.health-=100
            Evolving(self.world,self)
        return self

    def defend_choice(self):
        chance=random.random()
        if(chance<=self.aggression):
            return True
        else:
            return False

    def encounter(self,otherBird):
        if(otherBird.defend_choice()==False):
            #chase away other bird, eat
            self.eat()
        else:
            #fight, random one gets injured, other gets to eat
            if(self.health<=0):
                print(self.health)
            if(otherBird.health<=0):
                print(otherBird.health)
            prob=self.weight/(self.weight+otherBird.weight)
            #if(random.uniform(.25,.75)<=prob):
            if(random.random()<=prob):
                self.eat()
                otherBird.injured()
                if(otherBird.health<=0):
                    otherBird.die()
            else:
                otherBird.eat()
                self.injured()
                if(self.health<=0):
                    self.die()
        return self

########
# The code below actually runs the simulation.  You shouldn't have to do anything to it.
########
w = World()
for i in range(init_dove):
    Dove(w)
for i in range(init_hawk):
    Hawk(w)
for i in range(init_defensive):
    Defensive(w)
for i in range(init_evolving):
    Evolving(w,None)

for t in range(10000):
    w.free_food(10)
    w.conflict(50)
    w.update()
#w.status()
w.evolvingPlot()    # This line adds a plot of evolving birds. Uncomment it when needed.
