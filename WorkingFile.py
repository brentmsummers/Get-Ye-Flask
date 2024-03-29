#This is take on the game on Homestarrunner.com. The link to the flash version is here: http://homestarrunner.com/dungeonman.html

import os
import gettext

_ = gettext.gettext

starting_text = _("THY DUNGEONMAN\n\nYOU ARE THY DUNGEONMAN!\n\nFor help type HELP, to view inventory type INVENTORY\n")
dungeon_text = _("Ye find yeself in yon dungeon. Ye see a SCROLL. Behind ye SCROLL is a FLASK.\nObvious exits are NORTH, SOUTH, and DENNIS.\n\n\n")
dungeon_text_no_scroll = _("Ye find yeself in yon dungeon. Ye see a FLASK.\nObvious exits are NORTH, SOUTH, and DENNIS.\n\n\n")
what_to_do = _("What wouldst thou deau?")
end_game_text = _("end game")
help_text = _("help")
inventory_text = _("inventory")
rope_text = _("rope")
trinket_text = _("trinket")
dennis_text = _("dennis")
not_dennis_text = _("not dennis")
south_text = _("south")
north_text = _("north")
go_dungeon_text = _("dungeon")
get_scroll_text_1 = _("get ye scroll")
get_scroll_text_2 = _("scroll")
get_scroll_text_3 = _("get scroll")
get_flask_text_1 = _("get ye flask")
get_flask_text_2 = _("get flask")
get_flask_text_3 = _("flask")
give_dennis_text = _("give trinket to dennis")
trinket_text_1 = _("trinket")
trinket_text_2 = _("get ye trinket")
trinket_text_3 = _("get trinket")
dennis_text = _("dennis")
not_dennis_text = _("not dennis")
no_user_text = _("Please actually writeth somethingith")
bad_user_text = _("That does not computether. Type HELP is thou needs of it")
go_north_text = _("\nYou go NORTH through yon corridor.\nYou arrive at parapets.\nYe see a ROPE.\nObvious exits are SOUTH and DUNGEON\n")
go_south_text = _("\nYou head south to an embankment, or maybe a chasm.\nYou can't decide which.\nAnyway, ye spies a TRINKET. Obvious exits are DUNGEON\n")
south_text_trinket = _("Obvious exits are DUNGEON")
go_dennis_text = _("Ye arrive at Dennis.\nHe wears a sporty frock coat and a long jimberjam.\nHe paces about nervously.\nObvious exits are NOT DENNIS.\n")
get_ye_flask_full_text = _("You cannot get the FLASK.\nIt is firmly bolted to a wall which is bolted to the rest of the dungeon which is probably bolted to a castle.\nNever you mind.\n")
get_ye_scroll_full_text = _("Ye takes the SCROLL and reads of it.\nIt doth say:\n\nBEWARE, READER OF YE SCROLL,\nDANGER AWAIT TO THE -\n\nThe SCROLL dissapears in they hands with ye olde ZAP!\n\n")
scroll_gone = _("Ye cannot take yon scroll as it dissapeard with ye olde ZAP!")
get_ye_rope_full_text = _("You attempt to take ye ROPE but alas it is enchanted!\nIt glows a mustard red and smells like a public privy.\nThe ROPE wraps round your neck and hangs you from the parapets.\nWith your last breath, you wonder what parapets are.")
get_ye_trinket_full_text = _("Ye getsts yon TRINKET and discover it to be a bauble.\nYou rejoice at your good fortune.\nYou shove the TRINKET in your pouchel.\nIt kinda hurts.\n")
give_dennis_trinket_text = _("A novel idea! You givst the TRINKET to Dennis and he happily agrees to tell you what parapets are. \nWith this new knowledge, ye escapes from yon dungeon in order to search for the new dungeons and to remain...")
already_got_trinket_text = _("Ye hast already goteth yon trinket")
no_trinket_to_give_text = _("Ye doth not hath a TRINKET to given to DENNIS")
dungeon_master_text = _("THY DUNGEONMAN!!\n")
item_removed_text = _("Item removed from inventory")
item_added_text = _("Item added to inventory")
final_score_text = _("Your score is:")
you_won_text = _("You hath won! Congraturation!")
game_over_text = _("GAME OVER")
inventory_empty_text = _("Your inventory is currently empty!")
inventory_singular_text = _("Your inventory consists of the following item:")
inventory_plural_text = _("Your inventory consists of the following items:")
what_to_do_text = _("What wouldst thou deau?")
no_not_dennis_text = _("There is no NOT DENNIS here, please try again")
no_trinket_text = _("There is no TRINKET here, please try again.\n")
no_rope_text = _("There is no Rope here, please try again\n")
acceptable_options_text = _("This is a list of acceptable options for the entire game:")
play_again_text = _("Play again? [Y/N]")
yes_option_text_1 = _("y")
yes_option_text_2 = _("yes")


