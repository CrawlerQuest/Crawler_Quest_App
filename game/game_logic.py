from art import *
import random
import re
import pickle
from colorama import Fore, Back, Style
try:
    from character.character_logic import Character
    from monster.monster_logic import Bestiary, Monster
    from merchant.merchant_logic import Storefront, Items
except:
    from game.character.character_logic import Character
    from game.monster.monster_logic import Bestiary, Monster
    from game.merchant.merchant_logic import Storefront, Items


import os

# def center_console():
try:
    term_size = os.get_terminal_size().columns
except:
    term_size = 50

# print("ALASKA".center(term_size))
# width_size = os.term_size.columns()
# print(width_size)


def game_logic():
    title = text2art("                     Crawler Quest", chr_ignore=True)
    # center_title = print(title.center(term_size.columns))
    print(Fore.RED)
    print(Back.BLACK)
    print(Style.BRIGHT + title)
    print(Style.RESET_ALL) 
    print(Fore.GREEN)
    print(Style.BRIGHT)
    print(Back.BLACK)
    print("A long time ago, in a galaxy far, far away...".center(term_size))
    start_game = input("""
    (s)tart Game
    (q)uit Game
    """)
    # print(Style.RESET_ALL) 
    if start_game == "s":
        adventurer = load()
        store = Storefront() 
        besti = Bestiary()
        play(adventurer, besti, store) 
    elif start_game == 'q':
        quits()
    else:
        print('That was the first test and you failed it')
        quits()

def load():
    """reads save file if their is not one it creates then reads
    Returns:
        [string]:
    """
    adv = False
    save_me = False
    username = input("""
    Please enter your name adventurer
    """)
    try:
        with open(f'{username}.pkl','rb') as load_adv:
            adv = pickle.load(load_adv)
    except:
        print('Character Created')
        with open(f'{username}.pkl','wb') as new_adv:
            save_me = Character(username)
            pickle.dump(save_me,new_adv,pickle.HIGHEST_PROTOCOL)

    if adv:
        print(f"""
        Name:{adv.name}
        Level:{adv.level}
        Strength:{adv.strength}
        Vitality:{adv.vit}
        Potatoes:{adv.potatoes}
        """)
        return adv

    elif save_me:
        print(f"""
        Name:{save_me.name}
        Level:{save_me.level}
        Strength:{save_me.strength}
        Vitality:{save_me.vit}
        Potatoes:{save_me.potatoes}
        """)
        return save_me

def save(adv):
    with open(f'{adv.name}.pkl','wb') as sav_adv:
        pickle.dump(adv,sav_adv,pickle.HIGHEST_PROTOCOL)
def play(adv, bestiary, store):
    file = read_file('./assets/story.txt')
    story = process_story(file)
    input_keys = 'qwer'
    input_string = f'''\nWhat will you do?'''
    print(f'''\n{story['start'][0]}''')
    exit_peripheral = False
    current_ops = get_options(story['start'])

    while adv.vit:
        if len(current_ops) == 0:
            gameover("Your not smart enough")
        if not exit_peripheral:
            for option in range(len(current_ops)):
                input_string += f'''
                \n({input_keys[option]}){current_ops[option]}
                '''

        choice = input(input_string)
        if choice == 'q':
            current_ops, exit_peripheral = choice_Handler(current_ops[0],adv,bestiary,story,0, store)
            if not exit_peripheral:
                input_string = f'''\nWhat will you do?'''  
        elif choice == 'w':
            current_ops, exit_peripheral = choice_Handler(current_ops[1],adv,bestiary,story,1, store)
            if not exit_peripheral:
                input_string = f'''\nWhat will you do?'''  
        elif choice == 'e':
            current_ops, exit_peripheral = choice_Handler(current_ops[2],adv,bestiary,story,2, store)
            if not exit_peripheral:
                input_string = f'''\nWhat will you do?'''  
        elif choice == 'r':
            current_ops, exit_peripheral = choice_Handler(current_ops[3],adv,bestiary,story,3, store)
            if not exit_peripheral:
                input_string = f'''\nWhat will you do?'''  
        elif choice == 'lft':
                mon = random.choice(bestiary.randos)
                mon.scale(adv.level)
                fight(adv,mon)
                save(adv)
                exit_peripheral = True
        elif choice == 'boss':
                mon = random.choice(bestiary.bosses)
                fight(adv,mon)
                save(adv)
                exit_peripheral = True
        elif choice == 'quit':
            return adv.level
        else:
            input_string = f'''\nWhat will you do?'''
        

