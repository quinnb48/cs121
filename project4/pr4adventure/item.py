import os
allItems = []

def findItemLoc(name):
    #returns location name of any item, for save function
    for i in allItems:
        if i.name.lower() == name:
            return i.locName

def findItem(name): #gives item object
    for i in allItems:
        if i.name.lower() == name.lower():
            return i

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Item:

    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        self.loc = None
        self.locName = "nowhere"
        self.type = None

    def describe(self):
        clear()
        print(self.desc)
        print()
        input("Press enter to continue...")

    def putInRoom(self, room):
        self.loc = room
        self.locName = room.name
        room.addItem(self)
        allItems.append(self)

class Food(Item):
    def __init__(self, name, desc, health):
        Item.__init__(self, name, desc)
        self.type = "food"
        self.healing = health

class Key(Item):
    def __init__(self, name, desc, num):
        Item.__init__(self, name, desc)
        self.type = "key"
        self.num = num

class Body(Item):
    def __init__(self, name, desc):
        Item.__init__(self, name, desc)
        self.type = "body"

    def putInRoom(self, room):
        self.loc = room
        self.locName = room.name
        room.addBody(self)

    def cleanUp(self):
        self.describe()
        self.loc.removeBody(self)
        self.loc = None
        self.locName = "nowhere"

    def silentCleanUp(self):
        self.loc.removeBody(self)
        self.loc = None
        self.locName = "nowhere"

class Flashlight(Item):
    def __init__(self, name, desc, desc2):
        Item.__init__(self, name, desc)
        self.desc2 = desc2
        self.type = "flashlight"
        self.powered = False

    def replaceBatteries(self):
        self.powered = True

    def describe(self):
        if(self.powered):
            Item.describe()
        else:
            def describe(self):
                clear()
                print(self.desc2)
                print()
                input("Press enter to continue...")

class Npc(Item):
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        self.loc = None
        self.locName = "nowhere"
        self.status = "injured"
        self.type = "npc"

    def startConvo(self):
        clear()
        print("Your boss says:")
        print('''"Finally! What took you so long? Listen, my leg is broken. I need you to
        press that button over there. It'll turn my greatest doomsday device on, ending France
        permanently! Ahahahahaha!"''')
        print('"..."')
        print(''"Well? What are you waiting for? You'll get a bonus or something, probably."'')
        print()
        chosen = False
        while not chosen:
            decision = input("Press the button? ")
            decision = decision.split()
            if(decision[0].lower() == "yes"):
                return True
            elif(decision[0].lower() == "no"):
                return False

    def putInRoom(self, room):
        self.loc = room
        self.locName = room.name
        allItems.append(self)
