import random

list_of_numbers = []
list_of_selected_numbers =[]
for i in range(9):
    list_of_numbers.append("  ")


def tic_tac_toe_box():
    print("      |    |     ")
    print("      |    |     ")
    print("  {}  | {} |   {}  ".format(list_of_numbers[0],list_of_numbers[1],list_of_numbers[2]))
    print("      |    |     ")
    print("-----------------")
    print("      |    |     ")
    print("      |    |     ")
    print("  {}  | {} |   {}  ".format(list_of_numbers[3],list_of_numbers[4],list_of_numbers[5]))
    print("      |    |     ")
    print("-----------------")
    print("      |    |     ")
    print("      |    |     ")
    print("  {}  | {} |   {}  ".format(list_of_numbers[6],list_of_numbers[7],list_of_numbers[8]))
    print("      |    |     ")
    print("-----------------")

def choose_an_option():
    run = True
    while run:
        try:
            position = int(input("Choose position (1-9)"))
            if position not in range(1,10):
                print('Enter value between 1-9')
            elif position in list_of_selected_numbers:
                print('Position already selected. Select something else')
            else:
                list_of_numbers[position-1] = "X "
                list_of_selected_numbers.append(position)
                run = False
        except ValueError:
            print('Enter correct value')

def AI_move():
    run = True
    while(run):
        if len(list_of_selected_numbers) !=9:
            number = random.choice(range(1,10))
            if number not in list_of_selected_numbers:
                list_of_numbers[number-1] = "O "
                list_of_selected_numbers.append(number)
                print(number)
                run = False
        else:
            break

def Winner():
    if (list_of_numbers[0] == list_of_numbers[1] == list_of_numbers[2] == 'X ')or(list_of_numbers[3] == list_of_numbers[4] == list_of_numbers[5] == 'X ')or(list_of_numbers[6] == list_of_numbers[7] == list_of_numbers[8] == 'X ')or(list_of_numbers[0] == list_of_numbers[3] == list_of_numbers[6] == 'X ')or(list_of_numbers[1] == list_of_numbers[4] == list_of_numbers[7] == 'X ')or(list_of_numbers[2] == list_of_numbers[5] == list_of_numbers[8] == 'X ')or(list_of_numbers[0] == list_of_numbers[4] == list_of_numbers[8] == 'X ')or(list_of_numbers[2] == list_of_numbers[4] == list_of_numbers[6] == 'X ')or(list_of_numbers[0] == list_of_numbers[1] == list_of_numbers[2] == 'O ')or(list_of_numbers[3] == list_of_numbers[4] == list_of_numbers[5] == 'O ')or(list_of_numbers[6] == list_of_numbers[7] == list_of_numbers[8] == 'O ')or(list_of_numbers[0] == list_of_numbers[3] == list_of_numbers[6] == 'O ')or(list_of_numbers[1] == list_of_numbers[4] == list_of_numbers[7] == 'O ')or(list_of_numbers[2] == list_of_numbers[5] == list_of_numbers[8] == 'O ')or(list_of_numbers[0] == list_of_numbers[4] == list_of_numbers[8] == 'O ')or(list_of_numbers[2] == list_of_numbers[4] == list_of_numbers[6] == 'O '):
        xyz = True
        print('We got a winner!!')
        return xyz
    elif len(list_of_selected_numbers) == 9:
        print("It's a Tie")
        xyz = True
        return xyz
    else:
        xyz = False
        return xyz



print("Welcome to the Tic Tac Toe game")
print("The user's symbol will be 'X'")
print("The computer's symbol will be 'O'")
tic_tac_toe_box()
while 1 == 1:
    choose_an_option()
    AI_move()
    tic_tac_toe_box()
    if Winner() == True:
        break
