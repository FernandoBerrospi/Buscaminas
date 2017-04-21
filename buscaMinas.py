__autor__ = "Fernando Berrospi"

#LIBRERIAS
from tkinter import *
from random import *
from tkinter import messagebox


#CONTANTES
color_line = '#24292e'
color_background = '#eaffea'
color_mine = '#C0392B'
color_save = '#99A3A4'
color_figure = '#154360'
width = 600
height = width
n = 6
interval = width/n

#VARIABLES
mines = []
difficulty = 4
number_clicks = 0
number_mines = 0

#METODOS
def print_mines():
    for i in range(n):
        for q in range(n):
            print('[',mines[q][i],']', end=" ")
        print(' ')
        
def create_grilla():
    for i in range(n):
        canvas.create_line(interval*i,0,interval*i,height,fill = color_line)
        canvas.create_line(0,interval*i,width,interval*i,fill = color_line)

def verify_state(i,q):
    if i >= 0 and q >= 0 and i < n and q < n:
        if mines[i][q] == -1:
            return 1
    return 0
def validator(i,q):
    acu = 0
    acu+= verify_state(i-1,q)
    acu+= verify_state(i-1,q+1)
    acu+= verify_state(i,q+1)
    acu+= verify_state(i+1,q+1)
    acu+= verify_state(i+1,q)
    acu+= verify_state(i+1,q-1)
    acu+= verify_state(i,q-1)
    acu+= verify_state(i-1,q-1)
    return acu

def create_matriz():
    global number_mines
    global mines
    mines = []
    for i in range(n):
        mines.append([])
        for q in range(n):
            mines[i].append(0)

    for i in range(n):
        for q in range(n):
            if randint(0,difficulty) == 1:
                mines[i][q] = -1
                number_mines+= 1

    for i in range(n):
        for q in range(n):
            if mines[i][q] != -1:
                mines[i][q] = validator(i,q)               
    print_mines()

def create_square(x,y,color):
    canvas.create_rectangle(x*interval,y*interval,(x+1)*interval,(y+1)*interval,fill=color)
    
def create_figure(x,y,char,color):
    canvas.create_text(x*interval+interval/2,y*interval+interval/2, text=char,anchor = CENTER,font=("Purisa", int(interval - 30)),fill = color)

def init_game():
    global number_mines
    global number_clicks
    canvas.create_rectangle(0,0,width,height,fill=color_background)
    number_clicks = 0
    number_mines = 0
    create_grilla()    
    create_matriz()
    
def show():
    for i in range(n):
        for q in range(n):
            if mines[i][q] == -1:
                create_square(i,q,color_mine)
                create_figure(i,q,':(',color_figure)
            else:
                create_square(i,q,color_save)
                create_figure(i,q,mines[i][q],color_figure)

#CONFIGURANDO LA VENTA DE LA APLICACION
window = Tk()
window.title("Busca Minas")
window.geometry(str(width)+'x'+str(height))
window.focus_set()
window.resizable(width=False, height=False)
window.iconbitmap('favicon.ico')

#PREPARACION DEL CANVAS
canvas = Canvas(window,height = height,width = width, bg = color_background)
canvas.pack(expand=YES, fill=BOTH)

#INICIAR JUEGO
init_game()

#PROPORCIONANDOS LOS CONROLADORES DEL EVENTO CLICK
def click(event):
    global number_mines
    global number_clicks
    
    #Obtenermos las posiciones segun la matriz de donde se hizo click
    x = int(event.x / interval)
    y = int(event.y / interval)
    number_clicks+= 1

    #print(number_clicks,number_mines)
    
    if mines[x][y] == -1:
        show()
        if messagebox.askquestion('Game Over','Reiniciaremos el Juego') == 'yes':
            init_game()
        else:
            window.destroy()
    else:
        if number_clicks == n*n - number_mines:
            if messagebox.askquestion('Felicitaciones','Ganaste el juego, quieres reiniciar') == 'yes':
                init_game()
            else:
                window.destroy()
        else:
            create_square(x,y,color_save)
            create_figure(x,y,mines[x][y],color_figure)

canvas.bind("<Button-1>", click)

mainloop()

