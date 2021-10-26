import time


player_turn = True
draw = False
win = False
lose = False
pos1 = "1"
pos2 = "2"
pos3 = "3"
pos4 = "4"
pos5 = "5"
pos6 = "6"
pos7 = "7"
pos8 = "8"
pos9 = "9"
pos1_att = 1
pos2_att = 1
pos3_att = 1
pos4_att = 1
pos5_att = 100
pos6_att = 1
pos7_att = 1
pos8_att = 1
pos9_att = 1


def board():
    print(" " + " | ".join([pos1, pos2, pos3]))
    print("___|___|___")
    print(" " + " | ".join([pos4, pos5, pos6]))
    print("___|___|___")
    print(" " + " | ".join([pos7, pos8, pos9]))


board()

while not win and not lose and not draw:
    while player_turn:
        player_input = str(input("Enter the number of a square: "))
        if player_input == "1" and pos1 == "1":
            pos1 = "X"
            player_turn = False
        elif player_input == "2" and pos2 == "2":
            pos2 = "X"
            player_turn = False
        elif player_input == "3" and pos3 == "3":
            pos3 = "X"
            player_turn = False
        elif player_input == "4" and pos4 == "4":
            pos4 = "X"
            player_turn = False
        elif player_input == "5" and pos5 == "5":
            pos5 = "X"
            player_turn = False
        elif player_input == "6" and pos6 == "6":
            pos6 = "X"
            player_turn = False
        elif player_input == "7" and pos7 == "7":
            pos7 = "X"
            player_turn = False
        elif player_input == "8" and pos8 == "8":
            pos8 = "X"
            player_turn = False
        elif player_input == "9" and pos9 == "9":
            pos9 = "X"
            player_turn = False
        else:
            print("Error: square taken or doesn't exist. ")

    wincase1 = [pos1, pos2, pos3]
    wincase2 = [pos4, pos5, pos6]
    wincase3 = [pos7, pos8, pos9]
    wincase4 = [pos1, pos4, pos7]
    wincase5 = [pos2, pos5, pos8]
    wincase6 = [pos3, pos6, pos9]
    wincase7 = [pos1, pos5, pos9]
    wincase8 = [pos3, pos5, pos7]

    board()

    if wincase1.count("X") == 3:
        win = True
    if wincase2.count("X") == 3:
        win = True
    if wincase3.count("X") == 3:
        win = True
    if wincase4.count("X") == 3:
        win = True
    if wincase5.count("X") == 3:
        win = True
    if wincase6.count("X") == 3:
        win = True
    if wincase7.count("X") == 3:
        win = True
    if wincase8.count("X") == 3:
        win = True

    if pos1 != "1" and pos2 != "2" and pos3 != "3" and pos4 != "4" and pos5 != "5" and pos6 != "6" and pos7 != "7" and pos8 != "8" and pos9 != "9" and not win:
        draw = True