f_condition_1 = False
f_condition_2 = False
n_condition_1 = False
n_condition_2 = False
s_condition_1 = False
d_condition_1 = False
a_condition_1 = False
inventory = []
choice_list = ["north","south","dennis","scroll","flask","get ye trinket","give trinket to dennis","get ye scroll","scroll","not dennis","help","trinket","inventory","end game","rope","get ye flask","dungeon"]
current_room = ''
current_score = 0
    


def unacceptableChoice(choice_made):
    if choice_made == end_game_text:
        choice_made = end_game_text
        return choice_made
    if choice_made == '':
        print(no_user_text)
        choice_made = input()
        choice_made = choice_made.casefold()
        unacceptableChoice(choice_made)
        return choice_made
    elif choice_made not in choice_list:
        print(bad_user_text)
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
    print(go_north_text)
    choice_made = ''
    return choice_made

def go_dungeon(choice_made):
    clear_Screen()
    if a_condition_1 == True:
        print(dungeon_text_no_scroll)
        choice_made = ''
        return choice_made
    else:
        print(dungeon_text)
        choice_made = ''
        return choice_made

def go_south(choice_made):
    clear_Screen()
    global s_condition_1
    s_condition_1 = True
    print(go_south_text)
    choice_made = ''
    return choice_made

def dennis(choice_made):
    clear_Screen()
    global d_condition_1
    d_condition_1 = True
    print(go_dennis_text)
    choice_made = ''
    return choice_made

def not_dennis(choice_made):
    clear_Screen()
    print(go_dennis_text)
    choice_made = ''
    return choice_made

def get_ye_flask(choice_made):
    clear_Screen()
    global f_condition_1
    print(get_ye_flask_full_text)
    f_condition_1 = True
    choice_made = ''
    return choice_made

def get_ye_scroll(choice_made):
    clear_Screen()
    global a_condition_1
    if a_condition_1 == False:
        print(get_ye_scroll_full_text)
        compute_score()
        a_condition_1 = True
        choice_made = ''
        return choice_made
    else:
        print(scroll_gone)
        choice_made = ''
        return choice_made

def get_ye_rope(choice_made):
    clear_Screen()
    print(get_ye_rope_full_text)
    ye_have_lost(choice_made)    
    choice_made = end_game_text
    compute_score_neg()
    return choice_made


def get_ye_trinket(choice_made,i):
    if i in inventory:
        clear_Screen()
        print(already_got_trinket_text)
        print(south_text_trinket)
        choice_made = user_input(choice_made)
        make_a_choice(choice_made)                    
    else:
        inventory.append(trinket_text)
        clear_Screen()
        print(item_added_text)
        print(get_ye_trinket_full_text)
        compute_score()
        print(south_text_trinket)
        choice_made = user_input(choice_made)
        make_a_choice(choice_made)

def give_dennis_trinket(choice_made):
    clear_Screen()
    if len(inventory) > 0:
        print(give_dennis_trinket_text)
        print(dungeon_master_text)
        inventory.remove(trinket_text)
        print(item_removed_text)
        ye_have_won(choice_made)
    else:
        print(no_trinket_to_give_text)
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
    print(final_score_text + str(current_score))
    choice_made = end_game_text
    return choice_made

def ye_have_won(choice_made):
    print(you_won_text)
    display_score(choice_made)
    return choice_made

def ye_have_lost(choice_made):
    print("\n\n" + game_over_text + "\n\n")
    display_score(choice_made)
    return choice_made
    

