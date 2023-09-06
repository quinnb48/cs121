from room import *
from player import Player
from item import *
from monster import *
import os
import updater
import json #for saving files

player = Player()

#THINGS TO ADD:

def createWorld():
    #create rooms
    mainMenu = Room("mainmenu",'''Welcome to Janitor! //PLEASE NOTE: the saving/loading functions are in\n
    progress but the game literally won't run without them''')
    start = LockedRoom("start",'''You are in the changing room of your boss's, Dr. E. Vil. Scientist's, \n
    evil lair. It's only your first day but you've already been called in for overtime because \n
    some experiments apparently got out and have been destroying everything, though your boss doesn't \n
    want you to kill them for some reason. The door in front of you leads inside and locks once you've gone through.\n
    You should grab your supplies first, the key to the door is in them. ''', "un-unlockable") #don't want to go back in once through so no key to this door
    start.illuminate()
    frntdoor = EndRoom("frntdoor","Congratulations, you have left the building and your job behind. Good riddance to that mess. ", "Fuck this shit I'm out")
    hw1 = LockedRoom("hw1",'''You are now in the floor 1 hallway. There's a bathroom and break room \n
    to the right, and a staircase ahead. Also it looks like someone messed with the lights, \n
    they're flickering pretty badly. You should find a flashlight or something. ''', "cleaning supplies") #locked room, need cleaning supplies to enter
    hw1.illuminate()
    br1f1 = Room("br1f1",'''This is the floor 1 break room. There are snacks and a destroyed, \n
    drained vending machine. Looks like someone got vicious.''')
    bt1f1 = Room("bt1f1",'''You are in the floor 1 bathroom. Nothing here but an empty soap dispenser. ''')
    hw2 = Room("hw2",'''You have entered the floor 2 hallway. There's a lab and a dark room \n
    to the right, plus another lab and a bathroom on the left. ''')
    lb1f2 = Room("lb1f2",'''You have entered the lab on your left. It's a complete mess. Looks \n
    like there's a dead body in the corner. ''')
    bt1f2 = Room("bt1f2",'''You have entered the bathroom on floor 2. It's small and dank. The \n
    company skeleton, Indiana Bones, 'lives' here. It's kind of like a morbid mascot. ''')
    lb2f2 = Room("lb2f2",'''You have entered the lab on your right. Someone's turned the lights \n
    onto the 'spooky' setting. ''')
    dscf2 = LockedRoom("dscf2",'''It's the company's official Disco Room. See, there were some perks to \n
    working here. ''', "supply") #darkened room
    dscf2.unlock()
    hw3 = Room("hw3",'''You have entered the floor 3 hallway. There's a well-used lab to the left, \n
    and three cells to the right. The first one looks broken out of. ''')
    lb1f3 = Room("lb1f3",'''You have entered the lab on your left. It's mostly unused. There are \n
    beakers scattered all over, spare parts to random unfinished things, and an old pile of \n
    crates in a corner. ''')
    clstf3 = LockedRoom("clstf3",'''Someone should really fix those lights... anyway, looks like \n
    there's nothing in here but a bunch of trash. Oh hey, and a key! Neat. ''', "supply") #hidden and darkened room
    clstf3.unlock()
    cell1f3 = Room("cell1f3","You've entered the first cell on the right. It's empty. No bodies here to clean. ")
    cell2f3 = LockedRoom("cell2f3","You've entered the second cell on the right. It stinks in here. ", "cell key") #locked room, key A
    cell2f3.illuminate()
    cell3f3 = LockedRoom("cell3f3","You've entered the third cell on the right. It's empty. ", "cell key") #locked room, key A
    cell3f3.illuminate()
    hwf4 = Room("hwf4",'''You have entered the floor 4 hallway. There's the fancy break room and \n
    another cell to your left, and two more cells on the right. An overturned cleaning cart \n
    lies in the middle of the hallway, filled with useful things. Like bags. And batteries. ''')
    br1f4 = Room("br1f4",'''You've entered the fancy break room. Oh hey, they've got the good \n
    vending machine in here.''')
    cell4f4 = LockedRoom("cell4f4",'''You've entered the first cell on the right. It's also a mess. \n
    Someone should really clean this place up a bit. Not you though, that part's not your job. ''', "cell key") #locked room, key A
    cell4f4.illuminate()
    cell5f4 = Room("cell5f4",'''You've entered the cell on your left. This one looks much cleaner \n
    and nicer than the other ones. ''')
    emptyrf4 = Room("emptyrf4",'''It's a very large, very sturdy, very empty room. There's nothing \n
    in here but old suspicious stains. A giant metal door takes up the opposite wall. \n
    It's covered in dents and giant scratches. You probably shouldn't mess with it. ''')
    sprcellf4 = LockedRoom("sprcellf4",'''For some reason, you've entered the ominous giant door. This \n
    was a mistake. ''', "super-cell key") #locked room, key C
    sprcellf4.illuminate()
    mainlabf4 = LockedRoom("mainlabf4",'''You have finally entered your boss's main lab. It's an absolute \n
    disaster in here. Your boss stands in an evil-looking chair with a broken arm. You should \n
    probably talk to him. ''', "main lab key") #locked room, key B. Can attack boss? But he's also npc?
    mainlabf4.illuminate()
    #other ending rooms here
    two=EndRoom("two",'''Congratulations, you've successfully went out of your way to destroy the giant experiment\n
    monster thingy even though it wasn't your job.''',"Monster Hunter")
    three=EndRoom("three",'''Congratulations, you've killed a bunch of monsters and betrayed your boss and didn't clean\n
    up after yourself. Those secret agents you passed on the way out eventually turn up to hire you.''',"Action Hero")
    four=EndRoom("four","Congratulations, you did the exact opposite of what you were hired to do.","At least you cleaned up after yourself")
    five=EndRoom("five","Congratulations, you did the bare minimum of taking absolutely no actions.","Well at least you don't have to clean up this mess")
    six=EndRoom("six","Wow, you do your job good and then betray your boss like that. Top Ten Anime Betrayals.","E tu, brute?")
    seven=EndRoom("seven","wow, you did the exact opposite of your job and left your boss around to punish you for it. Smart.","Fired")
    eight=EndRoom("eight","Congrats, you cleaned up the place, but your boss' still mad you killed all his experiments.","Demoted")
    nine=EndRoom("nine",'''Congratulations. You did nothing except destroy France. You're not in trouble, but you're\n
    not in his good graces either.''',"Lazy")
    ten=EndRoom("ten",'''Congratulations, you did exactly what your boss wanted you to, even though none of this was in the\n
     job description! Yay!''',"Employee of the Month")
    #connect rooms
    Room.connectRooms(start, "forward", hw1, "back")
    Room.oneWayConnect(start, "outside", frntdoor)
    Room.connectRooms(hw1, "breakroom", br1f1, "back")
    Room.connectRooms(hw1, "bathroom", bt1f1, "back")
    Room.connectRooms(hw1, "upstairs", hw2, "downstairs")
    Room.connectRooms(hw2, "left lab", lb1f2, "back")
    Room.connectRooms(hw2, "bathroom", bt1f2, "back")
    Room.connectRooms(hw2, "right lab", lb2f2, "back")
    Room.connectRooms(hw2, "dark room", dscf2, "back")
    Room.connectRooms(hw2, "upstairs", hw3, "downstairs")
    Room.connectRooms(hw3, "lab", lb1f3, "back")
    Room.connectRooms(hw3, "first cell", cell1f3, "back")
    Room.connectRooms(hw3, "second cell", cell2f3, "back")
    Room.connectRooms(hw3, "third cell", cell3f3, "back")
    Room.connectRooms(hw3, "upstairs", hwf4, "downstairs")
    Room.connectRooms(hwf4, "breakroom", br1f4, "back")
    Room.connectRooms(hwf4, "left cell", cell5f4, "back")
    Room.connectRooms(hwf4, "right cell", cell4f4, "back")
    Room.connectRooms(hwf4, "right cell 2", emptyrf4, "back")
    Room.connectRooms(emptyrf4, "supercell", sprcellf4, "back")
    Room.connectRooms(hwf4, "main lab", mainlabf4, "back")
    #create items
    supply = Key("Cleaning supplies", "Your cleaning supplies. Put them to good use.", "supply")
    moreSupplies = Key("Cleaning supplies 2", "Some more cleaning supplies. Put them to good use.", "supply")
    cellKey = Key("Cell key", "The key to the cells. Looking at it makes you feel a bit guilty.", "cell key")
    superKey = Key("Super-cell key", "A giant metal key for a giant metal door.", "super-cell key")
    mainLabKey = Key("Main lab key", "Your boss should really invest in keycards or something.", "main lab key")
    flashlight = Flashlight("Flashlight", "A small flashlight, barely better than your phone light.",\
    "A small flashlight, dead. Needs batteries.")
    batteries = Item("Battery", "Some AAA for your flashlight. Hopefully not dead.")
    snacks1 = Food("Doritas", "A copyright-infringement-free bag of cheesy shapes", 10)
    susSand = Food("Suspicious sandwhich", '''You don't know how long it's been lying on that floor. You \
    don't know if you should trust it.''', 1)
    snacks2 = Food("N&N's", "", 10)
    partyHat = Item("Party hat", "A party hat for a party boy.")
    jars = Item("Organs jar", "Why would you pick this up.")
    poster = Item("Risque poster", '''A poster of a scantily clad lady doing something dangerous. \
    Nothing else notable. What, you thought there'd be a hole hidden behind it or something?''')
    boxes = Item("Strange boxes","Weirdly stacked boxes.")
    boss=Npc("boss","You haven't even talked to him and you can already tell he's an asshole")
    #place items
    supply.putInRoom(start)
    moreSupplies.putInRoom(hwf4)
    cellKey.putInRoom(br1f1)
    superKey.putInRoom(clstf3)
    mainLabKey.putInRoom(dscf2)
    flashlight.putInRoom(br1f1)
    batteries.putInRoom(hwf4)
    snacks1.putInRoom(br1f1)
    susSand.putInRoom(bt1f2)
    snacks2.putInRoom(br1f4)
    partyHat.putInRoom(dscf2)
    jars.putInRoom(dscf2)
    poster.putInRoom(cell5f4)
    boxes.putInRoom(lb1f3)
    boss.putInRoom(mainlabf4)
    #create bodies
    body1 = Body("Jim", "desc")
    body2 = Body("Ashley", "desc")
    body3 = Body("3", "desc")
    body4 = Body("4", "desc")
    body5 = Body("5", "desc")
    body6 = Body("6", "desc")
    body7 = Body("7", "desc")
    body8 = Body("8", "desc")
    skelly = Body("Indiana Bones", "desc")
    #place bodies
    body1.putInRoom(bt1f1)
    body2.putInRoom(lb1f2)
    body3.putInRoom(lb1f2)
    body4.putInRoom(hw3)
    body5.putInRoom(emptyrf4)
    body6.putInRoom(emptyrf4)
    body7.putInRoom(emptyrf4)
    body8.putInRoom(mainlabf4)
    skelly.putInRoom(bt1f2)
    #place people
    player.location = start
    #create & place monsters
    Monster("Loose experiment 1", 10, lb2f2)
    Monster("Loose experiment 2", 10, hw3)
    Monster("Loose experiment 3", 10, cell2f3)
    Monster("Loose experiment 4", 10, cell2f3)
    Monster("Loose experiment 5", 10, cell4f4)
    MinibossMonster("Big Heckin Experiment", 20, sprcellf4)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def printSituation():
    clear()
    if(player.location.lit == True):
        print(player.location.desc)
        print()
        if player.location.hasMonsters():
            print("This room contains the following loose experiments:")
            for m in player.location.monsters:
                print(m.name)
            print()
        if player.location.hasItems():
            print("This room contains the following items:")
            for i in player.location.items:
                print(i.name)
            print()
        if(player.location.hasBodies()):
            print("This room contains the following bodies:")
            for i in player.location.bodies:
                print(i.name + ": " + i.desc)
            print()
        if(player.location.name == "mainlabf4"):
            print("This room contains the following other people:")
            print("Your boss, Dr. E. Vil. Scientist")
            print()
        print("You can go in the following directions:")
        for e in player.location.exitNames():
            print(e)
        print()
    else:
        print("It's too dark to see anything in here.")
        print()
        print("You can go in the following directions:")
        for e in player.location.exitNames():
            print(e)
        print()

