board=["","", "",
       "", "", "",
       "", "", ""]
def print_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    
    print(board[3] + "|" + board[4] + "|" + board[5])
    
    print(board[6] + "|" + board[7] + "|" + board[8])
print("Welcome to Tic Tac Toe!")
player="X"
for i in range(9):
    print_board()
    
    position=int(input("Enter position (1-9): "))-1
    if board[position]=="":
        board[position]=player
        
    else:
        print("Position already taken. Try again.")
        continue
    if (board[0]==board[1]==board[2]!="") or (board[3]==board[4]==board[5]!="") or (board[6]==board[7]==board[8]!="") or (board[0]==board[3]==board[6]!="") or (board[1]==board[4]==board[7]!="") or (board[2]==board[5]==board[8]!="") or (board[0]==board[4]==board[8]!="") or (board[2]==board[4]==board[6]!=""):
        print_board()
        print(player + " wins!")
        break
    if player=="X":
        player="O"
    else:  
        player="X"
        
else:  
    print_board()
    print("It's a tie!")
