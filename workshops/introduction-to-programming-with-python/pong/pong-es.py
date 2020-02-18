# Pong
#
# Author: Isaac Ramírez
#
# Última modificación: 16/Feb/2020
#
# Descripción: Pong es un videojuego arcade de tenis desarrollado
# por Atari en 1972.
# 
# Próposito: Este mini juego tiene como objetivo ser una introducción a los
# fundamentos de programación con Python con la intención de despertar el
# interés sobre cómo funcionan los programas y videojuegos que usamos todos
# los días.

# Importación de librerías
import simplegui
import random

# Variables globales:
# canvas
ANCHO_CANCHA = 600
ALTO_CANCHA = 400

# pads
ANCHO_PADS = 8
ALTO_PADS = 80
MITAD_ANCHO_PADS = ANCHO_PADS / 2
MITAD_ALTO_PADS = ALTO_PADS / 2

# bola
RADIO_BOLA = 20


# Función que dibuja la bola en el centro de la cancha
# y la lanza a la izquierda o derecha.
def lanzar_bola(direccion):
    # vel_bola y pos_bola son vectores [x, y]
    global vel_bola, pos_bola

    # la posición incial de la bola es el centro de la cancha
    pos_bola = [ANCHO_CANCHA / 2, ALTO_CANCHA / 2]

    # escoger una velocidad aleatoria
    x = random.randrange(120, 240) / 40
    y = random.randrange(60, 180) / 40

    # si la direccion es a la derecha
    if direccion == 'DERECHA':
        # velocidad hacia la esquina superior derecha
        vel_bola = [x, -y]
    # si la direccion es a la izquierda
    elif direccion == 'IZQUIERDA':
        # velocidad hacia la esquina superior izquierda
        vel_bola = [-x, -y]

# Función para iniciar un nuevo juego.
def juego_nuevo():
    # estas variables son vectores [x, y]
    global pos_pad1, pos_pad2
    # estas variables son números enteros
    global vel_pad1, vel_pad2
    global puntuacion1, puntuacion2
    
    # posición de los pads a la mitad de la cancha
    pos_pad1 = [MITAD_ANCHO_PADS, ALTO_CANCHA / 2 - MITAD_ALTO_PADS]
    # [4, 160]
    pos_pad2 = [ANCHO_CANCHA - MITAD_ANCHO_PADS, ALTO_CANCHA / 2 - MITAD_ALTO_PADS]
    # [596, 160]
    
    # los pads inician detenidos
    vel_pad1 = 0
    vel_pad2 = 0
    
    # las puntaciones se reinician
    puntuacion1 = 0
    puntuacion2 = 0
    
    # escoger entre IZQUIERDA y DERECHA para lanzar la bola
    direccion = ['IZQUIERDA','DERECHA']
    lanzar_bola(direccion[random.randrange(0,2)])

