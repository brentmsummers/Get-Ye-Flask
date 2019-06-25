#This is take on the game on Homestarrunner.com. The link to the flash version is here: http://homestarrunner.com/dungeonman.html

import os
import gettext

_ = gettext.gettext


f_condition_1 = False
f_condition_2 = False
n_condition_1 = False
n_condition_2 = False
s_condition_1 = False
d_condition_1 = False
a_condition_1 = False

#inventory will be used throughout the game
inventory = []
#The following list has all of the acceptable commands a user can input in the game. Every input is checked against this list and if it's not found the user is informed and reinputs the command
choice_list = ["room","which room","display room","north","south","dennis","scroll","flask","get ye trinket","give trinket to dennis","get ye scroll","scroll","not dennis","help","trinket","inventory","end game","rope","get ye flask","dungeon"]
#This is a global variable that tracks and displays where the customer is. It is used so you can only interact with objects in the same room as you
current_room = ''
#Score is calculated in several different instances throughout the game and displayed when the game comes to an end
current_score = 0
    

#This takes the user in put and compares it agains the list of acceptable words; if it's not in that list it will ask for a new input.
def unacceptableChoice(choice_made):
    if choice_made == _("end game"):
        choice_made = _("end game")
        return choice_made
    if choice_made == '':
        print(_("Please actually writeth somethingith"))
        choice_made = input()
        choice_made = choice_made.casefold()
        unacceptableChoice(choice_made)
        return choice_made
    elif choice_made not in choice_list:
        print(_("That does not computether. Type HELP is thou needs of it"))
        choice_made = input()
        choice_made = choice_made.casefold()
        unacceptableChoice(choice_made)
        return choice_made
    elif choice_made in choice_list:
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
    print(_("You go NORTH through yon corridor."))
    print(_("You arrive at parapets."))
    print(_("Ye see a ROPE."))
    print(_("Obvious exits are SOUTH and DUNGEON"))
    choice_made = ''
    return choice_made

def go_dungeon(choice_made):
    clear_Screen()
    if a_condition_1 == True:
        print(_("Ye find yeself in yon dungeon. Ye see a FLASK.\nObvious exits are NORTH, SOUTH, and DENNIS.\n\n\n"))
        choice_made = ''
        return choice_made
    else:
        print(_("Ye find yeself in yon dungeon. Ye see a SCROLL. Behind ye SCROLL is a FLASK.\nObvious exits are NORTH, SOUTH, and DENNIS.\n\n\n"))
        choice_made = ''
        return choice_made

def go_south(choice_made):
    clear_Screen()
    global s_condition_1
    s_condition_1 = True
    print(_("You head south to an embankment, or maybe a chasm."))
    print(_("You can't decide which."))
    print(_("Anyway, ye spies a TRINKET. Obvious exits are DUNGEON"))
    choice_made = ''
    return choice_made

def dennis(choice_made):
    clear_Screen()
    global d_condition_1
    d_condition_1 = True
    print(_("Ye arrive at Dennis."))
    print(_("He wears a sporty frock coat and a long jimberjam."))
    print(_("He paces about nervously."))
    print(_("Obvious exits are NOT DENNIS."))
    choice_made = ''
    return choice_made

def not_dennis(choice_made):
    clear_Screen()
    print(_("Ye arrive at Dennis."))
    print(_("He wears a sporty frock coat and a long jimberjam."))
    print(_("He paces about nervously."))
    print(_("Obvious exits are NOT DENNIS."))
    choice_made = ''
    return choice_made

def get_ye_flask(choice_made):
    clear_Screen()
    global f_condition_1
    print(_("You cannot get the FLASK."))
    print(_("It is firmly bolted to a wall which is bolted to the rest of the dungeon which is probably bolted to a castle."))
    print(_("Never you mind."))
    f_condition_1 = True
    choice_made = ''
    return choice_made

def get_ye_scroll(choice_made):
    clear_Screen()
    global a_condition_1
    if a_condition_1 == False:
        print(_("Ye takes the SCROLL and reads of it."))
        print(_("It doth say:"))
        print("\n\n")
        print(_("BEWARE, READER OF YE SCROLL,"))
        print(_("DANGER AWAIT TO THE -"))
        print("\n\n")
        print(_("The SCROLL dissapears in they hands with ye olde ZAP!"))
        compute_score()
        a_condition_1 = True
        choice_made = ''
        return choice_made
    else:
        print(_("Ye cannot take yon scroll as it dissapeard with ye olde ZAP!"))
        choice_made = ''
        return choice_made