def choice_Handler(option,adv,bestiary,story,idx, store):
    exit_peripheral = False
    if option == 'fight':
        boss_check = []
        boss = random.choice(bestiary.bosses)
        small = random.choice(bestiary.randos)
        boss_check.append(boss)
        boss_check.append(small)
        if adv.level > 8:
            mon = random.choice(boss_check)
            mon.scale(adv.level)
            check = fight(adv,mon)
            save(adv)
            exit_peripheral = True
        else:
            mon = small
            mon.scale(adv.level)
            check = fight(adv,mon)
            save(adv)
            exit_peripheral = True
        if check:
            win_game(adv, bestiary, store)
    elif option == 'store':
        store.show_shop()
        shop(adv,store)
        option = get_options(story["town"])
        save(adv)
        exit_peripheral = True
    else:
        print_val = story[f'{option}']
        print(f'{print_val[0]}')
        option = get_options(story[f'{option}'])
    return option, exit_peripheral

def read_file(txt_file):
    with open(txt_file) as text:
        story_base = text.read()
        return story_base

def store_story(story_txt):
    parsed = tuple(re.findall(r'\[(.*?)\]', story_txt , re.IGNORECASE))
    return parsed
    
def process_story(txt_file):
    story_keys = {}
    count = 0
    key_Nodes = tuple(re.findall(r"\{([A-Za-z0-9_'\s1-]+)\}", txt_file, re.IGNORECASE))
    for key in key_Nodes:
        # print(key)
        story_keys[f'{key}'] = []
    
    para = store_story(txt_file)
    
    for key in story_keys.keys():
        story_keys[f'{key}'].append(para[count])
        
        count += 1
        # print(count) 
    #print(story_keys)
    return story_keys

def get_options(line):
    """Takes in line of story text
    parses out options
    Args:
        line ([string]): [story line]
        Brandon Gonzo
    """
    options = tuple(re.findall(r"\(([A-Za-z0-9_'\s1-]+)\)", line[0], re.IGNORECASE))
    return options


def fight(Character, Monster):
    """
    Args:
        Character (character object): [description]
        Monster (monster object): [description]
    Calls:
        gameover: if character vit reaches zero
        winfight: if monster vit reaches zero
    """
    def fight_text(adv,mon):
        print(f"Character health {Character.vit} ***** Monster health {Monster.vit}".center(term_size))
        print(f"Character strength {Character.strength} ***** Monster strength {Monster.strength}".center(term_size))
        print(f"Character defense {Character.defense} ***** Monster defense {Monster.defense}\n".center(term_size))
                                                  
    turn = 0
    rounds = 0
    mon_reset = Monster.vit
    print(f'A {Monster.name} approaches\n'.center(term_size))
    fight_text(Character, Monster)

    while Character.vit and Monster.vit:
        if not turn:
            take_turn(Character,Monster)
            turn += 1
            fight_text(Character, Monster)
            if  Monster.vit <= 0:
                 return winfight(Monster,Character,mon_reset)
        else:
            take_turn(Monster,Character)
            turn -= 1
            rounds += 1
            fight_text(Character, Monster)
        if Character.vit <= 0:
            return gameover(Monster.name)
        elif Monster.vit <= 0:
             return winfight(Monster.name)

