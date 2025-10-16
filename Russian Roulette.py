import os
import random
import time

def TypeWrite(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def main():
    rounds = 6
    slot_bullet = random.randint(1, rounds)
    stakes = 100
    os.system('cls') if os.name == 'nt' else os.system('clear')
    TypeWrite(f'Welcome to Russian Roulette!\n')
    time.sleep(1)
    while True:
        print()
        os.system('cls') if os.name == 'nt' else os.system('clear')
        chance = round((1/rounds)*100)
        stakes += abs((6 - rounds) * random.randint(100, 200))
        TypeWrite('Here is your current status:')
        TypeWrite(f'Rounds: {rounds}\nChance of Death: %{chance}')
        TypeWrite(f'Stakes: ${stakes}')
        TypeWrite('Are you ready to play? y/n')

        if input().lower() in ['y', 'yes', '']:
            print()
            TypeWrite('Then let\'s begin...', 0.15)
            print()
            time.sleep(3)

            if rounds == slot_bullet:
                print('BANG!')
                print()
                TypeWrite('... you died.')
                time.sleep(0.5)
                TypeWrite('Welcome to hell.', 0.05)
                print()
                break
            else:
                TypeWrite('Click!', 0.002)
                rounds -= 1
                TypeWrite('Lucky...')
                print()

            TypeWrite('Alright, Now it\'s my turn!')
            print()
            time.sleep(2)

            if rounds == slot_bullet:
                print('BANG!')
                print()
                time.sleep(3)
                TypeWrite(f'Earned ${stakes}')
                break
            else:
                TypeWrite('Click!', 0.002)
                rounds -= 1
                TypeWrite('Phew...')
                time.sleep(1)
                print()
        else:
            print()
            TypeWrite('Then...')
            TypeWrite('GET OUT!!', 0.0005)
            print()
            time.sleep(0.5)
            if rounds < 6:
                TypeWrite(f'Earned ${stakes}')
            break

if __name__ == '__main__':
    main()