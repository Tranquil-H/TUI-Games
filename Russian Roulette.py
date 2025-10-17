import os
import random
import time

def TypeWrite(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

if os.name == 'nt':
    import msvcrt
    def flush_input():
        os.system('@ECHO ON')
        while msvcrt.kbhit():
            msvcrt.getch()
else:
    import termios
    import sys
    def flush_input():
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)
        os.system('stty echo')

def main():
    rounds = 6
    slot_bullet = random.randint(1, rounds)
    stakes = 100
    os.system('cls') if os.name == 'nt' else os.system('clear')
    os.system('stty -echo')
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

        flush_input()
        if input().lower() in ['y', 'yes', '']:
            os.system('stty -echo') or os.system('@ECHO OFF')
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
            os.system('stty -echo') or os.system('@ECHO OFF')
            print()
            TypeWrite('Then...')
            TypeWrite('GET OUT!!', 0.0005)
            print()
            time.sleep(0.5)
            if rounds < 6:
                TypeWrite(f'Earned ${stakes}')
            break
    os.system('stty echo') or os.system('@ECHO ON')

if __name__ == '__main__':
    main()