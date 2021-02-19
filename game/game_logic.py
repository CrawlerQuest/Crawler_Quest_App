from art import *
import random
import re
from colorama import Fore, Back, Style
from kary import KaryTree, KaryNode
from character.character_logic import Character
from monster.monster_logic import Bestiary, Monster


def game_logic():
    title = text2art("Crawler Quest", chr_ignore=True)
    print(Fore.RED + title)
    print(Style.RESET_ALL) 
    print(Fore.BLUE)
    print("""
    *****************
    Welcome
    to
    the 
    thunderdome
    *****************
    """)
    start_game = input("""
    (s)tart Game
    (q)uit Game
    """)
    print(Style.RESET_ALL) 
    if start_game == "s":
        adventurer = Character(load())  #Creates instance of our character
        besti = Bestiary()
        play(adventurer,besti) 
    else:
        quits()

def load():
    """reads save file if theri is not one it creates then reads
    Returns:
        [string]:
    """
    loaded_data = False
    save_data = False
    username = input('Please enter your name adventurer')
    try:
        loaded_data = open(f'{username}.txt','r')
    except:
        save_data = open(f'{username}.txt','x')
        save_data.write(f'{username}')
        return_data = open(f'{username}.txt','r')

    if loaded_data:
        return loaded_data.read()
    elif save_data:
        return return_data.read()

def play(adv,bestiary):
    file = read_file('./assets/story.txt')
    story = process_story(file)
    input_keys = 'qwer'
    input_string = f'''
What will you do?'''
    print(f'''{story['start'][0]}
    ''')
    current_ops = get_options(story['start'])

    while adv.vit:
        for option in range(len(current_ops)):
            input_string += f''' 
({input_keys[option]}){current_ops[option]}
'''
        choice = input(input_string)
        if choice == 'q':
            if current_ops[0] == 'fight':
                mon = random.choice(bestiary.randos)
                fight(adv,mon)
            else:
                print(story[f'{current_ops[0]}'][0])
                current_ops = get_options(story[f'{current_ops[0]}'])
                print(current_ops)
                input_string = f'''
What will you do?'''
        elif choice == 'w':
            if current_ops[1] == 'fight':
                mon = random.choice(bestiary.randos)
                fight(adv,mon)
            else:
                print(story[f'{current_ops[1]}'][0])
                current_ops = get_options(story[f'{current_ops[1]}'])
                print(current_ops)
                input_string = f'''
What will you do?'''

        elif choice == 'e':
            if current_ops[2] == 'fight':
                mon = random.choice(bestiary.randos)
                fight(adv,mon)
            else:
                print(story[f'{current_ops[2]}'][0])
                current_ops = get_options(story[f'{current_ops[2]}'])
                print(current_ops)
                input_string = f'''
What will you do?'''

        elif choice == 'r':
            if current_ops[3] == 'fight':
                mon = random.choice(bestiary.randos)
                fight(adv,mon)
            else:
                print(story[f'{current_ops[3]}'][0])
                current_ops = get_options(story[f'{current_ops[3]}'])
                input_string = f'''
What will you do?'''

        elif choice == 'lft':
                mon = random.choice(bestiary.randos)
                fight(adv,mon)
        else:
            input_string = f'''
What will you do?
                            '''



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
    turn = 0
    rounds = 0
    mon_reset = Monster.vit
    print(f'A {Monster.name} approaches')
    print(f"""
adv health {Character.vit}   **************     monster health {Monster.vit}
strength {Character.strength}                   strenght {Monster.strength}
defense {Character.defense}                     defense {Monster.defense}
                                                malace {Monster.malice}
        """)
     
    while Character.vit and Monster.vit:
        if not turn:
            take_turn(Character,Monster)
            turn += 1
            print(f"""
adv health {Character.vit}   **************     monster health {Monster.vit}
strength {Character.strength}                   strenght {Monster.strength}
defense {Character.defense}                     defense {Monster.defense}
                                                malace {Monster.malice}
        """)
            if  Monster.vit <= 0:
                 return winfight(Monster,Character,mon_reset)
        else:
            take_turn(Monster,Character)
            turn -= 1
            rounds += 1
            print(f"""
adv health {Character.vit}   **************     monster health {Monster.vit}
strength {Character.strength}                   strenght {Monster.strength}
defense {Character.defense}                     defense {Monster.defense}
                                                malace {Monster.malice}
        """)
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
        if type(action) is int:
            damage = action
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
    # hp for monsters need to be reset
    mon.vit = hp_reset
    print(f'You defeated {mon.name} and gained {mon.exp_val} experience')
    print(character.exp_gain(mon.exp_val))

    


def gameover(cause):
    endgame = text2art(f"{cause}", chr_ignore=True)
    print(endgame)
    endgame_input = input("""
    (Q)uit
    (R)estart
    """)
    if endgame_input == "Q":
        quits()
    else:
        play()

def quits():
    pass

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