def showHelp():
    clear()
    print("go <direction> / enter <room> -- moves you in the given direction")
    print("inventory -- opens your inventory")
    print("pickup <item> -- picks up the item")
    print("eat <inventory item> -- gains health from an item in your inventory")
    print("combine <inventory item> -- combines one inventory item with another. possibly.")
    print("clean <thing> -- cleans up a mess")
    print("inspect <item> -- gives a description of something")
    print("unlock <room> -- unlocks an ajoining room")
    print("talk to <person> -- talk to a person")
    print("attack <experiment> -- fights an experiment")
    print("me -- displays player stats")
    print("save -- saves the game")
    print("main menu -- exits to main menu")
    print()
    input("Press enter to continue...")

def showMenu():
    clear()
    print("Welcome to Janitor!")
    print()
    print("New Game")
    print("Load Game")
    print("Restart Save")
    print("Exit")
    print()
    quitGame = False
    while player.inMainMenu:
        command = input("What will you do? ")
        while not command:
            print("Not a valid command")
            command = input("What will you do? ")
        commandWords = command.split()
        if(commandWords[0].lower() == "new"):
            print()
            player.name = input("Enter a name: ")
            f = open("listOfSavedGames.json", "a+")
            alreadySaved = False
            if len(f.read())!=0: #trying to check if already have a save of that name
                for x in f:
                    if player.name not in x.keys():
                        x.update({player.name:0})
                        f.write(json.dumps(x, indent=4))
                    else:
                        alreadySaved = True
                        print("Already a save of that name. ")
            else:
                for x in player.endingsFound: #try to update num endings found, recorded as the num next to player name
                    if player.endingsFound[x] == True:
                        totalEndingsFound+=1
                f.write(json.dumps({player.name:totalEndingsFound}, indent=4))
            f.close()
            player.inMainMenu = False
        elif(commandWords[0].lower() == "load"):
            f = open("listOfSavedGames.json", "r+")
            for x in f: #list saved games
                print(x)
            name = input("Which save? ")
            loadGame(name)
            player.inMainMenu = False
            f.close()
        elif(commandWords[0].lower() == "restart"):
            name = input("Which save? ")
            resetGameSave(name) #restart a save, but keep ending progress
            print("Save was restarted.")
        elif(commandWords[0].lower() == "exit"):
            player.inMainMenu = False
            quitGame = True

        else:
            print("Not a valid command")
    return quitGame


