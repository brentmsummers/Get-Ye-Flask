#This is take on the game on Homestarrunner.com. The link to the flash version is here: http://homestarrunner.com/dungeonman.html

import csv
import random
import arcade
import os
import subprocess

startingText = "THY DUNGEONMAN\n\nYOU ARE THY DUNGEONMAN!\n\nFor help type HELP, to view inventory type INVENTORY\n\nYe find yeself in yon dungeon. Ye see a SCROLL. Behind ye SCROLL is a FLASK.\nObvious exits are NORTH, SOUTH, and DENNIS.\n\n\n"
whatToDo = "What wouldst thou deau?"
choiceList = ['get ye scroll','Get Ye Scroll','GET YE SCROLL','Scroll','SCROLL','NOT DENNIS','Not Dennis','not dennis','help','HELP','Help','trinket','Trinket','TRINKET','inventory','Inventory',' END GAME ','End Game', 'end game','END GAME', 'End game','rope','ROPE','Get Ye Flask','Get ye flask','get ye flask','Get Ye flask','Get ye Flask','get Ye Flask','get ye Flask','get Ye flask','NORTH','SOUTH','DENNIS','SCROLL','FLASK','north','south','dennis','scroll','flask','rope','ROPE']
fCondition1 = False
fCondition2 = False
nCondition1 = False
nCondition2 = False
sCondition1 = False
dCondition1 = False
inventory = []
currentRoom = ''
    


def unacceptableChoice(choiceMade):
    #print("This is not a valid input, please try again")
    if choiceMade == "end game" or choiceMade == "End Game" or choiceMade == "END GAME":
        choiceMade = "end game"
        return choiceMade
    if choiceMade == '':
        print("Please actually write something")
        choiceMade = input()
        unacceptableChoice(choiceMade)
        return choiceMade
    elif choiceMade not in choiceList:
        print("That does not computether. Type HELP is thou needs of it")
        choiceMade = input()
        unacceptableChoice(choiceMade)
        return choiceMade
    elif choiceMade in choiceList:
        #choiceMade = input()
        makeAChoice(choiceMade)
        return choiceMade
        

def resetChoice(choiceMade):
    choiceMade = ''
    makeAChoice(choiceMade)

def goNorth(choiceMade):
    clearScreen()
    global nCondition1
    nCondition1 = True
    print("You go NORTH through yon corridor. You arrive at parapets. Ye see a ROPE. Obvious exits are SOUTH.\n")
    choiceMade = ''
    return choiceMade

def goSouth(choiceMade):
    clearScreen()
    global sCondition1
    sCondition1 = True
    print("You head south to an embankment. Or maybe a chasm. You can't decide which.\nAnyway, ye spies a TRINKET. Obvious exits are NORTH.\n")
    choiceMade = ''
    return choiceMade

def dennis(choiceMade):
    clearScreen()
    global dCondition1
    dCondition1 = True
    print("Ye arrive at Dennis. He wears a sporty frock coat and a long jimberjam. He paces about nervously.\nObvious exits are NOT DENNIS.\n")
    choiceMade = ''
    return choiceMade

def notDennis(choiceMade):
    clearScreen()
    print("You go NOT DENNIS.\nYe find yeself in yon dungeron. Ye see a SCROLL. Behind ye SCROLL is a FLASK.\nObvious exits are NORTH, SOUTH, and DENNIS.\n")
    choiceMade = ''
    return choiceMade

def getYeFlask(choiceMade):
    clearScreen()
    global fCondition1
    print("You cannot get the FLASK. It is firmly bolted to a wall which is bolted to the rest of the dungeon which is probably bolted to a castle. Never you mind.\n")
    fCondition1 = True
    choiceMade = ''
    return choiceMade

def getYeScroll(choiceMade):
    clearScreen()
    print("Ye takes the SCROLL and reads of it. It doth say:\n\nBEWARE, READER OF YE SCROLL,\nDANGER AWAIT TO THE -\n\nThe SCROLL dissapears in they hands with ye olde ZAP!\n\nWhat wouldst thou deau?")
    choiceMade = ''
    return choiceMade

def getYeRopeDeath(choiceMade):
    clearScreen()
    print("You attempt to take ye ROPE but alas it is enchanted! It glows a mustard red and smells like a public privy. The ROPE wraps round your neck and hangs you from the parapets. With your last breath, you wonder what parapets are.\n\nGAME OVER\n\n")
    choiceMade = 'End Game'
    return choiceMade

def inventoryShow(choiceMade):
    if len(inventory) < 1:
        print("\n\nYour inventory is currently empty!")
        choiceMade = userInput(choiceMade)
        makeAChoice(choiceMade)
    elif len(inventory) == 1:
        print("\n\nYour inventory consists of the following item:")
        print('\n'.join(inventory)+"\n\n")
        choiceMade = userInput(choiceMade)
        makeAChoice(choiceMade)
    elif len(inventory) > 1:
        print("\n\nYour inventory consists of the following items:")
        print('\n'.join(inventory)+"\n\n")
        choiceMade = userInput(choiceMade)
        makeAChoice(choiceMade)
            

