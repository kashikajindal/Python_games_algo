import random

board = [' ' for _ in range(10)]

def printboard(board):
    print('   |   |   ')
    print(' '+ board[1] + ' | ' + board[2] + ' |  ' + board[3])
    print('   |   |   ')
    print("------------")
    print('   |   |   ')
    print(' '+ board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |   ')
    print("------------")
    print('   |   |   ')
    print(' '+ board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |   ')
    
    


def isWinner(b,symbol):
    return (b[1] == symbol and b[2] == symbol and b[3] == symbol) or\
           (b[4] == symbol and b[5] == symbol and b[6] == symbol) or\
           (b[7] == symbol and b[8] == symbol and b[9] == symbol) or\
           (b[1] == symbol and b[4] == symbol and b[7] == symbol) or\
           (b[2] == symbol and b[5] == symbol and b[8] == symbol) or\
           (b[3] == symbol and b[6] == symbol and b[9] == symbol) or\
           (b[1] == symbol and b[5] == symbol and b[9] == symbol) or\
           (b[3] == symbol and b[5] == symbol and b[7] == symbol)
           
def spaceFree(board,position):
            return board[position]==' ' 

def insertLetter(board,symbol,position):
            board[position] = symbol
            printboard(board)
            
def playerMove(symbol):
    run=True
    while run:
        try:
            move = int(input(f"Player ({symbol}) , Please a number between 1 to 9 : "))
            if(move>0 and move<9):
                 if spaceFree(board,move):
                     run = False
                     insertLetter(board,symbol,move)
                 else:
                     print("Sorry, this space is already occupied choose another")
            else:
                print("Please enter a number between 1 to 9")  
        except ValueError:
            print("The entered value should be a number")
            
def AIMove(symbol):
    run = True
    while run:
         move = random.choice([i for i in range(1,10) if board[i]==' '])
         if move:
             insertLetter(board,symbol,move)
             run = False
             print(f"AI ({symbol}) placed at postion {move}")
         else:
             print("space already occupied")
             break
         
def startGame():
    playerSymbol = "X"
    AISymbol = "O"
    
    printboard(board)

    for turn in range(0,9):
      if turn%2==0:
        playerMove(playerSymbol)
      else:
          AIMove(AISymbol)
          
      if isWinner(board,playerSymbol):
          print("Player is Winner")
          break
      elif isWinner(board,AISymbol):
          print("AI is Winner")
          break
      elif turn == 8:
          print("It is a tie")
          break
      
if __name__ == "__main__":
    startGame( )
        