def saveGame():
    #Why is saving and loading so difficult and frustrating. I've mostly given up on fixing every little detail at this point
    #because it breaks otherwise
    p={
        "name": player.name,
        "player location": player.location.name,
        "player health": player.health,
        "hw1 locked": findRoom("hw1",player).locked,
        "cell 2 locked": findRoom("cell2f3",player).locked,
        "cell 3 locked": findRoom("cell3f3",player).locked,
        "cell 4 locked": findRoom("cell4f4",player).locked,
        "supercell locked": findRoom("sprcellf4",player).locked,
        "supply1 location": findItemLoc("cleaning supplies"),
        "supply2 location": findItemLoc("cleaning supplies 2"),
        "cell key location": findItemLoc('cell key'),
        "supercell key location": findItemLoc('super-cell key'),
        "main lab key location": findItemLoc('main lab key'),
        "flashlight location": findItemLoc('flashlight'),
        "flashlight lit": findItem("flashlight").powered,
        "batteries location": findItemLoc('battery'),
        "snacks1 location": findItemLoc("doritas"),
        "sandwhich location": findItemLoc('suspicious sandwhich'),
        "snacks2 location": findItemLoc("n&n's"),
        "hat location": findItemLoc('party hat'),
        "jars location": findItemLoc('organs jar'),
        "poster location": findItemLoc('risque poster'),
        "times inspected boxes": player.inspectedBoxes,
        "num bodies cleaned": player.numBodiesCleaned,
        "which bodies cleaned": player.whichBodiesCleaned,
        "exp killed": player.numExperimentsKilled,
        "which exp killed": player.whichExperimentsKilled,
        "endings found":
            {
                "Fuck this shit I'm out":player.endingsFound["Fuck this shit I'm out"],
                "Monster Hunter":player.endingsFound["Monster Hunter"],
                "Action Hero":player.endingsFound["Action Hero"],
                "At least you cleaned up after yourself":player.endingsFound["At least you cleaned up after yourself"],
                "Well at least you don't have to clean up this mess":player.endingsFound["Well at least you don't have to clean up this mess"],
                "E tu, brute?":player.endingsFound["E tu, brute?"],
                "Fired":player.endingsFound["Fired"],
                "Demoted":player.endingsFound["Demoted"],
                "Lazy":player.endingsFound["Lazy"],
                "Employee of the month":player.endingsFound["Employee of the month"]
            }
    }
    y = json.dumps(p, indent=4)
    f = open(player.name+".json", "w")
    f.write(y)
    f.close()
    f2 = open("listOfSavedGames.json", "r+")
    totalEndingsFound=0
    for x in player.endingsFound:
        if player.endingsFound[x] == True:
            totalEndingsFound+=1
    f2.write(json.dumps({player.name:totalEndingsFound}, indent=4))
    f2.close()

