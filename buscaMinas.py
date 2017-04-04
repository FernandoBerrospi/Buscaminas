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
width = 600
height = width
n = 10
interval = width/n

#VARIABLES
mines = []

#METODOS
def create_grilla():
    for i in range(n):
        canvas.create_line(interval*i,0,interval*i,height,fill = color_line)
        canvas.create_line(0,interval*i,width,interval*i,fill = color_line)

def create_matriz():
    if len(mines)>0:
        for i in range(n):
            mines[i] = []
    for i in range(n):
        mines.append([])
        for q in range(n):
            mines[i].append(randint(0, 1))
    print(mines)

def create_square(x,y,color):
    canvas.create_rectangle(x*interval,y*interval,(x+1)*interval,(y+1)*interval,fill=color)

def init_game():
    canvas.create_rectangle(0,0,width,height,fill=color_background)
    create_grilla()    
    create_matriz()
def show():
    for i in range(n):
        for q in range(n):
            if mines[i][q]:
                create_square(i,q,color_mine)
            else:
                create_square(i,q,color_save)

#CONFIGURANDO LA VENTA DE LA APLICACION
window = Tk()
window.title("Busca Minas")
window.geometry(str(width)+'x'+str(height))
window.focus_set()

#PREPARACION DEL CANVAS
canvas = Canvas(height = height,width = width, bg = color_background)
canvas.pack(expand=YES, fill=BOTH)

#INICIAR JUEGO
init_game()

#PROPORCIONANDOS LOS CONROLADORES DEL EVENTO CLICK
def click(event):
    #Obtenermos las posiciones segun la matriz de donde se hizo click
    x = int(event.x / interval)
    y = int(event.y / interval)

    if mines[x][y] == 1:
        show()
        if messagebox.askquestion('Game Over','Reiniciaremos el Juego') == 'yes':
            init_game()
        else:
            window.destroy()
    else:
        create_square(x,y,color_save)

canvas.bind("<Button-1>", click)

