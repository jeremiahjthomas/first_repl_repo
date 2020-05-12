#jerryT21
#jeremiah thomas
from pprint import pprint as pp
import random
import sys
import time
import pygame

time.sleep(1)
print("~ Jerry T presents... ~")
time.sleep(1)
print("- ARCADE -")
print("")
time.sleep(1)
print("Play Games Ranging from ~")

time.sleep(1)
print("Rock Paper Scissors [rp]")
time.sleep(0.5)
print("Hangman [h]")
time.sleep(0.5)
print("Tic Tac Toe [ttt]")
time.sleep(0.5)
print("Connect Four [cf]")
time.sleep(0.5)
print("Heads or Tails [ht]")
time.sleep(0.5)
print("Battleship [bs]")
time.sleep(1)
print("....btw one game is hidden. See if you can find it!!!")
time.sleep(1.5)
print("")
print("")
print("So... which game will it be? e.g: [ht]")
print("")

oogaboogagame_chosen = str(input(""))

while oogaboogagame_chosen == "rps":

    print("Let's Play Rock Paper Scissors!")
    print("")
    time.sleep(1)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("")
    # get user option
    print("Rock, Paper, or Scissors?")
    print("")
    userOption = input()

    # set computer's value
    rps = ["Rock", "Paper", "Scissors"]
    computer_choice = rps[random.randint(0, 2)]
    print(computer_choice)
    print("")

    # decide who wins

    # Computer Wins
    if userOption == "Rock" and computer_choice == "Paper":
        time.sleep(1)
        print("User:", userOption, "Computer:", computer_choice)
        time.sleep(1)
        print("Computer Wins")
    if userOption == "Paper" and computer_choice == "Scissors":
        time.sleep(1)
        print("User:", userOption, "Computer:", computer_choice)
        time.sleep(1)
        print("Computer Wins")
    if userOption == "Scissors" and computer_choice == "Rock":
        time.sleep(1)
        print("User:", userOption, "Computer:", computer_choice)
        time.sleep(1)
        print("Computer Wins")
    # User Wins
    if userOption == "Rock" and computer_choice == "Scissors":
        time.sleep(1)
        print("User:", userOption, "Computer:", computer_choice)
        time.sleep(1)
        print("User Wins")
    if userOption == "Paper" and computer_choice == "Rock":
        time.sleep(1)
        print("User:", userOption, "Computer:", computer_choice)
        time.sleep(1)
        print("User Wins")
    if userOption == "Scissors" and computer_choice == "Paper":
        time.sleep(1)
        print("User:", userOption, "Computer:", computer_choice)
        time.sleep(1)
        print("User Wins")
    # decide if tie
    if userOption == "Rock" and computer_choice == "Rock":
        time.sleep(1)
        print("User:", userOption, "Computer:", computer_choice)
        time.sleep(1)
        print("Tie")
    if userOption == "Paper" and computer_choice == "Paper":
        time.sleep(1)
        print("User:", userOption, "Computer:", computer_choice)
        time.sleep(1)
        print("Tie")
    if userOption == "Scissors" and computer_choice == "Scissors":
        time.sleep(1)
        print("User:", userOption, "Computer:", computer_choice)
        time.sleep(1)
        print("Tie")

while oogaboogagame_chosen == 'h':
    print("")
    time.sleep(0.5)
    print("")
    time.sleep(0.5)
    print("~~HANGMAN~~")
    print("")
    print("")

    # lets set some variables
    wordList = [
        "lion", "umbrella", "window", "computer", "glass", "juice", "chair", "desktop",
        "laptop", "dog", "cat", "lemon", "cabel", "mirror", "hat"
    ]

    guess_word = []
    secretWord = random.choice(wordList)  # lets randomize single word from the list
    length_word = len(secretWord)
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    letter_storage = []


    def change():

        for character in secretWord:  # printing blanks for each letter in secret word
            guess_word.append("-")

        print("Welcome to hangman by Jeremiah. I have a word for you to guess. It is", length_word, "characters")

        print("You are only allowed to enter a letter from a-z\n\n")

        print(guess_word)


    def guessing():
        guess_taken = 1

        while guess_taken < 10:

            guess = input("Pick a letter\n").lower()

            if not guess in alphabet:  # checking input
                print("Enter a letter from a-z alphabet")
            elif guess in letter_storage:  # checking if letter has been already used
                print("You have already guessed that letter!")
            else:

                letter_storage.append(guess)
                if guess in secretWord:
                    print("You guessed correctly!")
                    for x in range(0, length_word):  # This Part I just don't get it
                        if secretWord[x] == guess:
                            guess_word[x] = guess
                            print(guess_word)

                    if not '-' in guess_word:
                        print("You won!")
                        break
                else:
                    print("The letter is not in the word. Try Again!")
                    guess_taken += 1
                    if guess_taken == 10:
                        print(" ou lost!!! The secret word was", secretWord)


    change()
    guessing()

    print("Game Over!")