def loadGame(name):
    player.name = name
    f = open(player.name+".json", "r")
    s = json.loads(f.read())
    player.name = s["name"]
    player.location = findRoom(s["player location"],player)
    player.health = s["player health"]
    findRoom("hw1",player).locked = s["hw1 locked"]
    findRoom("cell2f3",player).locked = s["cell 2 locked"]
    findRoom("cell3f3",player).locked = s["cell 3 locked"]
    findRoom("cell4f4",player).locked = s["cell 4 locked"]
    findRoom("sprcellf4",player).locked = s["supercell locked"]
    player.placeInInventory(findItem("cleaning supplies"),findRoom(s["supply1 location"],player))
    player.placeInInventory(findItem("cleaning supplies 2"),findRoom(s["supply2 location"],player))
    player.placeInInventory(findItem('cell Key'),findRoom(s["cell key location"],player))
    player.placeInInventory(findItem('super-cell Key'),findRoom(s["supercell key location"],player))
    player.placeInInventory(findItem('main Lab Key'),findRoom(s["main lab key location"],player))
    player.placeInInventory(findItem('flashlight'),findRoom(s["flashlight location"],player))
    findItem("flashlight").powered = s["flashlight lit"]
    if findItem("flashlight").powered:
        illuminateAllRooms()
    player.placeInInventory(findItem('battery'),findRoom(s["batteries location"],player))
    player.placeInInventory(findItem('doritas'),findRoom(s["snacks1 location"],player))
    player.placeInInventory(findItem('suspicious sandwhich'),findRoom(s["sandwhich location"],player))
    player.placeInInventory(findItem("n&n's"),findRoom(s["snacks2 location"],player))
    player.placeInInventory(findItem('party Hat'),findRoom(s["hat location"],player))
    player.placeInInventory(findItem('organs jar'),findRoom(s["jars location"],player))
    player.placeInInventory(findItem('risque poster'),findRoom(s["poster location"],player))
    player.inspectedBoxes = s["times inspected boxes"]
    if player.inspectedBoxes >= 2:
        Room.connectRooms(player.location, "closet", findRoom("clstf3",player), "back")
    player.numBodiesCleaned = s["num bodies cleaned"]
    player.whichBodiesCleaned = s["which bodies cleaned"]
    for i in player.whichBodiesCleaned:
        findItem(i).silentCleanUp()
    player.numExperimentsKilled = s["exp killed"]
    player.whichExperimentsKilled = s["which exp killed"]
    for i in player.whichExperimentsKilled:
        getMonster(i).die()
    for num in player.endingsFound:
        player.endingsFound[num] = s["endings found"][num]
    f.close()


