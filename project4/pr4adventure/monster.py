import random
import updater

allMonsters = []

def getMonster(name):
    for i in allItems:
        if i.name.lower() == name:
            return i

class Monster:
    def __init__(self, name, health, room):
        self.name = name
        self.health = health
        self.room = room
        allMonsters.append(self)
        room.addMonster(self)
        updater.register(self)

    def update(self):
        if random.random() < .5:
            self.moveTo(self.room.randomNeighbor())

    def moveTo(self, room):
        self.room.removeMonster(self)
        self.room = room
        room.addMonster(self)

    def die(self):
        self.room.removeMonster(self)
        updater.deregister(self)


class MinibossMonster(Monster):
    def update(self):
        #do nothing cuz I don't want it to move
        return None
