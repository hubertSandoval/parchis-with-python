import random
import numpy as np
from matplotlib import pyplot as plt
import easygui as gui


# Is the positios that the player will walk trough fron start to goal

p1_path = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
p2_path = [0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0]
p3_path = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0]
p4_path = [0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]



# Boards to set up the path of each player

board_for_p1 = np.array([
    [0,           p1_path[12], p1_path[11],   p1_path[10], 0],
    [p1_path[14], p1_path[13], 0,             p1_path[9],  p1_path[8]],
    [p1_path[15], p1_path[16], p1_path[17],   0,           p1_path[7]],
    [p1_path[0],  p1_path[1],  0,             p1_path[5],  p1_path[6]],
    [0,           p1_path[2],                 p1_path[3],  p1_path[4], 0]
])

board_for_p2 = np.array([
    [0,           p2_path[8],  p2_path[7],   p2_path[6], 0],
    [p2_path[10], p2_path[9],  0,            p2_path[5], p2_path[4]],
    [p2_path[11], 0,           p2_path[17],  0,          p2_path[3]],
    [p2_path[12], p2_path[13], p2_path[16],  p2_path[1], p2_path[2]],
    [0,           p2_path[14], p2_path[15],  p2_path[0], 0]
])

board_for_p3 = np.array([
    [0,          p3_path[4],  p3_path[3],  p3_path[2],  0 ],
    [p3_path[6], p3_path[5],  0,           p3_path[1],  p3_path[0]],
    [p3_path[7], 0 ,          p3_path[17], p3_path[16], p3_path[15]],
    [p3_path[8], p3_path[9],  0,           p3_path[13], p3_path[14]],
    [0,          p3_path[10], p3_path[11], p3_path[12], 0]
])

board_for_p4 = np.array([
    [0,          p4_path[0], p4_path[15],  p4_path[14], 0],
    [p4_path[2], p4_path[1], p4_path[16],  p4_path[13], p4_path[12]],
    [p4_path[3], 0,          p4_path[17],  0,           p4_path[11]],
    [p4_path[4], p4_path[5], 0,            p4_path[9],  p4_path[10]],
    [0,          p4_path[6], p4_path[7],   p4_path[8],  0]
])

board = board_for_p1 + board_for_p2 + board_for_p3 + board_for_p4

#plt.plot(board)
#plt.show()

# Jail positions before someone get 6 in dice and get out to start race to goal

p1_jail_position = board[4][0]
p2_jail_position = board[4][4]
p3_jail_position = board[0][4]
p4_jail_position = board[0][0]

# start position once the player got 6 in dice and can start race to goal

p1_position = board[3][3]
p2_position = board[4][3]
p3_position = board[1][4]
p4_position = board[0][1]


print(f"board for p1 is: \n{board_for_p1}")
print(f"board for p2 is: \n{board_for_p2}")
print(f"board for p3 is: \n{board_for_p3}")
print(f"board for p4 is: \n{board_for_p4}")

print("and the final board is: taraaaaaaaaan!")

gui.msgbox(msg=board, title="My first message box")


#print(board)

goal = board[2][2]

if goal == 1:
    print("jugador 1 gana")
elif goal == 2:
    print("jugador 2 gana")
elif goal == 3:
    print("jugador 3 gana")
elif goal == 4:
    print("jugador 4 gana")
else:
    print("no hay ganadores aun!")





def dice():
    """This is the dice that the players will roll"""
    dice_result = print(random.randint(1, 6))
    return dice_result

def greeting():
    greet = print("Hola, bienvenido al juego de parchis en python, \
quien saque el numero mas alto, tira primero. \
en caso de empate, tira quien primero lo saco")
    return greet


"""
roll_dice = input(str("Jugador 1, por favor pulsa 't' para tirar los dados: "))



if roll_dice.lower() == "t":
    dice()
else:
    print("por favor rueda los dados, lo que ingresaste no fue valido")

"""