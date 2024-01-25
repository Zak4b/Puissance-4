import P4
game = P4.P4()

def gPlay(x):
    if game.win:
        return
    pid= game.cPlayer
    y= game.play(pid, x)
    if y<0:
        print("Forbiden")
    else:
        print(f"Play c{x,y}")
        if(game.checkLast()):
            print("C'est gagné.")

while True:
    game.print()
    x = input("0-6")
    gPlay(int(x))