# Función que se encarga de dibujar
# los elementos del juego en el canvas.
def dibujar(canvas):
    # estas variables son vectores [x, y]
    global pos_bola, vel_bola
    global pos_pad1, pos_pad2, vel_pad1, vel_pad2
    # estas variables son numericas
    global puntuacion1, puntuacion2

    # Syntax: canvas.draw_line(punto1, punto2, ancho_linea, color_linea)
    # dibujar la línea en medio de la cancha
    canvas.draw_line([ANCHO_CANCHA / 2, 0], [ANCHO_CANCHA / 2, ALTO_CANCHA], 1, "White")

    # dibujar el area de saque
    canvas.draw_line([ANCHO_PADS, 0], [ANCHO_PADS, ALTO_CANCHA], 1, "White")
    canvas.draw_line([ANCHO_CANCHA - ANCHO_PADS, 0], [ANCHO_CANCHA - ANCHO_PADS, ALTO_CANCHA], 1, "White")
    
    # dibujar las puntuaciones
    canvas.draw_text(str(puntuacion1), (ANCHO_CANCHA / 4, 50), 50, 'White')
    canvas.draw_text(str(puntuacion2), (ANCHO_CANCHA - (ANCHO_CANCHA / 4), 50), 50, 'White')
    
    # dibujar bola
    canvas.draw_circle(pos_bola, RADIO_BOLA, 2, "White", "White")

    # actualiza la posicion de la bola según su velocidad
    pos_bola[0] += vel_bola[0]
    pos_bola[1] += vel_bola[1]
    
    # dibujar los pads
    canvas.draw_line(pos_pad1, [pos_pad1[0], pos_pad1[1] + ALTO_PADS], ANCHO_PADS, 'White')
    # p1 = [4, 160], p2 = [4, 240]
    canvas.draw_line(pos_pad2, [pos_pad2[0], pos_pad2[1] + ALTO_PADS], ANCHO_PADS, 'White')
    # p1 = [596, 160], p2 = [596, 240]
    
    # actualiza la posicion de los pads según su velocidad
    max_pad = ALTO_CANCHA - ALTO_PADS + 1 # 321
    # pad 1
    if pos_pad1[1] + vel_pad1 in range (max_pad):
        pos_pad1[1] += vel_pad1
    # pad 2
    if pos_pad2[1] + vel_pad2 in range (max_pad):
        pos_pad2[1] += vel_pad2

    # Determinar si la bola colisiona con los bordes:
    # si la posición 'y' de la bola es menor o igual
    # a su radio (golpea arriba) o
    # si la posición 'y' de la bola es mayor o igual
    # al alto de la cancha - el radio de la bola (golpea abajo)...
    if pos_bola[1] <= RADIO_BOLA or pos_bola[1] >= ALTO_CANCHA - RADIO_BOLA:
        # entonces cambia la dirección de la bola
        # al sentido contrario
        vel_bola[1] = - vel_bola[1]
    # Determinar si la bola colisiona los pads:
    # si la posición 'x' de la bola es menor o igual
    # al ancho del pad + el radio de la bola (28)...
    elif pos_bola[0] <= ANCHO_PADS + RADIO_BOLA:
        # si la posicion 'y' de la bola esta dentro
        # del rango del tamaño del pad1...
        if pos_bola[1] >= pos_pad1[1] and pos_bola[1] <= pos_pad1[1] + ALTO_PADS:
            # entonces la bola rebota cambiando su velocidad
            # al sentido contrario.
            vel_bola[0] = - vel_bola[0]
            aumentar_velocidad_bola()
        else:
            # de lo contrario, entonces es una anotación
            # para el jugador 2.
            puntuacion2 += 1
            # lanzar la bola hacia la derecha
            lanzar_bola('DERECHA')
    # si la posición 'x' de la bola es mayor o igual
    # al ancho de la cancha - el ancho del pad + el radio de la bola (572)
    elif pos_bola[0] >= ANCHO_CANCHA - (ANCHO_PADS + RADIO_BOLA):
        # si la posición 'y' de la bola esta dentro
        # del rango del tamaño del pad2...
        if pos_bola[1] >= pos_pad2[1] and pos_bola[1] <= pos_pad2[1] + ALTO_PADS:
            # entonces la bola rebota cambiando su velocidad
            # al sentido contrario
            vel_bola[0] = - vel_bola[0]
            aumentar_velocidad_bola()
        else:
            # de lo contrario, entonces es una anotación
            # para el jugador 1.
            puntuacion1 += 1
            # lanzar la bola hacia la izquierda
            lanzar_bola('IZQUIERDA')

# Función para aumentar la velocidad
# de los pads mientras se presiona una tecla.
def al_presionar_tecla(tecla):
    # estas variables son numeros enteros
    global vel_pad1, vel_pad2
    
    # velocidad de aceleracion
    aceleracion = 10

    if tecla == simplegui.KEY_MAP["w"]:
        vel_pad1 -= aceleracion
    elif tecla == simplegui.KEY_MAP["s"]:
        vel_pad1 += aceleracion
    elif tecla == simplegui.KEY_MAP["up"]:
        vel_pad2 -= aceleracion
    elif tecla == simplegui.KEY_MAP["down"]:
        vel_pad2 += aceleracion

# Función para detener la velocidad
# de los pads al soltar una tecla.
def al_soltar_tecla(tecla):
    # estas variables son numeros enteros
    global vel_pad1, vel_pad2

    if tecla == simplegui.KEY_MAP["w"]:
        vel_pad1 = 0
    elif tecla == simplegui.KEY_MAP["s"]:
        vel_pad1 = 0
    elif tecla == simplegui.KEY_MAP["up"]:
        vel_pad2 = 0
    elif tecla == simplegui.KEY_MAP["down"]:
        vel_pad2 = 0
    
# Función para aumentar la velocidad de la bola
# cuando golpea un pad.
def aumentar_velocidad_bola():
    global vel_bola
    vel_bola[0] += vel_bola[0] * 0.1
    vel_bola[1] += vel_bola[1] * 0.1

# Crea un frame y asigna los eventos necesarios para interactuar con él.
frame = simplegui.create_frame("Pong", ANCHO_CANCHA, ALTO_CANCHA)
frame.set_draw_handler(dibujar)
frame.set_keydown_handler(al_presionar_tecla)
frame.set_keyup_handler(al_soltar_tecla)
frame.add_button('Reset', juego_nuevo, 100)

# Crea un juego nuevo e inicia la animación.
juego_nuevo()
frame.start()
