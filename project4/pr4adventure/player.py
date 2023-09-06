import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Player:
    def __init__(self):
        self.location = None
        self.inMainMenu = True
        self.name = ""
        self.items = []
        self.health = 50
        self.alive = True
        self.numBodiesCleaned = 0
        self.whichBodiesCleaned = []
        self.numExperimentsKilled = 0
        self.whichExperimentsKilled = []
        self.endingsFound = {"Fuck this shit I'm out":False,"Monster Hunter":False,"Action Hero":False,"At least you cleaned up after yourself":False,"Well at least you don't have to clean up this mess":False,\
        "E tu, brute?":False,"Fired":False,"Demoted":False,"Lazy":False,"Employee of the month":False,}
        self.inspectedBoxes = 0

    def goDirection(self, direction):
        room = self.location.getDestination(direction)
        if(room.locked == False):
            self.location = room
        else:
            print("You can't go in there, it's locked")

    def whatsThatDirection(self,direction): #gives room object
        return self.location.getDestination(direction)

    def pickup(self, item):
        self.items.append(item)
        item.loc = self
        item.locName = self.name
        self.location.removeItem(item)

    def placeInInventory(self, item, itemLoc): #for loading from game exit. itemLoc is where save says item should be
        if itemLoc.name != self.name:
            item.loc.removeItem(item)
            item.loc = itemLoc
            item.locName = itemLoc.name
            itemLoc.addItem(item)
        else:
            item.loc.removeItem(item)
            self.items.append(item)
            item.loc = self
            item.locName = self.name

    def resetPlaceInInventory(self,item,itemLoc):
            #item.loc.removeItem(item)
            item.loc = itemLoc
            item.locName = itemLoc.name
            itemLoc.addItem(item)

    def removeItem(self,item): #for non-confusion with reset game save
        if item in self.items:
            self.items.remove(item)
        item.loc = None
        item.locName = "nowhere"

    def useUpItem(self, item):
        self.items.remove(item)
        item.loc = None
        self.locName = "nowhere"

    def showInventory(self):
        clear()
        print("You are currently carrying:")
        print()
        for i in self.items:
            print(i.name + ": " + i.desc)
        print()
        input("Press enter to continue...")

    def getInventoryItemByName(self, name):
        for i in self.items:
            if i.name.lower() == name.lower():
                return i

        return False

    def getInventoryItemByType(self, type):
        for i in self.items:
            if i.type.lower() == type.lower():
                return i
        return False

    def getInventoryNameByType(self,type):
        for i in self.items:
            if i.type == type:
                print(i.name)
        return False

    def combineInventoryItems(self, item1, item2):
        item1 = self.getInventoryItemByName(item1)
        item2 = self.getInventoryItemByName(item2)
        if(item1 == False or item2 == False):
            return False
        elif(item1.name.lower() == "flashlight" and item2.name.lower() == "battery"):
            item1.replaceBatteries()
            self.useUpItem(item2)
            return True
        elif(item2.name.lower() == "flashlight" and item1.name.lower() == "battery"):
            item2.replaceBatteries()
            self.useUpItem(item1)
            return True
        else:
            return False

    def eat(self,item):
        if(item.type == "food"):
            self.health += item.healing
            self.useUpItem(item)
            print("Wow, you ate that. +" + str(item.healing) + " health")
            print()
            input("Press enter to continue...")
        else:
            print("You can't eat that.")
            print()
            input("Press enter to continue...")

    def attackMonster(self, mon):
        clear()
        print("You are attacking " + mon.name)
        print()
        print("Your health is " + str(self.health) + ".")
        print(mon.name + "'s health is " + str(mon.health) + ".")
        print()
        if self.health > mon.health:
            self.health -= mon.health
            print("You win. Your health is now " + str(self.health) + ".")
            mon.die()
            self.numExperimentsKilled+=1
            self.whichExperimentsKilled.append(mon.name)
        else:
            print("You lose.")
            self.alive = False
        print()
        input("Press enter to continue...")

    def gotEnding(self, num):
        return self.endingsFound[num]

    def getEnding(self, num):
        self.endingsFound[num] = True

    def stats(self):
        #prints player's stats
        print("Health: "+str(self.health))
        print("Bodies cleaned: "+str(self.numBodiesCleaned))
        print("Experiments killed: "+str(self.numExperimentsKilled))
        totalEndingsFound=0
        for x in self.endingsFound:
            if self.endingsFound[x] == True:
                totalEndingsFound+=1
        print("Total endings found: "+str(totalEndingsFound))
        input("Press enter to continue...")
