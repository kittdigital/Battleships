import pgzrun
import random
import pygame
import os

WIDTH = 540
HEIGHT = 640

BLACK = 0, 0, 0
WHITE = 255, 255, 255
RED = 128, 0, 0
GREEN = 0, 128, 0
GREY = 130, 130, 130

squareX = 0
squareY = 0

# define pieces as lists, [size, shortcode, hits, name]

carrier = [5, "ca", 5, "Aircarft Carrier"]
battleship = [4, "ba", 4, "Battleship"]
cruiser = [3, "cr", 3, "Cruiser"]
submarine = [3, "su", 3, "Submarine"]
destroyer = [2, "de", 2, "Destroyer"]

piece_array = [carrier, battleship, cruiser, submarine, destroyer]

ships_to_win = 5
moves = 0

game_on = True

playermap = [["","","","","","","","","",""],
             ["","","","","","","","","",""],
             ["","","","","","","","","",""],
             ["","","","","","","","","",""],
             ["","","","","","","","","",""],
             ["","","","","","","","","",""],
             ["","","","","","","","","",""],
             ["","","","","","","","","",""],
             ["","","","","","","","","",""],
             ["","","","","","","","","",""]]

enemymap = [["","","","","","","","","",""],
             ["","","","","","","","","",""],
             ["","","","","","","","","",""],
             ["","","","","","","","","",""],
             ["","","","","","","","","",""],
             ["","","","","","","","","",""],
             ["","","","","","","","","",""],
             ["","","","","","","","","",""],
             ["","","","","","","","","",""],
             ["","","","","","","","","",""]]




def draw():
    screen.fill((255, 255, 255))

    POSX = 20
    POSY = 0

    for h in range (10):
        screen.draw.text(chr(ord("a") + h), (POSX + (h*50) + 20, 2))


    for i in range (10):
        if (POSY == 0):
            POSY += 20
        else:
            POSY += 50
        for j in range (10):
            screen.draw.rect(Rect((POSX + (j*50), POSY), (50, 50)), BLACK)
            screen.draw.text(str(i+1), (2, POSY + 20))
            if enemymap[i][j] != "":
                if enemymap[i][j] == "HIT!":
                    screen.draw.filled_rect(Rect((POSX + (j*50), POSY), (50, 50)), GREEN)

                elif enemymap[i][j] == "MISS!":
                    screen.draw.filled_rect(Rect((POSX + (j*50), POSY), (50, 50)), RED)
                
                # Uncomment the below two lines to display enemy positions when debugging
                #else:
                    #screen.draw.text(enemymap[i][j], (POSX + ((j*50)+20), POSY + 20), color=BLACK)
 
    display_lives()

    if game_on == False:
        msg = "Game Over! \nYou Won In " + str(moves) + " Moves"
        screen.draw.text(msg,  center=(270, 260), shadow=(1,1), color=BLACK, fontsize = 70, scolor=GREY)

    




def check_win():

    global ships_to_win
    global game_on
    print("Ships Left: ", str(ships_to_win))

    if (ships_to_win == 0):
        print("You Win!  All ships found and destroyed")

        game_on = False


    

def on_mouse_down(pos):
    
    global moves
    if (game_on == True):

        posX = pos[0]
        posY = pos[1]

        squareX = (int((((posX) - 20) / 100) * 2 ))
        squareY = (int((((posY) - 20) / 100) * 2 ))

        if squareX > 9 or squareY > 9 :
            return

        if (enemymap[squareY][squareX] == "HIT!" ):
            print("hit")
            enemymap[squareY][squareX] = 'HIT!'

        elif (enemymap[squareY][squareX] == "ca" ):
            carrier[2] = carrier[2] - 1
            print(carrier[3], "Hit!")
            enemymap[squareY][squareX] = 'HIT!'
            check_ship_status(carrier)

        elif (enemymap[squareY][squareX] == "ba" ):
            battleship[2] = battleship[2] - 1
            print(battleship[3], "Hit!")
            enemymap[squareY][squareX] = 'HIT!'
            check_ship_status(battleship)


        elif (enemymap[squareY][squareX] == "cr" ):        
            cruiser[2] = cruiser[2] - 1
            print(cruiser[3], "Hit!")
            enemymap[squareY][squareX] = 'HIT!'
            check_ship_status(cruiser)


        elif (enemymap[squareY][squareX] == "su" ):
            submarine[2] = submarine[2] - 1
            print(submarine[3], "Hit!")
            enemymap[squareY][squareX] = 'HIT!'
            check_ship_status(submarine)


        elif (enemymap[squareY][squareX] == "de" ):
            destroyer[2] = destroyer[2] - 1
            print(destroyer[3], "Hit!")
            enemymap[squareY][squareX] = 'HIT!'
            check_ship_status(destroyer)

        else:
            print("miss")
            enemymap[squareY][squareX] = 'MISS!'
            moves = moves + 1

 
        


def display_lives():

    

    for j in range (len(piece_array)):

        if piece_array[j][2] == 0:
            screen.draw.filled_rect(Rect((20 +(j*105), HEIGHT - 100), (75, 50)), GREEN)
        else:
            screen.draw.rect(Rect((20 +(j*105), HEIGHT - 100), (75, 50)), BLACK)


        screen.draw.text(str(piece_array[j][2]), (45 +(j * 105), HEIGHT - 90), color=BLACK, fontsize = 50)

        screen.draw.text(piece_array[j][3], (20 + (j * 107), HEIGHT - 40), color=BLACK, fontsize = 16)

def check_ship_status(piece):
    
    global ships_to_win
    global moves 
    
    moves = moves + 1
    if piece[2] == 0 :
            print("You Sunk The " + piece[3] + "!")
            ships_to_win = ships_to_win -1
    
    check_win()



def place_enemy(piece, enemymap):

    piece_size = piece[0]
    piece_code = piece[1]
    valid_position = False   

    while (not valid_position):
        x = random.randint(0,9)
        y = random.randint(0,9)
        o = random.randint(0,1)
        if o == 0:
            orientation = "v"
        else:
            orientation = "h"
        
        valid_position = validate(enemymap,piece_size,x,y,orientation)

    enemymap = place_ship(enemymap,piece_size,piece_code,orientation,x,y)
   
    printEnemyMap()



def place_ship(map,ship,s,orientation,x,y):

	#place ship based on orientation
	if orientation == "v":
		for i in range(ship):
			map[x+i][y] = s
	elif orientation == "h":
		for i in range(ship):
			map[x][y+i] = s

	return map



def validate(board,piece_size,x,y,ori):

	#check if ship will fit in the board and is not conflicting with other ships
	if ori == "v" and x+piece_size > 10:
		return False
	elif ori == "h" and y+piece_size > 10:
		return False
	else:
		if ori == "v":
			for i in range(piece_size):
				if enemymap[x+i][y] != '':
					return False
		elif ori == "h":
			for i in range(piece_size):
				if enemymap[x][y+i] != '':
					return False
		
	return True


def generate_random_position(limit):
    
    position = [random.randint(0,9 - limit), random.randint(0,9 - limit)]

    if (enemymap[position[0]][position[1]] != ''):
        print("random position generated: ", position)
        generate_random_position(limit)
    else:
        return position





def printEnemyMap():
    for j in range(len(enemymap)):
        print(enemymap[j])


place_enemy(carrier, enemymap)
place_enemy(battleship, enemymap)
place_enemy(cruiser, enemymap)
place_enemy(submarine, enemymap)
place_enemy(destroyer, enemymap)

os.environ['SDL_VIDEO_CENTERED'] = '1'
pgzrun.go()