while oogaboogagame_chosen == "ttt":
    board = [i for i in range(0, 9)]
    player, computer = '', ''

    # Corners, Center and Others, respectively
    moves = ((1, 7, 3, 9), (5,), (2, 4, 6, 8))
    # Winner combinations
    winners = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    # Table
    tab = range(1, 10)


    def print_board():
        x = 1
        for i in board:
            end = ' | '
            if x % 3 == 0:
                end = ' \n'
                if i != 1: end += '---------\n';
            char = ' '
            if i in ('X', 'O'): char = i;
            x += 1
            print(char, end=end)


    def select_char():
        chars = ('X', 'O')
        if random.randint(0, 1) == 0:
            return chars[::-1]
        return chars


    def can_move(brd, player, move):
        if move in tab and brd[move - 1] == move - 1:
            return True
        return False


    def can_win(brd, player, move):
        places = []
        x = 0
        for i in brd:
            if i == player: places.append(x);
            x += 1
        win = True
        for tup in winners:
            win = True
            for ix in tup:
                if brd[ix] != player:
                    win = False
                    break
            if win == True:
                break
        return win


    def make_move(brd, player, move, undo=False):
        if can_move(brd, player, move):
            brd[move - 1] = player
            win = can_win(brd, player, move)
            if undo:
                brd[move - 1] = move - 1
            return (True, win)
        return (False, False)


    # AI goes here
    def computer_move():
        move = -1
        # If I can win, others don't matter.
        for i in range(1, 10):
            if make_move(board, computer, i, True)[1]:
                move = i
                break
        if move == -1:
            # If player can win, block him.
            for i in range(1, 10):
                if make_move(board, player, i, True)[1]:
                    move = i
                    break
        if move == -1:
            # Otherwise, try to take one of desired places.
            for tup in moves:
                for mv in tup:
                    if move == -1 and can_move(board, computer, mv):
                        move = mv
                        break
        return make_move(board, computer, move)


    def space_exist():
        return board.count('X') + board.count('O') != 9


    player, computer = select_char()
    print('Player is [%s] and computer is [%s]' % (player, computer))
    result = '%%% Deuce ! %%%'
    while space_exist():
        print_board()
        print('# Make your move ! [1-9] : ', end='')
        move = int(input())
        moved, won = make_move(board, player, move)
        if not moved:
            print(' >> Invalid number ! Try again !')
            continue
        #
        if won:
            result = '*** Congratulations ! You won ! ***'
            break
        elif computer_move()[1]:
            result = '=== You lose ! =='
            break;

    print_board()
    print(result)
