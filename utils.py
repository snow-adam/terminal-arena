import time
import random

def line_break(lines, timer=0):
    time.sleep(timer)
    for i in range(lines):
        print("\n")

def selection():
    print("\n> ", end="")

def generate_pokemon():
    generator = random.randint(1, 3)

    match generator:
        case 1:
            return "Bulbasaur"
        case 2:
            return "Charmander"
        case 3:
            return "Squirtle"
        
def display_hp(hp):
    for i in range(1, hp, 5):
        if (i >= hp - 5):
            break
        else:
            print("█", end="")