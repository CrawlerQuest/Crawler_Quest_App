from art import *
from colorama import Fore, Back, Style



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
    (S)tart Game
    (Q)uit Game
    """)
    print(Style.RESET_ALL) 
    if start_game == "S":
        play()
    else:
        quits()

def play():
    pass

def fight(Character, Monster):
    turn = 0
    rounds = 0
    while Character.vitality and Monster.vitality:
        if not turn:
            take_turn(Character)
            turn += 1
        else:
            take_turn(Monster)
            turn -= 1
            rounds += 1

def take_turn(actor):
    if actor.id == "c":
        take_t = input("""
        (A)ttack
        (D)efend
        """)

        if take_t == "A":
            damage = Character.strength - Monster.defense
            if damage == 0:
                damage = 1
            Monster.vitality -= damage
        elif take_t == "D":
            Character.defend()
    elif actor.id == "m":
        actor.behavior()
        



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