while oogaboogagame_chosen == "cf":
    grid1 = [0, 0, 0, 0]  # bottom row
    grid2 = [0, 0, 0, 0]
    grid3 = [0, 0, 0, 0]
    grid4 = [0, 0, 0, 0]

    grids = [grid1, grid2, grid3, grid4]

    check = []

    user = 1


    class fullSlot_error(Exception):
        pass


    def hasWon_def():
        print("player " + str(user) + " has won")
        time.sleep(1)


    def grid_def():
        print("", grid4, "\n", grid3, "\n", grid2, "\n", grid1)


    def user_def():
        global user
        if user < 2:
            user = 2
        else:
            user = 1
        return user


    def slotFull_def():
        while True:
            try:
                if grid4[userInput - 1] != 0:
                    raise fullSlot_error
                else:
                    break
            except fullSlot_error:
                print("slot is full try again")
                confirm_def()


    def confirm_def():
        looop = True
        while looop == True:
            try:
                global userInput
                userInput = int(input("\ninput a slot player " + str(user) + "(1,4)\n"))
                if userInput < 5 and 0 < userInput:
                    looop = False
                else:
                    print("invalid int")
            except ValueError:
                print("invalid input")


    def placement_def():
        counter = 0
        for i in range(0, 4):
            slotFull_def()
            if (grids[i][userInput - 1] == 0):
                grids[i][userInput - 1] = int(user)
                grid_def()
                break


    def check_def():
        global loop
        global check
        for i in range(0, 4):
            for a in range(0, 4):
                check.append(grids[i][a])
            if (check == [1, 1, 1, 1] or check == [2, 2, 2, 2]):
                hasWon_def()
                loop = False
                return loop
                break
            else:
                check = []
        for i in range(0, 4):
            for a in range(0, 4):
                check.append(grids[a][i])
            if (check == [1, 1, 1, 1] or check == [2, 2, 2, 2]):
                hasWon_def()
                loop = False
                return loop
                break
            else:
                check = []


    def checkEmpty_def():
        global check
        for i in range(0, 4):
            for a in range(0, 4):
                check.append(grids[i][a])
        if 0 not in check:
            print("full")


    def checks_def():
        check_def()
        checkEmpty_def()
        diagcheck_def()


    def diagcheck_def():
        global loop
        global check
        check = []
        diag = 0
        for i in range(0, 4):
            check.append(grids[diag][diag])
            diag = diag + 1
            if (check == [1, 1, 1, 1] or check == [2, 2, 2, 2]):
                hasWon_def()
                loop = False
                return loop
                break
        check = []
        diag = 3
        diag2 = 0
        for i in range(0, 4):
            check.append(grids[diag][diag2])
            if (check == [1, 1, 1, 1] or check == [2, 2, 2, 2]):
                hasWon_def()
                loop = False
                return loop
                break


    loop = True

    while loop == True:
        check_def()
        confirm_def()
        placement_def()
        checks_def()
        if loop == False:
            break
        user_def()
while oogaboogagame_chosen == "ht":
    print("")
    print("Time to Play Heads or Tails")
    time.sleep(1)

    time.sleep(1)
    print("")
    playerOne = input("Player One. Heads or Tails? ")
    print("")

    if playerOne == "Heads":
        print("Player 1 - Heads")
        time.sleep(1)
        print("Player Two = Tails")

    if playerOne == "Tails":
        print("Player 1 - Tails")
        time.sleep(1)
        print("Player 2 = Heads")

    coin_choose = ["Heads", "Tails"]
    hot = random.randint(0, 1)
    pick = coin_choose[hot]

    if str(pick) == str(playerOne):
        print("")
        print("Player One wins with", pick)

    if str(pick) != str(playerOne):
        print("")
        print("Player Two wins with", pick)

