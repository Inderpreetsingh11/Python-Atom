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
            elif position in list_of_numbers:
                print('Position already selected. Select something else')
            else:
                list_of_numbers[position-1] = "X "
                list_of_selected_numbers.append(position)
                run = False
        except ValueError:
            print('Enter correct value')


print("Welcome to the Tic Tac Toe game")
tic_tac_toe_box()
choose_an_option()
