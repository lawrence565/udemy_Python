step = 0
row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]

def display(row1, row2, row3):
    print(row1)
    print(row2)
    print(row3)

def user_choice():
    choice = input("Please enter a number (1~9): ")
    while not choice.isdigit() or (int(choice) not in range(1, 10)):
        if not choice.isdigit():
            print("Sorry, your choice is not valid")
        else:
            print("Your choice is not in the range between 1 ~ 9")
        choice = input("Please enter a number (1~9): ")
    return int(choice)

def get_current_symbol():
    # while step < 9:
    #     if step % 2 == 0:
    #         return "O"
    #     elif step % 2 == 1:
    #         return "X"
    global step
    step += 1
    symbol_list = ["X", "O"]
    return symbol_list[step % 2]

def update_table(index):
    row = (index - 1) // 3 + 1
    col = (index - 1)  % 3
    
    if row == 1:
        if row1[col] == ' ':
            row1[col] = get_current_symbol()
            return True
        else:
            print("please try again")
            return False
    elif row == 2:
        if row2[col] == ' ':
            row2[col] = get_current_symbol()
            return True
        else:
            print("please try again")
            return False
    elif row == 3:
        if row3[col] == ' ':
            row3[col] = get_current_symbol()
            return True
        else:
            print("please try again")
            return False

def checking_win():
    player1_win = False
    player2_win = False
    if row1[0] == row1[1] == row1[2] and ' ' not in row1:
        if row1[0] == "O":
            player1_win = True
        else:
            player2_win = True
    elif row2[0] == row2[1] == row2[2] and ' ' not in row2:
        if row2[0] == "O":
            player1_win = True
        else:
            player2_win = True
    elif row3[0] == row3[1] == row3[2] and ' ' not in row3:
        if row3[0] == "O":
            player1_win = True
        else:
            player2_win = True
    elif row1[0] == row2[0] == row3[0] and (row1[0] != ' ' and row2[0] != ' ' and row3[0] != ' '):
        if row1[0] == "O":
            player1_win = True
        else:
            player2_win = True
    elif row1[1] == row2[1] == row3[1] and (row1[1] != ' ' and row2[1] != ' ' and row3[1] != ' '):
        if row1[1] == "O":
            player1_win = True
        else:
            player2_win = True
    elif row1[2] == row2[2] == row3[2] and (row1[2] != ' ' and row2[2] != ' ' and row3[2] != ' '):
        if row1[2] == "O":
            player1_win = True
        else:
            player2_win = True
    elif row1[0] == row2[1] == row3[2] and (row1[0] != ' ' and row2[1] != ' ' and row3[2] != ' '):
        if row1[0] == "O":
            player1_win = True
        else:
            player2_win = True
    elif row1[2] == row2[1] == row3[0] and (row1[2] != ' ' and row2[1] != ' ' and row3[0] != ' '):
        if row1[2] == "O":
            player1_win = True
        else:
            player2_win = True

    if player1_win:
        return "Player 1 wins"
    elif player2_win:
        return "Player 2 wins"
    else:
        return "No one wins"

def play():
    while True:
        display(row1, row2, row3)
        while True: 
            if update_table(user_choice()):
                break
            else:
                print("Wrong position")
    
        result = checking_win()
        if result == "Player 1 wins":
            display(row1, row2, row3)
            print("Player 1 wins!!! Congrats")
            return
        elif result == "Player 2 wins":
            display(row1, row2, row3)
            print("Player 1 wins!!! Congrats")
            return
        elif result == "No one wins" and step == 9:
            display(row1, row2, row3)
            print("Tie! There's no winner")
            return
            
    
play()