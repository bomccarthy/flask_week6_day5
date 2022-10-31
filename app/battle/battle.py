import sys
sys.path.insert(0, 'C:/Users/sysrock/Documents/Coding/Pokemon Project/app/p_cards')
from pokeFunc import getPokemon
from getpass import getpass
from random import randint

def newSpeed(attack, defense, speed):
    if attack == 1 and defense == 1:
        return speed
    elif attack == 2 and defense == 2:
        return speed
    elif attack == 2:
        return speed/2        
    elif defense == 2:
        return speed*2

def hitDeduct(attack, defense):
    return randint(1,round(20*(attack/defense)))

def battleRound(name1, name2, hp1, hp2, new_speed1, new_speed2, attack1, attack2, defense1, defense2):
    if new_speed1 > new_speed2:
        input(f'{name1}, I choose you!!! (Press Enter to strike a blow)')
        hp2 -= hitDeduct(attack1, defense2)
        print(f'Hit Points: {hp1}    Hit Points: {hp2}')
        if hp2 <= 0:
            print(f'{name2} is dead. {name1} is the winner.')
        else:
            input(f'{name2}, I choose you!!! (Press Enter to strike a blow)')
            hp1 -= hitDeduct(attack2, defense1)
            print(f'Hit Points: {hp1}    Hit Points: {hp2}')
            if hp1 <= 0:
                print(f'{name1} is dead. {name2} is the winner.')
            else:
                battleRound(name1, name2, hp1, hp2, new_speed1, new_speed2, attack1, attack2, defense1, defense2)

def battle():
    user1_pokemon = getPokemon(getpass('Which of your pokemon would you like to use?'))
    user2_pokemon = getPokemon(getpass('Which of your pokemon would you like to use?'))
    name1 = user1_pokemon['name']
    name2 = user2_pokemon['name']
    hp1 = user1_pokemon['hp']
    att1 = user1_pokemon['attack']
    def1 = user1_pokemon['defense']
    spatt1 = user1_pokemon['special_attack']
    spdef1 = user1_pokemon['special_defense']
    speed1 = user1_pokemon['speed']
    hp2 = user2_pokemon['hp']
    att2 = user2_pokemon['attack']
    def2 = user2_pokemon['defense']
    spatt2 = user2_pokemon['special_attack']
    spdef2 = user2_pokemon['special_defense']
    speed2 = user2_pokemon['speed']
    choose_attack1 = int(getpass('User1, type 1 to use Attack, type 2 to use Special Attack.  '))
    if choose_attack1 == 1:
        attack1 = att1
    else:
        attack1 = spatt1
    choose_defense1 = int(getpass('User1, type 1 to use Defense, type 2 to use Special Defense.  '))
    if choose_defense1 == 1:
        defense1 = def1
    else:
        defense1 = spdef1
    choose_attack2 = int(getpass('User2, type 1 to use Attack, type 2 to use Special Attack.  '))
    if choose_attack1 == 1:
        attack2 = att2
    else:
        attack2 = spatt2
    choose_defense2 = int(getpass('User2, type 1 to use Defense, type 2 to use Special Defense.  '))
    if choose_defense1 == 1:
        defense2 = def2
    else:
        defense2 = spdef2
    new_speed1 = newSpeed(choose_attack1, choose_defense2, speed1)
    new_speed2 = newSpeed(choose_attack2, choose_defense1, speed2)
    battleRound(name1, name2, hp1, hp2, new_speed1, new_speed2, attack1, attack2, defense1, defense2)

battle()