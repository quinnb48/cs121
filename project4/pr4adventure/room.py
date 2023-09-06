import random
allRooms = []

def findRoom(name,player): #gives room object from name
    for i in allRooms:
        if i.name.lower() == name.lower():
            return i
        elif name.lower() == player.name.lower():
            return player

def illuminateAllRooms():
    for i in allRooms:
        i.lit = True

class Room:

    def __init__(self, name, description):
        self.name = name
        self.desc = description
        self.monsters = []
        self.exits = []
        self.items = []
        self.bodies = []
        self.locked = False
        self.lit = True
        self.ending = "no"
        allRooms.append(self)

    def addExit(self, exitName, destination):
        self.exits.append([exitName, destination])

    def getDestination(self, direction):
        for e in self.exits:
            if e[0] == direction:
                return e[1]

    def connectRooms(room1, dir1, room2, dir2):
        #creates "dir1" exit from room1 to room2 and vice versa
        room1.addExit(dir1, room2)
        room2.addExit(dir2, room1)

    def oneWayConnect(room1, dir1, room2):
        #creates a one-way exit from room1 to room2
        room1.addExit(dir1, room2)

    def exitNames(self):
        return [x[0] for x in self.exits]

    def addItem(self, item):
        self.items.append(item)

    def removeItem(self, item):
        self.items.remove(item)

    def addMonster(self, monster):
        self.monsters.append(monster)

    def removeMonster(self, monster):
        self.monsters.remove(monster)

    def addBody(self, body):
        self.bodies.append(body)

    def removeBody(self, body):
        self.bodies.remove(body)

    def hasItems(self):
        return self.items != []

    def getItemByName(self, name):
        for i in self.items:
            if i.name.lower() == name.lower():
                return i
        return False

    def hasMonsters(self):
        return self.monsters != []

    def getMonsterByName(self, name):
        for i in self.monsters:
            if i.name.lower() == name.lower():
                return i
        return False

    def hasBodies(self):
        return self.bodies != []

    def getBodyByName(self, name):
        for i in self.bodies:
            if i.name.lower() == name.lower():
                return i
        return False

    def randomNeighbor(self):
        return random.choice(self.exits)[1]

    def changeDesc(self, newDesc):
        self.desc = newDesc

class LockedRoom(Room):
    def __init__(self, name, description, key):
        Room.__init__(self, name, description)
        self.locked = True
        self.key = key
        self.lit = False

    def illuminate(self):
        self.lit = True

    def darken(self):
        self.lit = False

    def unlock(self):
        self.locked = False

    def lock(self):
        self.locked = True

class EndRoom(Room):
    def __init__(self, name, description, endingNum):
        Room.__init__(self,name, description)
        self.ending = endingNum