def take_turn(actor,passive):
    monster_turn_stack = []
    player_turn_stack = []
    if actor.id == "c":
        if player_turn_stack:
            actor.defense = actor.defense / 1.25
            player_turn_stack.pop(0)
        take_t = input("""
        (a)ttack
        (d)efend
        """)

        if take_t == "a":
            damage = actor.strength - passive.defense
            if damage == 0:
                damage = 1
            passive.vit -= damage
        elif take_t == "d":
            actor.defend()
            player_turn_stack.append('def_up')
    elif actor.id == "m":
        if monster_turn_stack:
            actor.defense = actor.defense / 1.25
            monster_turn_stack.pop(0)
        action,atk_name = actor.behavior()
        if type(action) is int or float:
            damage = action
            if damage == 0:
                damage = 1
            print(f'{actor.name} {atk_name}ed')
            passive.vit -= damage
        else:
            print(f'{actor.name} {atk_name}ed')
            monster_turn_stack.append('def_up')

def winfight(mon,character,hp_reset):
    """handles after battle exp gain and resuming story
    Args:
        mon ([type]): [description]
        character ([type]): [description]
    """
    mon.vit = hp_reset
    character.take_pots(mon.potatoes)
    print(f"you have {character.potatoes} NOW")
    print(f'You defeated {mon.name} and gained {mon.exp_val} experience')
    exp_needed, exp_curr = character.exp_gain(mon.exp_val)
    print(f'{exp_needed} to level, current EXP: {exp_curr}')
    return True

def shop(adv,store):
    while adv.vit:
        buy = input("What are you buying (armor , weapon)\n Press (z) to exit store")
        if buy == "armor":
            item_select = input("Type name of item\n")
            for item in store.armor:
                if item_select == item.name:
                    if adv.potatoes >= item.price:
                        adv.potatoes -= item.price
                        adv.add_item(item)
                        print('Thank you for your buisness\n')
                        adv.pull_stats()
                        store.armor.pop(0)
                    else:
                        print("No money no honey")
        elif buy == "weapon":
            item_select = input("Type name of item\n")
            for item in store.weapons:
                if item_select == item.name:
                    if adv.potatoes >= item.price:
                        adv.potatoes -= item.price
                        adv.add_item(item)
                        print('Thank You For Your buisness')
                        adv.pull_stats()
                        store.weapons.pop(0)
                    else:
                        print("No money no honey")
        elif buy == 'z':
            print('thanks for shopping')
            break
    

    
def gameover(cause):
    endgame = text2art(f"{cause}", chr_ignore=True)
    print(endgame)
    endgame_input = input("""
    (q)uit
    (r)estart
    """)
    if endgame_input == "q":
        quits()
    else:
        game_logic()

def quits():
    print("You are the weakest link goodbye")
    exit()


def win_game(adv, bestiary, store):
    wingame = text2art(f"Path Complete", chr_ignore=True)
    reset_choice = input("Would you like to choose another path? (r)eset or (q)uit")
    if reset_choice == "r":
        play(adv, bestiary, store)
    elif reset_choice == "q":
        quits()
    

if __name__ == "__main__":
    game_logic()
    # story_txt = read_file('./assets/story.txt')
    # print(store_story(story_txt))
    # process_story(story_txt)
  







    # count = 0
    # children = []
    # root = KaryNode(key_Nodes[0])
    # story_tree = KaryTree(root)
    # # print(story_tree.root.value)
    # scene_parse = tuple(re.findall("\[.*?\]",txt_file, re.IGNORECASE))
    # for scene in range(len(scene_parse)):
    #     children_parse = tuple(re.findall("\(.*?\)",scene_parse[scene], re.IGNORECASE))
    #     if count == 0:
    #         root.children.append(KaryNode(children_parse[0]))
    #         root.children.append(KaryNode(children_parse[1]))
    #         root.children.append(KaryNode(children_parse[2]))
    #         count += 1
    #     children.append(children_parse)
    # saplings = root.children
    # for child in range(len(saplings)):
        
    #     children_parse = tuple(re.findall("\(.*?\)",scene_parse[scene], re.IGNORECASE))
    #     for grand_child in range(len(children_parse)):
    #         saplings[child].children.append(KaryNode(children_parse[grand_child]))


    # return story_tree
    # #    
    # #     else:
    # #         child = root.children[]
    # #         child.children.append(KaryNode(children_parse[scene]))
    # #         count +=1
    
    # # return story_tree