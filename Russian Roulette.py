import os
import random
import time

rounds = 6
slot_bullet = random.randint(1, rounds)
stakes = 100

def TypeWrite(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def main():
    TypeWrite(f'Welcome to Russian Roulette!\n')
        
    while True:
        global rounds
        global slot_bullet
        global stakes
        chance = round((1/rounds)*100)
        TypeWrite('Here is your current status:')
        TypeWrite(f'Rounds: {rounds}\nChance of Death: %{chance}')
        TypeWrite(f'Stakes: ${stakes}')
        TypeWrite('Are you ready to play? y/n')
        ans = input()
        if ans.lower() in ['y', 'yes', '']:
            print()
            TypeWrite('Then let\'s begin...', 0.3)
            print()
            time.sleep(3)
            if rounds == slot_bullet:
                print('BANG!')
                print()
                TypeWrite('... you died.')
                time.sleep(2)
                TypeWrite('Welcome to hell.', 0.05)
                break
            else:
                TypeWrite('Click!', 0.002)
                rounds -= 1
                TypeWrite('Lucky...')
                print()
            TypeWrite('Alright...')
            TypeWrite('Now it\'s my turn!')
            print()
            time.sleep(2)
            if rounds == slot_bullet:
                print('BANG!')
                time.sleep(3)
                TypeWrite(f'Earned ${stakes}')
                break
            else:
                TypeWrite('Click!', 0.002)
                rounds -= 1
                TypeWrite('Phew...')
                print()
            stakes += abs((6 - rounds) *400)
        else:
            TypeWrite('Then...')
            TypeWrite('GET OUT!!', 0.0005)
            break

if __name__ == '__main__':
    main()
    time.sleep(2)
    print()
    TypeWrite('Thanks for playing! :D')