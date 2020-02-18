# Author: Isaac Ramírez, iramirezc@live.com.mx
# Last date modified: 04/10/2015
# Project: Mini-project #4. "Pong".
# Course: An Introduction to Interactive Programming in
#         Python (Part 1) @coursera.org

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2

# initialize ball_pos and ball_vel for new ball in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    x = random.randrange(120, 240) / 40
    y = random.randrange(60, 180) / 40
    if direction == 'RIGHT':
        ball_vel = [x, -y]
    elif direction == 'LEFT':
        ball_vel = [-x, -y]

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel # these are numbers
    global score1, score2 # these are ints
    paddle1_pos = [HALF_PAD_WIDTH, HEIGHT/2 - HALF_PAD_HEIGHT]
    paddle2_pos = [WIDTH - HALF_PAD_WIDTH, HEIGHT/2 - HALF_PAD_HEIGHT]
    paddle1_vel = 0
    paddle2_vel = 0
    score1 = 0
    score2 = 0
    lf = ['LEFT','RIGHT']
    spawn_ball(lf[random.randrange(0,2)])

# draw canvas and elements
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel

    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")

    # update ball's position
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "White", "White")

    # update paddle's vertical position, keep paddle on the screen
    max_paddle = HEIGHT - PAD_HEIGHT + 1
    # paddle 1
    if paddle1_pos[1] + paddle1_vel in range (max_paddle):
        paddle1_pos[1] += paddle1_vel
    # paddle 2
    if paddle2_pos[1] + paddle2_vel in range (max_paddle):
        paddle2_pos[1] += paddle2_vel

    # draw paddles
    canvas.draw_line(paddle1_pos, [paddle1_pos[0],paddle1_pos[1] + PAD_HEIGHT], PAD_WIDTH, 'White')
    canvas.draw_line(paddle2_pos, [paddle2_pos[0],paddle2_pos[1] + PAD_HEIGHT], PAD_WIDTH, 'White')

    # determine whether paddle and ball collide
    # if hits top or bottom
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    # if hits gutters
    elif ball_pos[0] <= PAD_WIDTH + BALL_RADIUS:
        # if hits paddle 1
        if ball_pos[1] >= paddle1_pos[1] and ball_pos[1] <= paddle1_pos[1] + PAD_HEIGHT:
            ball_vel[0] = - ball_vel[0]
            speedup()
        else:
            score2 += 1
            spawn_ball('RIGHT')
    elif ball_pos[0] >= WIDTH - (PAD_WIDTH + BALL_RADIUS):
        # if hits paddle 2
        if ball_pos[1] >= paddle2_pos[1] and ball_pos[1] <= paddle2_pos[1] + PAD_HEIGHT:
            ball_vel[0] = - ball_vel[0]
            speedup()
        else:
            score1 += 1
            spawn_ball('LEFT')

    # draw scores
    canvas.draw_text(str(score1), (WIDTH / 4, 50), 50, 'White')
    canvas.draw_text(str(score2), (WIDTH - WIDTH / 4, 50), 50, 'White')

def keydown(key):
    global paddle1_vel, paddle2_vel
    acc = 10
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel += acc
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel -= acc
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel -= acc
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel += acc

def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0

def speedup():
    global ball_vel
    ball_vel[0] += ball_vel[0] * 0.1
    ball_vel[1] += ball_vel[1] * 0.1

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button('Reset', new_game, 100)

# start frame
new_game()
frame.start()