def get_ye_rope(choice_made):
    clear_Screen()
    print(_("You attempt to take ye ROPE but alas it is enchanted!"))
    print(_("It glows a mustard red and smells like a public privy."))
    print(_("The ROPE wraps round your neck and hangs you from the parapets."))
    print(_("With your last breath, you wonder what parapets are."))
    ye_have_lost(choice_made)    
    choice_made = _("end game")
    compute_score_neg()
    return choice_made


def get_ye_trinket(choice_made,i):
    if i in inventory:
        clear_Screen()
        print(_("Ye hast already goteth yon trinket"))
        print(_("Obvious exits are DUNGEON"))
        choice_made = user_input(choice_made)
        make_a_choice(choice_made)                    
    else:
        inventory.append(_("trinket"))
        clear_Screen()
        print(_("Item added to inventory"))
        print(_("Ye getsts yon TRINKET and discover it to be a bauble."))
        print(_("You rejoice at your good fortune."))
        print(_("You shove the TRINKET in your pouchel."))
        print(_("It kinda hurts."))
        compute_score()
        print(_("Obvious exits are DUNGEON"))
        choice_made = user_input(choice_made)
        make_a_choice(choice_made)

def give_dennis_trinket(choice_made):
    clear_Screen()
    if len(inventory) > 0:
        print(_("A novel idea! You givst the TRINKET to Dennis and he happily agrees to tell you what parapets are."))
        print(_("With this new knowledge, ye escapes from yon dungeon in order to search for the new dungeons and to remain..."))
        print(_("THY DUNGEONMAN!!"))
        inventory.remove(_("trinket"))
        print(_("Item removed from inventory"))
        ye_have_won(choice_made)
    else:
        print(_("Ye doth not hath a TRINKET to given to DENNIS"))
        choice_made = user_input(choice_made)
        make_a_choice(choice_made)
        
def compute_score():
    global current_score
    current_score += 2
    return current_score

def compute_score_neg():
    global current_score
    current_score -= 1
    return current_score

def display_score(choice_made):
    print(_("Your score is:") + str(current_score))
    choice_made = _("end game")
    return choice_made

def ye_have_won(choice_made):
    print(_("You hath won! Congraturation!"))
    display_score(choice_made)
    return choice_made

def ye_have_lost(choice_made):
    print("\n\n" + _("GAME OVER") + "\n\n")
    display_score(choice_made)
    return choice_made
    

def inventory_show(choice_made):
    if len(inventory) < 1:
        print("\n\n" + _("Your inventory is currently empty!") + "\n")
        choice_made = user_input(choice_made)
        make_a_choice(choice_made)
    elif len(inventory) == 1:
        print("\n\n" + _("Your inventory consists of the following item:") + "\n")
        print('\n'.join(inventory)+"\n\n")
        choice_made = user_input(choice_made)
        make_a_choice(choice_made)
    elif len(inventory) > 1:
        print("\n\n" + _("Your inventory consists of the following items:") + "\n")
        print('\n'.join(inventory)+"\n\n")
        choice_made = user_input(choice_made)
        make_a_choice(choice_made)
            

def user_input(choice_made):
    print("\n" + _("What wouldst thou deau?"))
    choice_made = input()
    choice_made = choice_made.casefold()
    print("\n")
    return choice_made 

def print_current_room(choice_made):
    print("\n")
    print("You are current in the " + current_room + " room.")
    choice_made = user_input(choice_made)
    return choice_made

def clear_Screen():
    print("\n"*50)