def resetGameSave(name):
    p={
        "name": player.name,
        "player location": "start",
        "player health": 50,
        "hw1 locked": True,
        "cell 2 locked": True,
        "cell 3 locked": True,
        "cell 4 locked": True,
        "supercell locked": True,
        "supply1 location": "start",
        "supply2 location": "hwf4",
        "cell key location": "br1f1",
        "supercell key location": "clstf3",
        "main lab key location": "dscf2",
        "flashlight location": "br1f1",
        "flashlight lit": False,
        "batteries location": "hwf4",
        "snacks1 location": "br1f1",
        "sandwhich location": "bt1f2",
        "snacks2 location": "br1f4",
        "hat location": "dscf2",
        "jars location": "dscf2",
        "poster location": "cell5f4",
        "times inspected boxes": 0,
        "num bodies cleaned": 0,
        "which bodies cleaned": [],
        "exp killed": 0,
        "which exp killed": [],
        "endings found":
            {
                "Fuck this shit I'm out":player.endingsFound["Fuck this shit I'm out"],
                "Monster Hunter":player.endingsFound["Monster Hunter"],
                "Action Hero":player.endingsFound["Action Hero"],
                "At least you cleaned up after yourself":player.endingsFound["At least you cleaned up after yourself"],
                "Well at least you don't have to clean up this mess":player.endingsFound["Well at least you don't have to clean up this mess"],
                "E tu, brute?":player.endingsFound["E tu, brute?"],
                "Fired":player.endingsFound["Fired"],
                "Demoted":player.endingsFound["Demoted"],
                "Lazy":player.endingsFound["Lazy"],
                "Employee of the month":player.endingsFound["Employee of the month"]
            }
    }
    player.location = findRoom("start",player)
    player.health = 50
    player.items=[]
    findRoom("hw1",player).locked = True
    findRoom("cell2f3",player).locked = True
    findRoom("cell3f3",player).locked = True
    findRoom("cell4f4",player).locked = True
    findRoom("sprcellf4",player).locked = True
    #don't actually think these comented out are necessary cuz of pre-game setup
    #player.resetPlaceInInventory(findItem("cleaning supplies"),findRoom("start",player))
    #player.resetPlaceInInventory(findItem("cleaning supplies 2"),findRoom("hwf4",player))
    #player.resetPlaceInInventory(findItem('cell Key'),findRoom("br1f1",player))
    #player.resetPlaceInInventory(findItem('super-cell Key'),findRoom("clstf3",player))
    #player.resetPlaceInInventory(findItem('main Lab Key'),findRoom("dscf2",player))
    #player.resetPlaceInInventory(findItem('flashlight'),findRoom("br1f1",player))
    findItem("flashlight").powered = False
    #player.resetPlaceInInventory(findItem('battery'),findRoom("hwf4",player))
    #player.resetPlaceInInventory(findItem('doritas'),findRoom("br1f1",player))
    #player.resetPlaceInInventory(findItem('suspicious sandwhich'),findRoom("bt1f2",player))
    #player.resetPlaceInInventory(findItem("n&n's"),findRoom("br1f4",player))
    #player.resetPlaceInInventory(findItem('party Hat'),findRoom("dscf2",player))
    #player.resetPlaceInInventory(findItem('organs jar'),findRoom("dscf2",player))
    #player.resetPlaceInInventory(findItem('risque poster'),findRoom("cell5f4",player))
    player.inspectedBoxes = 0
    player.numBodiesCleaned = 0
    player.whichBodiesCleaned = []
    player.numExperimentsKilled =  0
    player.whichExperimentsKilled = []
    for num in player.endingsFound:
        player.endingsFound[num] = p["endings found"][num]
    y = json.dumps(p, indent=4)
    f = open(player.name+".json", "w")
    f.write(y)
    f.close()

