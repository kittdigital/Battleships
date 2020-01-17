import pgzrun
import random

WIDTH = 540
HEIGHT = 640

# define pieces as lists, [size, shortcode]

carrier = [5, "ca"]
battleship = [4, "ba"]
cruiser = [3, "cr"]
submarine = [3, "su"]
destroyer = [2, "de"]

test = 0


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
    screen.fill((128, 0, 0))

    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    POSX = 20
    POSY = 0

    place_enemy(carrier, enemymap)
    place_enemy(battleship, enemymap)
    place_enemy(cruiser, enemymap)
    place_enemy(submarine, enemymap)
    place_enemy(destroyer, enemymap)


    for i in range (10):
        if (POSY == 0):
            POSY += 20
        else:
            POSY += 50
        for j in range (10):
            screen.draw.rect(Rect((POSX + (j*50), POSY), (50, 50)), BLACK)
            if enemymap[i][j] != "":
                screen.draw.text(enemymap[i][j], (POSX + ((j*50)+20), POSY + 20))

    
    for i in range (5):
        screen.draw.rect(Rect((20 +(i*100), HEIGHT - 100), (50, 50)), BLACK)


def place_enemy(piece, enemymap):

    piece_size = piece[0]
    piece_code = piece[1]
    valid_position = False

    print(piece_size)
    print(piece_code)
    

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



def place_ship(enemymap,ship,s,orientation,x,y):

	#place ship based on orientation
	if orientation == "v":
		for i in range(ship):
			enemymap[x+i][y] = s
	elif orientation == "h":
		for i in range(ship):
			enemymap[x][y+i] = s

	return enemymap



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




def define_enemy_pos():
    




    define_carrier_pos()
    define_battleship_pos()
    define_cruiser_pos()



def printEnemyMap():
    for j in range(len(enemymap)):
        print(enemymap[j])


def define_carrier_pos():
    carrier_positions = [[0,0], [0,0], [0,0], [0,0], [0,0]]

    carrier_positions[0] = [random.randint(0,9), random.randint(0,9)]
    print(carrier_positions[0])

    if  (carrier_positions[0][0] > 4) and (carrier_positions[0][1] > 4):
        define_carrier_pos()
    elif (carrier_positions[0][0] > 4):
        
        enemymap[carrier_positions[0][0]][carrier_positions[0][1]] = "ca"
        for i in range(1,5):

            carrier_positions[i] = [carrier_positions[i-1][0], carrier_positions[i-1][1] + 1]
            print("Carrier Position: " + str(carrier_positions[i][0]) + ", " + str(carrier_positions[i][1]))
            print()
            enemymap[carrier_positions[i][0]][carrier_positions[i][1]] = "ca"
        
        printEnemyMap()
    
    elif (carrier_positions[0][0] <= 4):
        direction = random.randint(0,1)  # 0 = Left to right, 1 = Up down
        
        if (direction == 0) and (carrier_positions[0][1] <= 4):
            enemymap[carrier_positions[0][0]][carrier_positions[0][1]] = "ca"
            for i in range(1,5):

                carrier_positions[i] = [carrier_positions[i-1][0], carrier_positions[i-1][1] + 1]
                print(carrier_positions[i][0])
                print(carrier_positions[i][1])
                enemymap[carrier_positions[i][0]][carrier_positions[i][1]] = "ca"
        
            printEnemyMap()
        else:

            enemymap[carrier_positions[0][0]][carrier_positions[0][1]] = "ca"
            for i in range(1,5):

                carrier_positions[i] = [carrier_positions[i-1][0] + 1, carrier_positions[0][1]]
                print(carrier_positions[i][0])
                print(carrier_positions[i][1])
                enemymap[carrier_positions[i][0]][carrier_positions[i][1]] = "ca"
        
            printEnemyMap()


def define_battleship_pos():
    battleship_positions = [[0,0], [0,0], [0,0], [0,0]]

    battleship_positions[0] = [random.randint(0,9), random.randint(0,9)]

    print(battleship_positions[0])









    
    






def define_cruiser_pos():
    cruiser_positions = [[0,0], [0,0], [0,0]]

    cruiser_positions[0] = [random.randint(0,9), random.randint(0,9)]

    
    print(cruiser_positions[0])

    if  (cruiser_positions[0][0] > 3) and (cruiser_positions[0][1] > 3):
        define_cruiser_pos()
    elif (cruiser_positions[0][0] > 3):
        
        if (enemymap[cruiser_positions[0][0]][cruiser_positions[0][1]] != ''):
            define_cruiser_pos()
        else:

            enemymap[cruiser_positions[0][0]][cruiser_positions[0][1]] = "cr"


        for i in range(1,3):

            cruiser_positions[i] = [cruiser_positions[i-1][0], cruiser_positions[i-1][1] + 1]
            print(cruiser_positions[i][0])
            print(cruiser_positions[i][1])

            if (enemymap[cruiser_positions[i][0]][cruiser_positions[i][1]] != ''):
                print("Enemy Grid Search Result: " + str(searchEnemyGrid(enemymap,"cr")))
                if (searchEnemyGrid(enemymap,"cr")):
                    print("No \"cr\" found")
                else:

                    enemymap[cruiser_positions[i][0]][cruiser_positions[i][1]] = "cr"

                # define_cruiser_pos()
            else:
                enemymap[cruiser_positions[i][0]][cruiser_positions[i][1]] = "cr"
        
        printEnemyMap()
    
    elif (cruiser_positions[0][0] <= 3):
        direction = random.randint(0,1)  # 0 = Left to right, 1 = Up down
        
        if (direction == 0) and (cruiser_positions[0][1] <= 3):
            enemymap[cruiser_positions[0][0]][cruiser_positions[0][1]] = "cr"
            for i in range(1,3):

                cruiser_positions[i] = [cruiser_positions[i-1][0], cruiser_positions[i-1][1] + 1]
                print(cruiser_positions[i][0])
                print(cruiser_positions[i][1])
                if (enemymap[cruiser_positions[i][0]][cruiser_positions[i][1]] != ''):
                    print("Enemy Grid Search Result: " + str(searchEnemyGrid(enemymap,"cr")))
                    define_cruiser_pos()
                else:
                    enemymap[cruiser_positions[i][0]][cruiser_positions[i][1]] = "cr"
        
            printEnemyMap()
        else:

            enemymap[cruiser_positions[0][0]][cruiser_positions[0][1]] = "cr"
            for i in range(1,3):

                cruiser_positions[i] = [cruiser_positions[i-1][0] + 1, cruiser_positions[0][1]]
                print(cruiser_positions[i][0])
                print(cruiser_positions[i][1])

                if (enemymap[cruiser_positions[i][0]][cruiser_positions[i][1]] != ''):
                    print("Enemy Grid Search Result: " + str(searchEnemyGrid(enemymap,"cr")))
                    define_cruiser_pos()
                else:
                    enemymap[cruiser_positions[i][0]][cruiser_positions[i][1]] = "cr"
        
            printEnemyMap()
        


def searchEnemyGrid(matrix, text):
    indexes = [index for index, v in enumerate(matrix) if v == text]
    print(indexes)
    return indexes

pgzrun.go()
