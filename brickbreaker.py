import tkinter
import time
import random

# How big is the playing area?
CANVAS_WIDTH = 600      # Width of drawing canvas in pixels
CANVAS_HEIGHT = 800     # Height of drawing canvas in pixels

# Constants for the bricks
N_ROWS = 8              # How many rows of bricks are there?
N_COLS = 10             # How many columns of bricks are there?
SPACING = 5             # How much space is there between each brick?
BRICK_START_Y = 50      # The y coordinate of the top-most brick
BRICK_HEIGHT = 20       # How many pixels high is each brick
BRICK_WIDTH = 54.5

# Constants for the ball and paddle
BALL_SIZE = 40
PADDLE_Y = CANVAS_HEIGHT - 40
PADDLE_WIDTH = 80

def main():
    canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT, 'Breakout')
    for row in range(N_ROWS):
        for col in range(N_COLS):
            create_brick(canvas, row, col)

    ball = canvas.create_oval(280, 380, 320, 420, fill = "blue")
    paddle = canvas.create_rectangle(260, PADDLE_Y, 340, PADDLE_Y-20, fill = "purple")

    # Increase the x coordinate by change_x and the y coordinate by change_y
    change_x = 10
    change_y = 10

    lives = 3
    bricks = 80

    life_text = canvas.create_text(10, 20, anchor='w', font='Times', text='Lives: ' + str(lives))

    while True:


        mouse_x = canvas.winfo_pointerx()
        canvas.moveto(paddle, mouse_x, PADDLE_Y)

        canvas.move(ball, change_x, change_y)

        # Check for collision with walls
        if hit_top_wall(canvas, ball):
            change_y *= -1
        if hit_left_wall(canvas, ball) or hit_right_wall(canvas, ball):
            change_x *= -1

        # Check for collision with paddle
        if hit_paddle(canvas, ball, paddle):
            change_y *= -1

        # Check for collision with bricks
        hit_brick(canvas, paddle, ball)
        results = hit_brick(canvas, paddle, ball)
        if results != None and len(results) > 1:
            canvas.delete(results[0])
            change_y *= -1
            bricks -= 1

        if fall_out(canvas, ball):
            lives -= 1
            canvas.delete(ball)
            ball = canvas.create_oval(280, 380, 320, 420, fill="blue")
            canvas.delete(life_text)
            life_text = canvas.create_text(10, 20, anchor='w', font='Times', text='Lives: ' + str(lives))


        if lives == 0:
            quit()

        if bricks == 0:
            quit()


        # Re-draw canvas
        canvas.update()

        # Pause
        time.sleep(1/40)

    canvas.mainloop()

def fall_out(canvas, ball):
    ball_top_y = get_top_y(canvas, ball)
    return ball_top_y > (CANVAS_HEIGHT - BALL_SIZE)

def hit_top_wall(canvas, ball):
    ball_top_y = get_top_y(canvas, ball)
    return ball_top_y < 0 + BALL_SIZE

def hit_left_wall(canvas, ball):
    ball_left_x = get_left_x(canvas, ball)
    return ball_left_x < 0

def hit_right_wall(canvas, ball):
    ball_left_x = get_left_x(canvas, ball)
    return ball_left_x > (CANVAS_WIDTH - BALL_SIZE)

def hit_paddle(canvas, ball, paddle):
    paddle_coords = canvas.coords(paddle)
    x1 = paddle_coords[0]
    y1 = paddle_coords[1]
    x2 = paddle_coords[2]
    y2 = paddle_coords[3]
    results = canvas.find_overlapping(x1, y1, x2, y2)
    return len(results) > 1

def hit_brick(canvas, paddle, ball):
    ball_coords = canvas.coords(ball)
    x1 = ball_coords[0]
    y1 = ball_coords[1]
    x2 = ball_coords[2]
    y2 = ball_coords[3]
    results = canvas.find_overlapping(x1, y1, x2, y2)
    if paddle not in results:
        return results
    else:
        return None

def create_brick(canvas, row, col):
    x = (col*BRICK_WIDTH) + SPACING
    if col != 0:
        x = (col * BRICK_WIDTH) + ((SPACING * col) + SPACING)
    y = (row * BRICK_HEIGHT) + ((SPACING * row) + SPACING) + 50
    x2 = x + BRICK_WIDTH
    y2 = y + BRICK_HEIGHT
    color = "red"
    if col == 0:
        color = "red"
    elif col == 1:
        color = "red"
    elif col == 2:
        color = "orange"
    elif col == 3:
        color = "orange"
    elif col == 4:
        color = "yellow"
    elif col == 5:
        color = "yellow"
    elif col == 6:
        color = "green"
    elif col == 7:
        color = "green"
    elif col == 8:
        color = "cyan"
    elif col == 9:
        color = "cyan"
    canvas.create_rectangle(x, y, x2, y2, fill = color)


def get_top_y(canvas, object):
    '''
    This friendly method returns the y coordinate of the top of an object.
    Recall that canvas.coords(object) returns a list of the object 
    bounding box: [x_1, y_1, x_2, y_2]. The element at index 1 is the top-y
    '''
    return canvas.coords(object)[1]

def get_left_x(canvas, object):
    '''
    This friendly method returns the x coordinate of the left of an object.
    Recall that canvas.coords(object) returns a list of the object 
    bounding box: [x_1, y_1, x_2, y_2]. The element at index 0 is the left-x
    '''
    return canvas.coords(object)[0]

def make_canvas(width, height, title):
    """
    DO NOT MODIFY
    Creates and returns a drawing canvas
    of the given int size with a blue border,
    ready for drawing.
    """
    top = tkinter.Tk()
    top.minsize(width=width, height=height)
    top.title(title)
    canvas = tkinter.Canvas(top, width=width + 1, height=height + 1)
    canvas.pack()
    return canvas

if __name__ == '__main__':
    main()