while oogaboogagame_chosen == "bs":
    Rows = 0
    Columns = 0
    turns = 0
    Answer = "NaN"

    print("Time to Play Battleship!")
    print("")
    while (Rows > 10) or (Columns > 10) or (Rows <= 0) or (Columns <= 0):
        Rows = int(input("Please enter the number of rows you want. \n"))
        Columns = int(input("Please enter the number of columns you want. \n"))


    def create_grid(Rows, Columns):
        # Creates the 2D Data Grid
        grid = []
        for row in range(Rows):
            row = []
            for col in range(Columns):
                row.append(' ')
            grid.append(row)
        return grid


    grid = create_grid(Rows, Columns)


    def display_grid(grid, Columns):
        # Prints the labels for the grid
        column_names = 'abcdefghijklmnopqrstuvwxyz'[:Columns]
        print('  | ' + ' | '.join(column_names.upper()) + ' |')
        for number, row in enumerate(grid):
            print(number + 1, '| ' + ' | '.join(row) + ' |')


    grid = create_grid(Rows, Columns)
    display_grid(grid, Columns)


    def random_row(grid):
        # Makes a random row integer
        return random.randint(1, len(grid))


    def random_col(grid):
        # Makes a random column integer
        return random.randint(1, len(grid[0]))


    def update_gridHit(grid, GuessRow, GuessColumn):
        grid[GuessRow - 1][GuessColumn - 1] = 'O'


    def update_gridMiss(grid, GuessRow, GuessColumn):
        grid[GuessRow - 1][GuessColumn - 1] = 'X'


    ShipRow = random_row(grid)
    ShipColumn = random_col(grid)

    # Testing purposes only, comment out if needed.
    print(ShipRow)
    print(ShipColumn)

    while (turns != 5):
        GuessRow = int(input("What row do you guess? \n"))
        GuessColumn = int(input("What column do you guess? \n"))

        if (GuessRow == ShipRow) and (GuessColumn == ShipColumn):
            turns += 1
            update_gridHit(grid, GuessRow, GuessColumn)
            display_grid(grid, Columns)
            print("You hit the battleship! Congratulations!")
            break

        else:
            if (GuessRow < 1 or GuessRow > Rows) or (GuessColumn < 1 or GuessColumn > Columns):
                # Warning if the guess is out of the board
                print("Outside the set grid. Please pick a number within it your Rows and Columns.")

            elif (grid[GuessRow - 1][GuessColumn - 1] == "X"):
                # If "X" is there than print that it missed
                print("You guessed that already.")

            else:
                # Updates the grid with an "X" saying that you missed the ship
                turns += 1
                print("You missed the ship.")
                update_gridMiss(grid, GuessRow, GuessColumn)
                display_grid(grid, Columns)

        if (turns >= 5):
            print("Game over! You ran out of tries")

## so you looked at the code to figure out what the hidden game is...

while oogaboogagame_chosen == "snake":


    pygame.init()

    white = (255, 255, 255)
    yellow = (255, 255, 102)
    black = (0, 0, 0)
    red = (213, 50, 80)
    green = (0, 255, 0)
    blue = (50, 153, 213)

    dis_width = 600
    dis_height = 400

    dis = pygame.display.set_mode((dis_width, dis_height))
    pygame.display.set_caption('Snake Game by Edureka')

    clock = pygame.time.Clock()

    snake_block = 10
    snake_speed = 15

    font_style = pygame.font.SysFont("bahnschrift", 25)
    score_font = pygame.font.SysFont("comicsansms", 35)


    def Your_score(score):
        value = score_font.render("Your Score: " + str(score), True, yellow)
        dis.blit(value, [0, 0])


    def our_snake(snake_block, snake_list):
        for x in snake_list:
            pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])


    def message(msg, color):
        mesg = font_style.render(msg, True, color)
        dis.blit(mesg, [dis_width / 6, dis_height / 3])


    def gameLoop():
        game_over = False
        game_close = False

        x1 = dis_width / 2
        y1 = dis_height / 2

        x1_change = 0
        y1_change = 0

        snake_List = []
        Length_of_snake = 1

        foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

        while not game_over:

            while game_close == True:
                dis.fill(blue)
                message("You Lost! Press C-Play Again or Q-Quit", red)
                Your_score(Length_of_snake - 1)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = True
                            game_close = False
                        if event.key == pygame.K_c:
                            gameLoop()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x1_change = -snake_block
                        y1_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x1_change = snake_block
                        y1_change = 0
                    elif event.key == pygame.K_UP:
                        y1_change = -snake_block
                        x1_change = 0
                    elif event.key == pygame.K_DOWN:
                        y1_change = snake_block
                        x1_change = 0

            if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
                game_close = True
            x1 += x1_change
            y1 += y1_change
            dis.fill(blue)
            pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
            snake_Head = []
            snake_Head.append(x1)
            snake_Head.append(y1)
            snake_List.append(snake_Head)
            if len(snake_List) > Length_of_snake:
                del snake_List[0]

            for x in snake_List[:-1]:
                if x == snake_Head:
                    game_close = True

            our_snake(snake_block, snake_List)
            Your_score(Length_of_snake - 1)

            pygame.display.update()

            if x1 == foodx and y1 == foody:
                foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                Length_of_snake += 1

            clock.tick(snake_speed)

        pygame.quit()
        quit()


    gameLoop()



