list_of_numbers = []
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

tic_tac_toe_box()