# the machine attempts to win
    if not win and not draw:
        if wincase1.count("O") == 2 and wincase1.count("X") == 0:
            pos1_att = pos1_att + 1000
            pos2_att = pos2_att + 1000
            pos3_att = pos3_att + 1000

        if wincase2.count("O") == 2 and wincase2.count("X") == 0:
            pos4_att = pos4_att + 1000
            pos5_att = pos5_att + 1000
            pos6_att = pos6_att + 1000

        if wincase3.count("O") == 2 and wincase3.count("X") == 0:
            pos7_att = pos7_att + 1000
            pos8_att = pos8_att + 1000
            pos9_att = pos9_att + 1000

        if wincase4.count("O") == 2 and wincase4.count("X") == 0:
            pos1_att = pos1_att + 1000
            pos4_att = pos4_att + 1000
            pos7_att = pos7_att + 1000

        if wincase5.count("O") == 2 and wincase5.count("X") == 0:
            pos2_att = pos2_att + 1000
            pos5_att = pos5_att + 1000
            pos8_att = pos8_att + 1000

        if wincase6.count("O") == 2 and wincase6.count("X") == 0:
            pos3_att = pos3_att + 1000
            pos6_att = pos6_att + 1000
            pos9_att = pos9_att + 1000

        if wincase7.count("O") == 2 and wincase7.count("X") == 0:
            pos1_att = pos1_att + 1000
            pos5_att = pos5_att + 1000
            pos9_att = pos9_att + 1000

        if wincase8.count("O") == 2 and wincase8.count("X") == 0:
            pos3_att = pos3_att + 1000
            pos5_att = pos5_att + 1000
            pos7_att = pos7_att + 1000

        if wincase1.count("X") == 2 and wincase1.count("O") == 0:
            pos1_att = pos1_att + 500
            pos2_att = pos2_att + 500
            pos3_att = pos3_att + 500

        if wincase2.count("X") == 2 and wincase2.count("O") == 0:
            pos4_att = pos4_att + 500
            pos5_att = pos5_att + 500
            pos6_att = pos6_att + 500

        if wincase3.count("X") == 2 and wincase3.count("O") == 0:
            pos7_att = pos7_att + 500
            pos8_att = pos8_att + 500
            pos9_att = pos9_att + 500

        if wincase4.count("X") == 2 and wincase4.count("O") == 0:
            pos1_att = pos1_att + 500
            pos4_att = pos4_att + 500
            pos7_att = pos7_att + 500

        if wincase5.count("X") == 2 and wincase5.count("O") == 0:
            pos2_att = pos2_att + 500
            pos5_att = pos5_att + 500
            pos8_att = pos8_att + 500

        if wincase6.count("X") == 2 and wincase6.count("O") == 0:
            pos3_att = pos3_att + 500
            pos6_att = pos6_att + 500
            pos9_att = pos9_att + 500

        if wincase7.count("X") == 2 and wincase7.count("O") == 0:
            pos1_att = pos1_att + 500
            pos5_att = pos5_att + 500
            pos9_att = pos9_att + 500

        if wincase8.count("X") == 2 and wincase8.count("O") == 0:
            pos3_att = pos3_att + 500
            pos5_att = pos5_att + 500
            pos7_att = pos7_att + 500

        if wincase1.count("O") == 1 and wincase1.count("X") == 0:
            pos1_att = pos1_att + 10
            pos2_att = pos2_att + 10
            pos3_att = pos3_att + 10

        if wincase2.count("O") == 1 and wincase2.count("X") == 0:
            pos7_att = pos7_att + 10
            pos8_att = pos8_att + 10
            pos9_att = pos9_att + 10

        if wincase3.count("O") == 1 and wincase3.count("X") == 0:
            pos7_att = pos7_att + 10
            pos8_att = pos8_att + 10
            pos9_att = pos9_att + 10

        if wincase4.count("O") == 1 and wincase4.count("X") == 0:
            pos1_att = pos1_att + 10
            pos4_att = pos4_att + 10
            pos7_att = pos7_att + 10

        if wincase5.count("O") == 1 and wincase5.count("X") == 0:
            pos2_att = pos2_att + 10
            pos5_att = pos5_att + 10
            pos8_att = pos8_att + 10

        if wincase6.count("O") == 1 and wincase6.count("X") == 0:
            pos3_att = pos3_att + 10
            pos6_att = pos6_att + 10
            pos9_att = pos9_att + 10

        if wincase7.count("O") == 1 and wincase7.count("X") == 0:
            pos1_att = pos1_att + 10
            pos5_att = pos5_att + 10
            pos9_att = pos9_att + 10

        if wincase8.count("O") == 1 and wincase8.count("X") == 0:
            pos3_att = pos3_att + 10
            pos5_att = pos5_att + 10
            pos7_att = pos7_att + 10

        if wincase1.count("X") == 1 and wincase1.count("O") == 0:
            pos1_att = pos1_att + 1
            pos2_att = pos2_att + 1
            pos3_att = pos3_att + 1

        if wincase2.count("X") == 1 and wincase2.count("O") == 0:
            pos4_att = pos4_att + 1
            pos5_att = pos5_att + 1
            pos6_att = pos6_att + 1

        if wincase3.count("X") == 1 and wincase3.count("O") == 0:
            pos7_att = pos7_att + 1
            pos8_att = pos8_att + 1
            pos9_att = pos9_att + 1

        if wincase4.count("X") == 1 and wincase4.count("O") == 0:
            pos1_att = pos1_att + 1
            pos4_att = pos4_att + 1
            pos7_att = pos7_att + 1

        if wincase5.count("X") == 1 and wincase5.count("O") == 0:
            pos2_att = pos2_att + 1
            pos5_att = pos5_att + 1
            pos8_att = pos8_att + 1

        if wincase6.count("X") == 1 and wincase6.count("O") == 0:
            pos3_att = pos3_att + 1
            pos6_att = pos6_att + 1
            pos9_att = pos9_att + 1

        if wincase7.count("X") == 1 and wincase7.count("O") == 0:
            pos1_att = pos1_att + 1
            pos5_att = pos5_att + 1
            pos9_att = pos9_att + 1

        if wincase8.count("X") == 1 and wincase8.count("O") == 0:
            pos3_att = pos3_att + 1
            pos5_att = pos5_att + 1
            pos7_att = pos7_att + 1

        if pos1 == "X" or pos1 == "O":
            pos1_att = 0

        if pos2 == "X" or pos2 == "O":
            pos2_att = 0

        if pos3 == "X" or pos3 == "O":
            pos3_att = 0

        if pos4 == "X" or pos4 == "O":
            pos4_att = 0

        if pos5 == "X" or pos5 == "O":
            pos5_att = 0

        if pos6 == "X" or pos6 == "O":
            pos6_att = 0

        if pos7 == "X" or pos7 == "O":
            pos7_att = 0

        if pos8 == "X" or pos8 == "O":
            pos8_att = 0

        if pos9 == "X" or pos9 == "O":
            pos9_att = 0

        point_values = [pos1_att, pos2_att, pos3_att, pos4_att, pos5_att, pos6_att, pos7_att, pos8_att, pos9_att]
        point_values.sort()
        time.sleep(.75)

        if point_values[-1] == pos1_att:
            pos1 = "O"

        elif point_values[-1] == pos2_att:
            pos2 = "O"

        elif point_values[-1] == pos3_att:
            pos3 = "O"

        elif point_values[-1] == pos4_att:
            pos4 = "O"

        elif point_values[-1] == pos5_att:
            pos5 = "O"

        elif point_values[-1] == pos6_att:
            pos6 = "O"

        elif point_values[-1] == pos7_att:
            pos7 = "O"

        elif point_values[-1] == pos8_att:
            pos8 = "O"

        elif point_values[-1] == pos9_att:
            pos9 = "O"

        wincase1 = [pos1, pos2, pos3]
        wincase2 = [pos4, pos5, pos6]
        wincase3 = [pos7, pos8, pos9]
        wincase4 = [pos1, pos4, pos7]
        wincase5 = [pos2, pos5, pos8]
        wincase6 = [pos3, pos6, pos9]
        wincase7 = [pos1, pos5, pos9]
        wincase8 = [pos3, pos5, pos7]

        if wincase1.count("O") == 3:
            lose = True
        if wincase2.count("O") == 3:
            lose = True
        if wincase3.count("O") == 3:
            lose = True
        if wincase4.count("O") == 3:
            lose = True
        if wincase5.count("O") == 3:
            lose = True
        if wincase6.count("O") == 3:
            lose = True
        if wincase7.count("O") == 3:
            lose = True
        if wincase8.count("O") == 3:
            lose = True

        print("Computer's turn: ")
        board()

        pos1_att = 1
        pos2_att = 1
        pos3_att = 1
        pos4_att = 1
        pos5_att = 100
        pos6_att = 1
        pos7_att = 1
        pos8_att = 1
        pos9_att = 1

        player_turn = True

if win:
    print("Congratulations! You win!")
elif draw:
    print("It's a draw!")
else:
    print("You lose! Better luck next time!")
