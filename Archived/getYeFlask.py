#This is take on the game on Homestarrunner.com. The link to the flash version is here: http://homestarrunner.com/dungeonman.html

import csv
import random
import arcade
import os
import subprocess

starting_text = "THY DUNGEONMAN\n\nYOU ARE THY DUNGEONMAN!\n\nFor help type HELP, to view inventory type INVENTORY\n\nYe find yeself in yon dungeon. Ye see a SCROLL. Behind ye SCROLL is a FLASK.\nObvious exits are NORTH, SOUTH, and DENNIS.\n\n\n"
what_to_do = "What wouldst thou deau?"
choiceList = ['get ye trinket', 'get trinket','give trinket to dennis','get ye scroll','Get Ye Scroll','GET YE SCROLL','Scroll','SCROLL','NOT DENNIS','Not Dennis','not dennis','help','HELP','Help','trinket','Trinket','TRINKET','inventory','Inventory',' END GAME ','End Game', 'end game','END GAME', 'End game','rope','ROPE','Get Ye Flask','Get ye flask','get ye flask','Get Ye flask','Get ye Flask','get Ye Flask','get ye Flask','get Ye flask','NORTH','SOUTH','DENNIS','SCROLL','FLASK','north','south','dennis','scroll','flask','rope','ROPE']
f_condition_1 = False
f_condition_2 = False
n_condition_1 = False
n_condition_2 = False
s_condition_1 = False
d_condition_1 = False
inventory = []
current_room = ''
current_score = 0
    


def unacceptableChoice(choice_made):
    #print("This is not a valid input, please try again")
    if choice_made == "end game" or choice_made == "End Game" or choice_made == "END GAME":
        choice_made = "end game"
        return choice_made
    if choice_made == '':
        print("Please actually write something")
        choice_made = input()
        choice_made = choice_made.casefold()
        unacceptableChoice(choice_made)
        return choice_made
    elif choice_made not in choiceList:
        print("That does not computether. Type HELP is thou needs of it")
        choice_made = input()
        choice_made = choice_made.casefold()
        unacceptableChoice(choice_made)
        return choice_made
    elif choice_made in choiceList:
        choice_made = input()
        choice_made = choice_made.casefold()
        make_a_choice(choice_made)
        return choice_made
        

def reset_Choice(choice_made):
    choice_made = ''
    make_a_choice(choice_made)

def go_north(choice_made):
    clear_Screen()
    global n_condition_1
    n_condition_1 = True
    print("You go NORTH through yon corridor. You arrive at parapets. Ye see a ROPE. Obvious exits are SOUTH.\n")
    choice_made = ''
    return choice_made

def go_south(choice_made):
    clear_Screen()
    global s_condition_1
    s_condition_1 = True
    print("You head south to an embankment. Or maybe a chasm. You can't decide which.\nAnyway, ye spies a TRINKET. Obvious exits are NORTH.\n")
    choice_made = ''
    return choice_made

def dennis(choice_made):
    clear_Screen()
    global d_condition_1
    d_condition_1 = True
    print("Ye arrive at Dennis. He wears a sporty frock coat and a long jimberjam. He paces about nervously.\nObvious exits are NOT DENNIS.\n")
    choice_made = ''
    return choice_made

def not_dennis(choice_made):
    clear_Screen()
    print("You go NOT DENNIS.\nYe find yeself in yon dungeron. Ye see a SCROLL. Behind ye SCROLL is a FLASK.\nObvious exits are NORTH, SOUTH, and DENNIS.\n")
    choice_made = ''
    return choice_made

def get_ye_flask(choice_made):
    clear_Screen()
    global f_condition_1
    print("You cannot get the FLASK. It is firmly bolted to a wall which is bolted to the rest of the dungeon which is probably bolted to a castle. Never you mind.\n")
    f_condition_1 = True
    choice_made = ''
    return choice_made

def get_ye_scroll(choice_made):
    clear_Screen()
    print("Ye takes the SCROLL and reads of it. It doth say:\n\nBEWARE, READER OF YE SCROLL,\nDANGER AWAIT TO THE -\n\nThe SCROLL dissapears in they hands with ye olde ZAP!\n\n")
    compute_score()
    choice_made = ''
    return choice_made

def get_ye_rope(choice_made):
    clear_Screen()
    print("You attempt to take ye ROPE but alas it is enchanted! It glows a mustard red and smells like a public privy. The ROPE wraps round your neck and hangs you from the parapets. With your last breath, you wonder what parapets are.\n\nGAME OVER\n\n")
    choice_made = 'End Game'
    compute_score_neg()
    return choice_made


def get_ye_trinket(choice_made,i):
    if i in inventory:
        print("Ye getsts yon TRINKET and discover it to be a bauble. You rejoice at your good fortune. \nYou shove the TRINKET in your pouchel. It kinda hurts.\n")
        choice_made = user_input(choice_made)
        make_a_choice(choice_made)                    
    inventory.append("TRINKET")
    print("Ye getsts yon TRINKET and discover it to be a bauble. You rejoice at your good fortune. \nYou shove the TRINKET in your pouchel. It kinda hurts.\n")
    compute_score()
    choice_made = user_input(choice_made)
    make_a_choice(choice_made)

