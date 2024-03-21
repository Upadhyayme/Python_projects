field = ['1', '2', '3',
         '4', '5', '6',
         '7', '8', '9']

current_player = 1
players = {'x', 'o'}
for player in players:
    def check(field):
        if(field[0] == player and field[1] == player and field[2] == player):
            print("player 1 wins")
        if(field[3] == player and field[4] == player and field[5] == player):
            print("player 1 wins")
        if(field[6] == player and field[7] == player and field[8] == player):
            print("player 1 wins")
        if(field[0] == player and field[3] == player and field[6] == player):
            print("player 1 wins")
        if(field[1] == player and field[4] == player and field[8] == player):
            print("player 1 wins")
        if(field[2] == player and field[5] == player and field[8] == player):
            print("player 1 wins")
        if(field[0] == player and field[4] == player and field[8] == player):
            print("player 1 wins")
        if(field[2] == player and field[4] == player and field[6] == player):
            print("player 1 wins")    

def draw(field):
    print(f"{field[0]} {field[1]} {field[2]}")
    print(f"{field[3]} {field[4]} {field[5]}")
    print(f"{field[6]} {field[7]} {field[8]}")
    print("\n")
draw(field)

while True:
    x = input(f"Player {current_player}, where to place? ")
    x = int(x)
    
    if current_player==1:
        field[x-1] = 'x'
        current_player = 2
    else:
        field[x-1] = 'o'
        current_player = 1
    check(field)
    draw(field)