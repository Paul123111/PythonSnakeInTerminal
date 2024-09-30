#!/usr/bin/python3

import subprocess
import time
import sys
from random import randrange
from curtsies import Input
import curtsies.events

class Frame(curtsies.events.ScheduledEvent):
    pass

def create_matrix(w, h):
    matrix = [['.' for x in range(w)] for y in range(h)]
    return matrix

def print_screen(matrix, length):
    output = "\n\r"
    output += "       Score = " + str(length-4) + " - Snake in Terminal - WASD to move - Q to quit\n  _"
    
    for j in range(len(matrix[0])):
        output += "__"
    output += "_\n  |"

    for i in matrix:
        for j in range(len(i)):
            output += i[j] + " "
        output += "|\n  |"

    output += "\r  *"

    for j in range(len(matrix[0])):
        output += "**"
    output += "*\n"

    sys.stdout.write(output)

def game_over(matrix, length):
    print_screen(matrix, length)
    print('Game Over! Your score was ' + str(length-4) + '!')
    input('Press enter to exit...')
    subprocess.run("clear", shell=True)

def main():
    
    #screen variables
    if (len(sys.argv) == 5):
        if (sys.argv[1] == '--size'):
            try:
                args = sys.argv[2:]
                width = int(args[0])
                height = int(args[1])
                num_apples = int(args[2])
            except:
                print("To choose game size, use '--size _x_ _y_ _num-apples_'")
                return 1
    elif len(sys.argv) == 1:
        width = 32
        height = 32
        num_apples = 1
    else:
        print("To choose game size, use '--size _x_ _y_ _num-apples_'")
        return 1
    
    try:
        matrix = create_matrix(width, height)
    except:
        print("To choose game size, use '--size _x_ _y_ _num-apples_'")
        return 1

    #matrix[4][8] = '@'
    #matrix[7][15] = 'a'
    
    #game variables
    direction = 1 #0=up 1=right 2=down 3=left
    player_x = randrange(width)
    player_y = randrange(height)
    length = 4
    snake_coords = [(player_x, player_y)]
    apple_coords = []

    for i in range(num_apples):
        apple_coords.append((randrange(width), randrange(height)))

    input_generator = Input(keynames='curses')
    schedule_next_frame = input_generator.scheduled_event_trigger(Frame)
    schedule_next_frame(when=time.time())

    with input_generator:
        for e in input_generator:
        #game loop

            ########################
            # player input
            ########################
            if e == 'q':
                subprocess.run("clear", shell=True)
                break

            #choosing direction

            if (e == 'a') & (direction!=1):
                direction=3
            elif (e == 'd') & (direction!=3):
                direction=1
            elif (e == 's') & (direction!=0):
                direction=2
            elif (e == 'w') & (direction!=2):
                direction=0

            ########################
            # game updates
            ########################
            #moving player
            if direction == 0:
                player_y -= 1
            elif direction == 1:
                player_x += 1
            elif direction == 2:
                player_y += 1
            elif direction == 3:
                player_x -= 1
            
            snake_coords.insert(0, (player_x, player_y))
            if len(snake_coords) > length:
                snake_coords.pop(length)

            #updating what screen should look like
            #if player eats apple
            if len(snake_coords) >= (width*height):
                return 1

            if (player_x, player_y) in apple_coords:
                for i in range(len(apple_coords)):
                    while apple_coords[i] in snake_coords:
                        apple_coords[i] = (randrange(width), randrange(height))
                length += 1

            if (player_x, player_y) in snake_coords[1:]:
                game_over(matrix, length)
                break

            if (player_x >= 0) & (player_y >= 0) & (player_x < width) & (player_y < height):
                counter = 0
                for i in matrix:
                    for j in range(len(i)):
                        if (j, counter) in snake_coords:
                            if (j, counter) == snake_coords[0]:
                                i[j] = '\x1b[0;30;47m' + '@' + '\x1b[0m'
                            else:
                                i[j] = '\x1b[0;37;44m' + 'O' + '\x1b[0m'
                        elif (j, counter) in apple_coords:
                            i[j] = '\x1b[0;30;41m' + 'a' + '\x1b[0m'
                        else:
                            i[j] = '.'
                    counter += 1
            else:
                game_over(matrix, length)
                break

            ########################  
            # drawing screen
            ########################

            print_screen(matrix, length)
            
            #move cursor to top of game
            for i in range(height+4):
                print("\033[A", end="")
            sys.stdout.flush()
            
            if isinstance(e, Frame):
                when = e.when + 0.1
                while when < time.time():
                    when += 0.1
                schedule_next_frame(when)
    return 0

if __name__ == '__main__':
    main()
