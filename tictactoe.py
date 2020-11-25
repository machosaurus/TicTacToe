
#MATRIX IS IN COLUMN-MAJOR.

def insertMove(player,move):

    if move[0]== '0': #================= FIRST COLUMN
        if move[1]== 'a':
            player[0][0] = 1
            gameboard[2]= gameboard[2][0:8] + player[4] + gameboard[2][9:len(gameboard[2])]
        elif move[1]== 'b':
            player[0][1] = 1
            gameboard[4]= gameboard[4][0:8] + player[4] + gameboard[4][9:len(gameboard[4])]
        elif move[1]== 'c':
            player[0][2] = 1
            gameboard[6]= gameboard[6][0:8] + player[4] + gameboard[6][9:len(gameboard[6])]
    elif move[0]=='1': #============= SECOND COLUMN
        if move[1]== 'a':
            player[1][0] = 1
            gameboard[2]= gameboard[2][0:12] + player[4] + gameboard[2][13:len(gameboard[2])]
        elif move[1]== 'b':
            player[1][1] = 1
            gameboard[4]= gameboard[4][0:12] + player[4] + gameboard[4][13:len(gameboard[4])]


        elif move[1]== 'c':
            player[1][2] = 1
            gameboard[6]= gameboard[6][0:12] + player[4] + gameboard[6][13:len(gameboard[6])]
    elif move[0]=='2': #============= THIRD COLUMN
        if move[1]== 'a':
            player[2][0] = 1
            gameboard[2]= gameboard[2][0:16] + player[4] + gameboard[2][17:len(gameboard[2])]
        elif move[1]== 'b':
            player[2][1] = 1
            gameboard[4]= gameboard[4][0:16] + player[4] + gameboard[4][17:len(gameboard[4])]
        elif move[1]== 'c':
            player[2][2] = 1
            gameboard[6]= gameboard[6][0:16] + player[4] + gameboard[6][17:len(gameboard[6])]

    #print('\n')
    for item in gameboard:
        print (item)
    
    #print(player)

def checkMove(move,player):
    
    if( ((move[0] == '0') or (move[0] =='1') or (move[0] =='2')) and ((move[1] == 'a') or (move[1]=='b') or (move[1]=='c')) ):

        x = int(move[0])
        n = move[1]
        if n == 'a':
            n = 0
        elif n == 'b':
            n = 1
        else:
            n = 2
        
        if player == 1:
            if player2[x][n] == 1:
                print("Swiper no Swiping! Choose A Free Space.")
                return False
        else:
            if player1[x][n] == 1:
                print("Thou Shalt Not Steal. Choose A Free Space.")
                return False

        return True
    else:    
        print("Invalid choice. Try again in column-major.")
        return False

def checkWin(player):
    #Checks All Columns
    if( (player[0][0]+ player[0][1]+ player[0][2] == 3) or (player[1][0]+ player[1][1]+ player[1][2] == 3) or (player[2][0]+ player[2][1]+ player[2][2] == 3)):
        print("\n===Congratulations! You Won! Look at you! You're Winning! You're Winning at Life!! ==========")
        return True;
    #checks All Rows
    elif( (player[0][0]+ player[1][0]+  player[2][0] == 3) or (player[0][1]+ player[1][1] + player[2][1] == 3) or (player[0][2]+ player[1][2]+  player[2][2] == 3)):
        print("=============Congratulations! You Won! Look at you! You're Winning at Life!! ===========")
        return True;
    #checks Diagonals
    elif( (player[0][0] + player[1][1] + player[2][2] == 3) or (player[2][0] + player[1][1] + player[0][2] == 3)):
        print("=============Congratulations! You Won! Look at you! You're Winning at Life!! ===========")
        return True;
    else:
        return False;

####################################################    
'''          board string:
print("        0   1   2   ")
print("       --- --- ---  ")
print("   a  |   |   |   | ")[2]   [8] [12] [16] 
print("       --- --- ---  ")
print("   b  |   |   |   | ")[4]     
print("       --- --- ---  ")
print("   c  |   |   |   | ")[6]   
print("       --- --- ---  ")
'''

boardStr = "\n        0   1   2  /       --- --- ---  /   a  |   |   |   |  /       --- --- ---  /   b  |   |   |   |  /       --- --- ---  /   c  |   |   |   |  /       --- --- ---  "
gameboard = boardStr.split("/")
player1 = [[0,0,0],[0,0,0],[0,0,0],1, 'X']
player2 = [[0,0,0],[0,0,0],[0,0,0],2, 'O']
gameOnBitchez = True
whoIsPlaying = 1
player = player1
counter = 0

print("\n\nIntitializing...........Tic Tac Toe")
for item in gameboard:
    print (item)

print("\n=========Game On=========")
while gameOnBitchez == True:
    #print("GOB: "+ str(gameOnBitchez))
    move = input("\nPlayer " + str(player[3]) +" (" + player[4]+"), Choose your move (#𝛼): ")

    boo = checkMove(move,player[3])
    if boo:
        insertMove(player,move)
        counter+=1
        thereIsWinner = checkWin(player);
        if thereIsWinner: 
            gameOnBitchez = False;

        if counter >=9:
            print("\nNo Winners. You both suck.\n:D Bye for now! Please Play again! <3~~~~~~~~~~~<")
            break
        if player[3] == 1: 
            player = player2;
        else:   
            player = player1;
        




        
'''=============================================================================
   if(  (player[0][0]+ player[0][1]+  player[0][2] == 3) or (player[1][0]+ player[1][1]+ player[1][2] == 3) or (player[2][0]+ player[2][1]+  player[2][2] == 3)):
        print("=============WIN==COLUMN===========")
    #checks All Rows
    elif(  (player[0][0]+ player[1][0]+  player[2][0] == 3) or (player[0][1]+ player[1][1]+ player[2][1] == 3) or (player[0][2]+ player[1][2]+  player[2][2] == 3)):
        print("=============WIN===ROW============")
    #checks Diagonals
    elif( ((player[0][0] and player[1][1] and  player[2][2]) == 3) or ((player[2][0] and player[1][1] and player[0][2]) == 3)):
        print("=============WIN===DIAGONAL==========")



        player1 = [['a','b','c'],['a','b','c'],['a','b','c'],1]
player2 = [['a','b','c'],['a','b','c'],['a','b','c'],2]

'''