def userInput(choiceMade):
    print("What wouldst thou deau?")
    choiceMade = input()
    return choiceMade

def clearScreen():
    print("\n"*40)


def makeAChoice(choiceMade):
    if choiceMade == '':
        while choiceMade == '':
            choiceMade = userInput(choiceMade)
            makeAChoice(choiceMade)
            if choiceMade == "End Game" or choiceMade == "end game" or choiceMade == "End game" or choiceMade == "END GAME":
                break
            
    while choiceMade != "End Game" or choiceMade != 'end game':
        if choiceMade not in choiceList:
            choiceMade = (unacceptableChoice(choiceMade))
        elif choiceMade == 'Get ye flask' or choiceMade == 'get ye flask' or choiceMade == "flask" or choiceMade == "Flask":
            getYeFlask(choiceMade)
            choiceMade = userInput(choiceMade)
            makeAChoice(choiceMade)
            break
        elif choiceMade == 'Get ye scroll' or choiceMade == 'Get Ye Scroll' or choiceMade == 'get ye scroll' or choiceMade == 'GET YE SCROLL' or choiceMade == 'scroll' or choiceMade == 'SCROLL' or choiceMade == 'Scroll':
            getYeScroll(choiceMade)
            choiceMade = userInput(choiceMade)
            makeAChoice(choiceMade)
        elif choiceMade == 'NORTH' or choiceMade == 'north':
            goNorth(choiceMade)
            choiceMade = userInput(choiceMade)
            makeAChoice(choiceMade)
            break
        elif choiceMade == 'SOUTH' or choiceMade == 'south':
            goSouth(choiceMade)
            choiceMade = userInput(choiceMade)
            makeAChoice(choiceMade)
            break
        elif choiceMade == 'dennis' or choiceMade == 'DENNIS' or choiceMade == 'Dennis':
            dennis(choiceMade)
            choiceMade = userInput(choiceMade)
            makeAChoice(choiceMade)
            break
        elif choiceMade == 'not dennis' or choiceMade == 'NOT DENNIS' or choiceMade == 'Not Dennis':
            if dCondition1 == False:
                print("There is no NOT DENNIS here, please try again")
                choiceMade = userInput(choiceMade)
                makeAChoice(choiceMade)
            notDennis(choiceMade)
            choiceMade = userInput(choiceMade)
            makeAChoice(choiceMade)
            break
        elif choiceMade == 'TRINKET' or choiceMade == 'trinket' or choiceMade == 'Trinket':
            i = "TRINKET"
            if sCondition1 == True:
                if i in inventory:
                    print("Ye getsts yon TRINKET and discover it to be a bauble. You rejoice at your good fortune. \nYou shove the TRINKET in your pouchel. It kinda hurts.\n")
                    choiceMade = userInput(choiceMade)
                    makeAChoice(choiceMade)                    
                inventory.append("TRINKET")
                print("Ye getsts yon TRINKET and discover it to be a bauble. You rejoice at your good fortune. \nYou shove the TRINKET in your pouchel. It kinda hurts.\n")
                choiceMade = userInput(choiceMade)
                makeAChoice(choiceMade)
                break
            else:
                print("There is no TRINKET here, please try again.\n")
                choiceMade = userInput(choiceMade)
                makeAChoice(choiceMade)
                break
            
        elif choiceMade == 'ROPE' or choiceMade == 'rope' or choiceMade == 'Rope':
            if nCondition1 == False:
                print("There is no Rope here, please try again\n")
                choiceMade = userInput(choiceMade)
                choiceMade = 'Exit Game'
                makeAChoice(choiceMade)
                break
                
            elif nCondition1 == True:
                getYeRopeDeath(choiceMade)
                break
            
        elif choiceMade == "inventory" or choiceMade == "Inventory":
            inventoryShow(choiceMade)
            break
        
        elif choiceMade == "Help" or choiceMade == "help" or choiceMade == "HELP":
            print("This is a list of acceptable options for the entire game:")
            print('\n'.join(choiceList))
            choiceMade = userInput(choiceMade)
            makeAChoice(choiceMade)
            break
        
        elif choiceMade == "End Game" or choiceMade == "end game" or choiceMade == "End game" or choiceMade == "END GAME":
            break

def startGame():
    global fCondition1
    global fCondition2
    global nCondition1
    global nCondition2
    global sCondition1
    global dCondition1
    fCondition1 = False
    fCondition2 = False
    nCondition1 = False
    nCondition2 = False
    sCondition1 = False
    dCondition1 = False
    print(startingText)
    print(whatToDo)
    playAgain = 'Y'
    while playAgain == 'Y':
        inventory.clear()  
        choiceMade = input()
        makeAChoice(choiceMade)
        print("Play again? [Y/N]")
        playAgain = input()
        if playAgain == 'Y' or playAgain == 'y' or playAgain == 'yes' or playAgain == 'Yes':
            startGame()
        else:
            break


startGame()


