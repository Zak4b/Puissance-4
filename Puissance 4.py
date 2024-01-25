import P4
import tkinter
from tkinter import messagebox
win = tkinter.Tk()
taille_C = 100
width=7*taille_C
height=6*taille_C
win.minsize(width, height)
win.title("Puissance 4")
canvas=tkinter.Canvas(win, width=width, height=height+50)
canvas.pack()

canvas.create_rectangle(0,0,width,height, fill="#9c9c9c")
for i in range(8):
    canvas.create_line(i*taille_C,0,i*taille_C,height, fill="blue", width=5)
for i in range(7):
    canvas.create_line(0,i*taille_C,width,i*taille_C, fill="blue", width=5)

game = P4.P4()
PlayerClrs =["#000000","#FF0000", "#FFFF00"]
cursor = canvas.create_polygon([320.0, 630.0, 380.0, 630.0, 350.0, 610.0], outline="black", fill=PlayerClrs[game.cPlayer], width=2)

cList = []
def draw(color, x, y):
    c = canvas.create_oval(x*taille_C+5, height-(y*taille_C)-5, (x+1)*taille_C-5, height-((y+1)*taille_C-5), fill=color)
    cList.append(c)

def resetCanva():
    global cList
    game.__init__()
    for c in cList:
        canvas.delete(c)
    cList = []
    canvas.itemconfig(cursor, fill=PlayerClrs[game.cPlayer])
    x= int(canvas.coords(cursor)[0] //100) # 0-6 ->> 3
    canvas.move(cursor, 100*(3-x), 0)

def clic_canvas(event):
    i, j = event.x, event.y
    x, y= i//taille_C, j//taille_C 
    print(f"Click {i,j} -> c{x,y}")
    gPlay(x)

def move_cursor(event):
    x= int(canvas.coords(cursor)[0] //100)
    if event.keysym == "q" and x > 0:
        canvas.move(cursor, -100, 0)
    elif event.keysym == "d" and x < 6:
        canvas.move(cursor, 100, 0)
    elif event.keysym == "space":
        gPlay(x)

def gPlay(x):
    if game.win:
        return
    pid= game.cPlayer
    y= game.play(pid, x)
    if y<0:
        print("Forbiden")
    else:
        print(f"Play c{x,y}")
        draw(PlayerClrs[pid], x, y)
        canvas.itemconfig(cursor, fill=PlayerClrs[game.cPlayer])
        if(game.check(x,y)):
            messagebox.showinfo("Information", "This is an information message.")

resetCanva()
info_button = tkinter.Button(win, text="Reset", command=resetCanva)
info_button.pack()
canvas.bind("<Button-1>", clic_canvas)
canvas.bind("<KeyPress>", move_cursor)
canvas.focus_set()
win.mainloop()

