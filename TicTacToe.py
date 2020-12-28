import random
the_board=[' ']*10

def display_board():
    '''
    This Function prints out the board so the numpad can be used as a reference
    '''
    global the_board
    print("\n")
    print("  " + "  |   |   " )
    print ("  " + the_board[7] +" | " + the_board[8] +" | " + the_board[9] +"  " )
    print("  " + "  |   |   " )
    print("------------")
    print("  " + "  |   |   " )
    print ("  " + the_board[4] +" | " + the_board[5] +" | " + the_board[6] +"  " )
    print("  " + "  |   |   " )
    print("------------")
    print("  " + "  |   |   " )
    print ("  " + the_board[1] +" | " + the_board[2] +" | " + the_board[3] +"  " )
    print("  " + "  |   |   " )
 


def player_input():
    marker= ''
    while marker!='X' and marker !='O' :
        
        marker=input('Player1: Choose X or O: ').upper()
        
    if marker=="X":
        return ('X','O')
    else :
        return ('O','X')


def place_marker(board,mark,position):
    board[position]=mark
    


def win_check(board,mark):
    return ((board[7]==board[8]==board[9]==mark) or 
       (board[4]==board[5]==board[6]==mark) or 
       (board[1]==board[2]==board[3]==mark) or 
       (board[7]==board[4]==board[1]==mark) or 
       (board[8]==board[5]==board[2]==mark) or 
       (board[9]==board[6]==board[3]==mark) or 
       (board[7]==board[5]==board[3]==mark) or 
       (board[9]==board[5]==board[1]==mark))


def choose_first():
    flip=random.randint(0,1)
    
    if flip==0:
        return 'Player 1'
    else:
        return 'Player 2'


def space_check(board,position):
    return board[position]==' '



def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    
    return True


def player_choice(board):
    position =0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position) :
        position = int(input('Choose a position(1-9):'))
        
    return position



def replay():
    global the_board
    the_board=[' ']*10
    choice=input("Want to Play Again?(Yes/No)")
    return choice=="Yes"





print ("Welcome to Tic Tac Toe !!!")

while True:
    
    player1_marker,player2_marker=player_input()
    turn = choose_first()
    print(turn+' will go first')
    play_game=input("Ready to Play? Y or N?")
    
    if play_game=="Y":
        game_on=True
    else :
        game_on=False
    
    while game_on :
        if turn =="Player 1":
            display_board()
            position=player_choice(the_board)
            place_marker(the_board,player1_marker,position)
            
            if win_check(the_board,player1_marker):
                display_board()
                print("Player 1 has won!!!")
                game_on=False
            else:
                if full_board_check(the_board):
                    display_board()
                    print("Tie Game!!!")
                    game_on=False
                    
                else:
                    turn ="Player 2"
        
        else:
            display_board()
            position=player_choice(the_board)
            place_marker(the_board,player2_marker,position)
            
            if win_check(the_board,player2_marker):
                display_board()
                print("Player 2 has won!!!")
                game_on=False
            else:
                if full_board_check(the_board):
                    display_board()
                    print("Tie Game!!!")
                    game_on=False
                    
                else:
                    turn ="Player 1"
    
    if not replay():
        break
           