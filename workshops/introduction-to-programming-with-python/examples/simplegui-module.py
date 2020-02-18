# ¡Una obra de arte!
import simplegui

def dibujar(canvas):
    canvas.draw_line([0, 0], [300, 300], 3, "Green")
    canvas.draw_line([0, 300], [300, 0], 5, "Red")
    canvas.draw_circle([150, 150], 20, 5, 'Red', 'Black')

frame = simplegui.create_frame("Test", 300, 300)
frame.set_draw_handler(dibujar)
frame.start()