createWorld()
playing = True
while playing and player.alive:
    while player.inMainMenu:
            if showMenu():
                playing = False
                commandSuccess = True
    if playing:
        printSituation()
        commandSuccess = False
    timePasses = False
    while not commandSuccess:
        commandSuccess = True
        command = input("What now? ")
        while not command:
            print("Not a valid command")
            command = input("What now? ")
        commandWords = command.split()
        if(commandWords[0].lower() == "go" or commandWords[0].lower() == "enter"):
            if(commandWords[0].lower() == "go"): #both commands are different lengths, adjust accordingly
                destination = command[3:]
            else:
                destination = command[6:]
            foundRoom = False
            for e in player.location.exitNames():
                if(e == destination):
                    if(player.whatsThatDirection(e).locked == False):
                        saveGame()
                        player.goDirection(destination)
                        foundRoom = True
                        timePasses = True
                        if(player.location.ending != "no"): #if room is an ending room
                            player.getEnding(player.location.ending)
                            print()
                            print(player.location.desc)
                            print("Ending found: " + str(player.location.ending))
                            input("Press enter to return to main menu")
                            resetGameSave(player.name)
                            player.inMainMenu = True
                    else:
                        print("The room is locked. Try to find the key, maybe? ")
                        foundRoom = True
                        commandSuccess = False
            if(foundRoom == False):
                print("No such room. ")
                commandSuccess = False
        elif commandWords[0].lower() == "pickup":  #can handle multi-word objects
            targetName = command[7:]
            target = player.location.getItemByName(targetName)
            if(player.location.lit == True):
                if target != False and targetName!="strange boxes":
                    player.pickup(target)
                elif(targetName=="strange boxes"):
                    print("There's too many, you can't do that. ")
                    commandSuccess = False
                else:
                    print("No such item.")
                    commandSuccess = False
            else:
                print('''Go ahead, pick up a random item in a dark room in a mad scientist's \
                evil lab. I'm sure that's perfectly safe.''')
                commandSuccess = False
        elif commandWords[0].lower() == "inventory":
            player.showInventory()
        elif commandWords[0].lower() == "help":
            showHelp()
        elif commandWords[0].lower() == "save":
            saveGame()
        elif commandWords[0].lower() == "main":
            saveGame()
            player.inMainMenu = True
        elif commandWords[0].lower() == "attack":
            if(player.location.lit == True):
                targetName = command[7:]
                target = player.location.getMonsterByName(targetName)
                if target != False:
                    player.attackMonster(target)
                    if(targetName.lower=="big heckin experiment" and player.alive):
                        player.location = findRoom("two",player)
                        player.getEnding(player.location.ending)
                        resetGameSave(player.name)
                        print()
                        print(player.location.desc)
                        print("Ending found: " + str(player.location.ending))
                        input("Press enter to return to main menu")
                        player.inMainMenu = True
                else:
                    print("No such loose experiment here.")
                    commandSuccess = False
            else:
                print("It's too dark to see, much less fight something.")
                commandSuccess = False
        elif(commandWords[0].lower() == "clean"):
            if(player.location.lit == True):
                targetName = command[6:]
                target = player.location.getBodyByName(targetName)
                if(target != False):
                    if(targetName.lower() == "indiana bones"):
                        decision = input("Really? Would you really do that to him? He's not even part of your quota. ")
                        if decision:
                            skelly.cleanUp()
                            bt1f2.changeDesc("You have entered the bathroom on floor 2. It's small and dank and empty.")
                    else:
                        target.cleanUp()
                        player.numBodiesCleaned +=1
                        player.whichBodiesCleaned.append(target.name)
                        print("The body is now gone.")
                else:
                    print("No such mess here.")
                    commandSuccess = False
            else:
                print("It's too dark to see, much less clean something.")
                commandSuccess = False
        elif(commandWords[0].lower() == "eat"):
            targetName = command[4:]
            target = player.getInventoryItemByName(targetName)
            if target != False:
                player.eat(target)
            else:
                print("No such item.")
                commandSuccess = False
        elif(commandWords[0].lower() == "unlock"):
            foundRoom=False
            for e in player.location.exitNames():
                #look through connected rooms
                if(e == command[7:]):
                    wrongKey=False #make sure no redundant/incorrect printed info
                    unlockedRoom=False
                    room = player.whatsThatDirection(e)
                    if(room.locked == True):
                        print()
                        if(player.getInventoryItemByName(room.key)!=False):
                                room.unlock()
                                unlockedRoom=True
                                foundRoom=True
                                print("The room is now unlocked.")
                                print()
                                input("Press enter to continue...")
                        else:
                            print("You don't have that key yet.")
                            commandSuccess = False
                            wrongKey=True
                            foundRoom=True
                    else:
                        print("It's already unlocked.")
                        commandSuccess = False
                        foundRoom=True
            if not foundRoom:
                print("No such room here.")
                commandSuccess = False
        elif(commandWords[0].lower() == "inspect"):
            targetName = command[8:] #so many targets cuz ofdifferent things to inspect
            itemTarget = player.getInventoryItemByName(targetName)
            itemTarget2 = player.location.getItemByName(targetName)
            bodyTarget = player.location.getBodyByName(targetName)
            monsterTarget = player.location.getMonsterByName(targetName)
            if(targetName.lower() == "strange boxes"):
                player.inspectedBoxes +=1
                if(player.inspectedBoxes == 1):
                    print("A crumbling pile of cardboard boxes. They're all empty but look specifically stacked. You can see something dark behind them...")
                    print()
                    input("Press enter to continue...")
                elif(player.inspectedBoxes == 2):
                    Room.connectRooms(player.location, "closet", findRoom("clstf3",player), "back")
                    print("Aha! An old closet was hidden behind the boxes.")
                    print()
                    input("Press enter to continue...")
                elif(player.inspectedBoxes > 2):
                    print("You can enter the closet now.")
                    print()
                    input("Press enter to continue...")
            elif(itemTarget != False):
                print(itemTarget.desc)
                print()
                input("Press enter to continue...")
            elif(itemTarget2 != False):
                print(itemTarget2.desc)
                print()
                input("Press enter to continue...")
            elif(bodyTarget != False):
                print(bodyTarget2.desc)
                print()
                input("Press enter to continue...")
            elif(monsterTarget != False):
                print(monsterTarget2.desc)
                print()
                input("Press enter to continue...")
            else:
                print("No such thing here.")
                commandSuccess = False
        elif(commandWords[0].lower() == "combine"):
            item1 = input("Which first item? ")
            item2 = input("With which item? ")
            if not player.combineInventoryItems(item1,item2):
                print("Those don't go together")
                commandSuccess = False
            else:
                illuminateAllRooms()
                print("Congrats, you'll be able to see in dark rooms now. ")
                input("Press enter to continue...")
        elif(commandWords[0].lower() == "talk"):
            if(commandWords[1].lower() == "boss" or commandWords[1].lower() == "dr" or commandWords[1].lower() == "dr." or commandWords[1].lower() == "doctor" or commandWords[2].lower() == "boss" or commandWords[2].lower() == "dr" or commandWords[2].lower() == "dr." or commandWords[2].lower() == "doctor"):
                    if findItem("boss").startConvo(): #did player press button?
                        print()
                        print('''You press the button. Dr. E. Vil. Scientist cackles maniacally as France is permanently deleted, then vaguely
                        gestures to the exit door in the corner. Your job is done, you're free to leave now.''')
                        input("Press enter to continue...")
                        if(player.numExperimentsKilled==5):
                            if(player.numBodiesCleaned==8):
                                player.location = findRoom("eight",player)
                                player.getEnding(player.location.ending)
                                resetGameSave(player.name)
                                print()
                                print(player.location.desc)
                                print("Ending found: " + str(player.location.ending))
                                input("Press enter to return to main menu")
                                player.inMainMenu = True
                            else:
                                player.location = findRoom("seven",player)
                                player.getEnding(player.location.ending)
                                resetGameSave(player.name)
                                print()
                                print(player.location.desc)
                                print("Ending found: " + str(player.location.ending))
                                input("Press enter to return to main menu")
                                player.inMainMenu = True
                        else:
                            if(player.numBodiesCleaned==8):
                                player.location = findRoom("ten",player)
                                player.getEnding(player.location.ending)
                                resetGameSave(player.name)
                                print()
                                print(player.location.desc)
                                print("Ending found: " + str(player.location.ending))
                                input("Press enter to return to main menu")
                                player.inMainMenu = True
                            else:
                                player.location = findRoom("nine",player)
                                player.getEnding(player.location.ending)
                                resetGameSave(player.name)
                                print()
                                print(player.location.desc)
                                print("Ending found: " + str(player.location.ending))
                                input("Press enter to return to main menu")
                                player.inMainMenu = True
                    else:
                        print()
                        print('''You refuse to press the button. Your boss yells at you as you exit, passing a secret agent
                        SWAT team on your way out. You're definitely fired but at least you didn't blow up a country.''')
                        input("Press enter to continue...")
                        if(player.numExperimentsKilled==5):
                            if(player.numBodiesCleaned==8):
                                player.location = findRoom("four",player)
                                player.getEnding(player.location.ending)
                                resetGameSave(player.name)
                                print()
                                print(player.location.desc)
                                print("Ending found: " + str(player.location.ending))
                                input("Press enter to return to main menu")
                                player.inMainMenu = True
                            else:
                                player.location = findRoom("three",player)
                                player.getEnding(player.location.ending)
                                resetGameSave(player.name)
                                print()
                                print(player.location.desc)
                                print("Ending found: " + str(player.location.ending))
                                input("Press enter to return to main menu")
                                player.inMainMenu = True
                        else:
                            if(player.numBodiesCleaned==8):
                                player.location = findRoom("six",player)
                                player.getEnding(player.location.ending)
                                resetGameSave(player.name)
                                print()
                                print(player.location.desc)
                                print("Ending found: " + str(player.location.ending))
                                input("Press enter to return to main menu")
                                player.inMainMenu = True
                            else:
                                player.location = findRoom("five",player)
                                player.getEnding(player.location.ending)
                                resetGameSave(player.name)
                                print()
                                print(player.location.desc)
                                print("Ending found: " + str(player.location.ending))
                                input("Press enter to return to main menu")
                                player.inMainMenu = True
            else:
                print("No one like that here. ")
                commandSuccess = False
        elif(commandWords[0].lower() == "me"):
            player.stats()
        else:
            print("Not a valid command")
            commandSuccess = False
    if timePasses == True:
        updater.updateAll()