def make_a_choice(choice_made):
    if choice_made == '':
        while choice_made == '':
            choice_made = user_input(choice_made)
            make_a_choice(choice_made)
            if choice_made == _("end game"):
                display_score()
                break
            
    while choice_made != _("end game"):
        if choice_made not in choice_list:
            choice_made = (unacceptableChoice(choice_made))
            break
            
        elif choice_made == _("get ye flask") or choice_made == _("get flask") or choice_made == _("flask"):
            
            if f_condition_2 == False:
                get_ye_flask(choice_made)
                f_condition_2 == True    
                global current_score
                current_score += 1
                choice_made = user_input(choice_made)
                make_a_choice(choice_made)
                break
            else:
                get_ye_flask(choice_made)
                choice_made = user_input(choice_made)
                make_a_choice(choice_made)
                break
        
        elif choice_made == _("get ye scroll") or choice_made == _("scroll") or choice_made == _("get scrolll"):
            get_ye_scroll(choice_made)
            print(dungeon_text_no_scroll)
            choice_made = user_input(choice_made)
            make_a_choice(choice_made)
            break
            
        elif choice_made == _("north"):
            #global current_room
            #current_room = 'north'
            go_north(choice_made)
            choice_made = user_input(choice_made)
            make_a_choice(choice_made)
            break
        
        elif choice_made == _("south"):
            #global current_room
            #current_room = 'south'
            go_south(choice_made)
            choice_made = user_input(choice_made)
            make_a_choice(choice_made)
            break

        elif choice_made == _("dungeon"):
            #global current_room
            #current_room = 'dungeon'
            go_dungeon(choice_made)
            choice_made = user_input(choice_made)
            make_a_choice(choice_made)
            break
        
        elif choice_made == _("dennis"):
            #global current_room
            #current_room = 'dennis'
            dennis(choice_made)
            choice_made = user_input(choice_made)
            make_a_choice(choice_made)
            break
        
        elif choice_made == _("not dennis"):
            if d_condition_1 == False:
                print(_("There is no NOT DENNIS here, please try again"))
                choice_made = user_input(choice_made)
                make_a_choice(choice_made)
            not_dennis(choice_made)
            choice_made = user_input(choice_made)
            make_a_choice(choice_made)
            break

        elif choice_made == _("trinket") or choice_made == _("get ye trinket") or choice_made == _("get trinket"):
            i = trinket_text
            if s_condition_1 == True:
                get_ye_trinket(choice_made,i)
                break
            else:
                print(_("There is no TRINKET here, please try again."))
                choice_made = user_input(choice_made)
                make_a_choice(choice_made)
                break
            
        elif choice_made == _("rope"):
            if n_condition_1 == False:
                print(_("There is no Rope here, please try again"))
                choice_made = user_input(choice_made)
                choice_made = _("end game")
                make_a_choice(choice_made)
                break
                
            elif n_condition_1 == True:
                get_ye_rope(choice_made)
                break
            
        elif choice_made == _("inventory"):
            inventory_show(choice_made)
            break
        
        elif choice_made == _("room") or choice_made == _("which room") or choice_made == _("display room"):
            print_current_room(choice_made)
            make_a_choice(choice_made)
            break
        
        elif choice_made == _("give trinket to dennis"):
            give_dennis_trinket(choice_made)
            break
        
        elif choice_made == _("help"):
            print(_("This is a list of acceptable options for the entire game:"))
            print('\n'.join(choice_list))
            choice_made = user_input(choice_made)
            make_a_choice(choice_made)
            break
        
        
        elif choice_made == _("end game"):
            display_score()
            break

def start_game():
    global f_condition_1
    global f_condition_2
    global n_condition_1
    global n_condition_2
    global s_condition_1
    global d_condition_1
    global a_condition_1
    f_condition_1 = False
    f_condition_2 = False
    n_condition_1 = False
    n_condition_2 = False
    s_condition_1 = False
    d_condition_1 = False
    a_condition_1 = False
    print(_("THY DUNGEONMAN\n\nYOU ARE THY DUNGEONMAN!\n\nFor help type HELP, to view inventory type INVENTORY\n"))
    print(_("Ye find yeself in yon dungeon. Ye see a SCROLL. Behind ye SCROLL is a FLASK.\nObvious exits are NORTH, SOUTH, and DENNIS.\n\n\n"))
    print(_("What wouldst thou deau?"))
    d_condition = _("y")
    while d_condition == _("y"):
        inventory.clear()
        choice_made = input()
        choice_made = choice_made.casefold()
        make_a_choice(choice_made)
        print(_("Play again? [Y/N]"))
        d_condition = input()
        d_condition = d_condition.casefold()
        if d_condition == _("y") or d_condition == _("yes"):
            clear_Screen()
            start_game()
        else:
            break


clear_Screen()
start_game()


