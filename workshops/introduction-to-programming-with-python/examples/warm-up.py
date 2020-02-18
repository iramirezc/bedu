import random
import simplegui

ALTO = 300
ANCHO = 400

posicion = [ANCHO / 2, ALTO / 2]
velocidad = [random.randrange(10), random.randrange(10)]

def dibujar(canvas):
    global posicion, velocidad

    canvas.draw_circle(posicion, 10, 1, "White", "White")
    posicion[0] += velocidad[0]
    posicion[1] += velocidad[1]
    
    if posicion[0] < 0 or posicion[0] > ANCHO:
        velocidad[0] = -velocidad[0]
    elif posicion[1] < 0 or posicion[1] > ALTO:
        velocidad[1] = -velocidad[1]

frame = simplegui.create_frame("Rebota", ANCHO, ALTO)
frame.set_draw_handler(dibujar)
frame.start()