def inventory_show(choice_made):
    if len(inventory) < 1:
        print("\n\n" + inventory_empty_text + "\n")
        choice_made = user_input(choice_made)
        make_a_choice(choice_made)
    elif len(inventory) == 1:
        print("\n\n" + inventory_singular_text + "\n")
        print('\n'.join(inventory)+"\n\n")
        choice_made = user_input(choice_made)
        make_a_choice(choice_made)
    elif len(inventory) > 1:
        print("\n\n" + inventory_plural_text + "\n")
        print('\n'.join(inventory)+"\n\n")
        choice_made = user_input(choice_made)
        make_a_choice(choice_made)
            

def user_input(choice_made):
    print("\n" + what_to_do_text)
    choice_made = input()
    choice_made = choice_made.casefold()
    print("\n")
    return choice_made 

def clear_Screen():
    print("\n"*50)


def make_a_choice(choice_made):
    if choice_made == '':
        while choice_made == '':
            choice_made = user_input(choice_made)
            make_a_choice(choice_made)
            if choice_made == end_game_text:
                display_score()
                break
            
    while choice_made != end_game_text:
        if choice_made not in choice_list:
            choice_made = (unacceptableChoice(choice_made))
            break
            
        elif choice_made == get_flask_text_1 or choice_made == get_flask_text_2 or choice_made == get_flask_text_3:
            
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
        
        elif choice_made == get_scroll_text_1 or choice_made == get_scroll_text_2 or choice_made == get_scroll_text_3:
            get_ye_scroll(choice_made)
            print(dungeon_text_no_scroll)
            choice_made = user_input(choice_made)
            make_a_choice(choice_made)
            break
            
        elif choice_made == north_text:
            go_north(choice_made)
            choice_made = user_input(choice_made)
            make_a_choice(choice_made)
            break
        
        elif choice_made == south_text:
            go_south(choice_made)
            choice_made = user_input(choice_made)
            make_a_choice(choice_made)
            break

        elif choice_made == go_dungeon_text:
            go_dungeon(choice_made)
            choice_made = user_input(choice_made)
            make_a_choice(choice_made)
            break
        
        elif choice_made == dennis_text:
            dennis(choice_made)
            choice_made = user_input(choice_made)
            make_a_choice(choice_made)
            break
        
        elif choice_made == not_dennis_text:
            if d_condition_1 == False:
                print(no_not_dennis_text)
                choice_made = user_input(choice_made)
                make_a_choice(choice_made)
            not_dennis(choice_made)
            choice_made = user_input(choice_made)
            make_a_choice(choice_made)
            break

        elif choice_made == trinket_text_1 or choice_made == trinket_text_1 or choice_made == trinket_text_1:
            i = trinket_text
            if s_condition_1 == True:
                get_ye_trinket(choice_made,i)
                break
            else:
                print(no_trinket_text)
                choice_made = user_input(choice_made)
                make_a_choice(choice_made)
                break
            
        elif choice_made == rope_text:
            if n_condition_1 == False:
                print(no_rope_text)
                choice_made = user_input(choice_made)
                choice_made = end_game_text
                make_a_choice(choice_made)
                break
                
            elif n_condition_1 == True:
                get_ye_rope(choice_made)
                break
            
        elif choice_made == inventory_text:
            inventory_show(choice_made)
            break

        elif choice_made == give_dennis_text:
            give_dennis_trinket(choice_made)
            break
        
        elif choice_made == help_text:
            print(acceptable_options_text)
            print('\n'.join(choice_list))
            choice_made = user_input(choice_made)
            make_a_choice(choice_made)
            break
        
        
        elif choice_made == end_game_text:
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
    print(starting_text)
    print(dungeon_text)
    print(what_to_do)
    d_condition = yes_option_text_1
    while d_condition == yes_option_text_1:
        inventory.clear()
        choice_made = input()
        choice_made = choice_made.casefold()
        make_a_choice(choice_made)
        print(play_again_text)
        d_condition = input()
        d_condition = d_condition.casefold()
        if d_condition == yes_option_text_1 or d_condition == yes_option_text_2:
            clear_Screen()
            start_game()
        else:
            break

'''class Person:
  def __init__(self, location, flask):
    self.location = location
    self.flask = flask

p1 = Person("Dungeon", 0)

print(p1.location)
print(p1.flask)'''


clear_Screen()
start_game()