def give_dennis_trinket(choice_made):
    clear_Screen()
    if len(inventory) > 0:
        print("A novel idea! You givst the TRINKET to Dennis and he happily agrees to tell you what parapets are. With this new knowledge, ye escapes from yon dungeon in order to search for the new dungeons and to remain...")
        print("THY DUNGEONMAN!!\n")
        inventory.remove("TRINKET")
        ye_have_won(choice_made)
        
def compute_score():
    global current_score
    current_score += 1
    return current_score

def compute_score_neg():
    global current_score
    current_score -= 1
    return current_score

def display_score(choice_made):
    print("Your score was:" + str(current_score))
    choice_made = 'end game'
    return choice_made

def ye_have_won(choice_made):
    print("You hath won! Congraturation!")
    display_score(choice_made)
    return choice_made
    

def inventory_show(choice_made):
    if len(inventory) < 1:
        print("\n\nYour inventory is currently empty!")
        choice_made = user_input(choice_made)
        make_a_choice(choice_made)
    elif len(inventory) == 1:
        print("\n\nYour inventory consists of the following item:")
        print('\n'.join(inventory)+"\n\n")
        choice_made = user_input(choice_made)
        make_a_choice(choice_made)
    elif len(inventory) > 1:
        print("\n\nYour inventory consists of the following items:")
        print('\n'.join(inventory)+"\n\n")
        choice_made = user_input(choice_made)
        make_a_choice(choice_made)
            

def user_input(choice_made):
    print("What wouldst thou deau?")
    choice_made = input()
    choice_made = choice_made.casefold()
    return choice_made 

def clear_Screen():
    print("\n"*40)


def make_a_choice(choice_made):
    if choice_made == '':
        while choice_made == '':
            choice_made = user_input(choice_made)
            make_a_choice(choice_made)
            if choice_made == "end game":
                display_score()
                break
            
    while choice_made != "end game":
        if choice_made not in choiceList:
            choice_made = (unacceptableChoice(choice_made))
        elif choice_made == 'get ye flask' or choice_made == "flask" or choice_made == "get flask":
            get_ye_flask(choice_made)
            choice_made = user_input(choice_made)
            make_a_choice(choice_made)
            break
        elif choice_made == 'get ye scroll' or choice_made == 'scroll' or choice_made == 'get scroll':
            get_ye_scroll(choice_made)
            choice_made = user_input(choice_made)
            make_a_choice(choice_made)
        elif choice_made == 'north':
            go_north(choice_made)
            choice_made = user_input(choice_made)
            make_a_choice(choice_made)
            break
        elif choice_made == 'south':
            go_south(choice_made)
            choice_made = user_input(choice_made)
            make_a_choice(choice_made)
            break
        elif choice_made == 'dennis':
            dennis(choice_made)
            choice_made = user_input(choice_made)
            make_a_choice(choice_made)
            break
        elif choice_made == 'not dennis':
            if d_condition_1 == False:
                print("There is no NOT DENNIS here, please try again")
                choice_made = user_input(choice_made)
                make_a_choice(choice_made)
            not_dennis(choice_made)
            choice_made = user_input(choice_made)
            make_a_choice(choice_made)
            break

        elif choice_made == 'trinket' or choice_made == 'get ye trinket' or choice_made == 'get trinket':
            i = "TRINKET"
            if s_condition_1 == True:
                get_ye_trinket(choice_made,i)
                break
            else:
                print("There is no TRINKET here, please try again.\n")
                choice_made = user_input(choice_made)
                make_a_choice(choice_made)
                break
            
        elif choice_made == 'rope':
            if n_condition_1 == False:
                print("There is no Rope here, please try again\n")
                choice_made = user_input(choice_made)
                choice_made = 'Exit Game'
                make_a_choice(choice_made)
                break
                
            elif n_condition_1 == True:
                get_ye_rope(choice_made)
                break
            
        elif choice_made == "inventory":
            inventory_show(choice_made)
            break
        elif choice_made == "give trinket to dennis":
            give_dennis_trinket(choice_made)
            break
        
        elif choice_made == help_text:
            print("This is a list of acceptable options for the entire game:")
            print('\n'.join(choiceList))
            choice_made = user_input(choice_made)
            make_a_choice(choice_made)
            break
        
        
        elif choice_made == endGame:
            display_score()
            break
end_game_text = 'End Game'
help_text = 'Help'
inventory_text = 'Inventory'
rope_text = 'Rope'
trinket_text = 'Trinket'
dennis_text = 'Dennis'
not_dennis_text = 'Not Dennis'
south_text = 'South'
north_text = 'North'
get_scroll_text = 'Get ye scroll'
get_flask_text = 'Get ye flask'


def start_game():
    global f_condition_1
    global f_condition_2
    global n_condition_1
    global n_condition_2
    global s_condition_1
    global d_condition_1
    f_condition_1 = False
    f_condition_2 = False
    n_condition_1 = False
    n_condition_2 = False
    s_condition_1 = False
    d_condition_1 = False
    print(starting_text)
    print(what_to_do)
    d_condition = 'Y'
    while d_condition == 'Y':
        inventory.clear()  
        choice_made = input()
        choice_made = choice_made.casefold()
        make_a_choice(choice_made)
        print("Play again? [Y/N]")
        d_condition = input()
        d_condition = d_condition.casefold()
        if d_condition == 'Y' or d_condition == 'y' or d_condition == 'yes' or d_condition == 'Yes':
            start_game()
        else:
            break


start_game()


