from pygame import init, display, font
from random import uniform

IN_COLOR = "orange"
OUT_COLOR = "gray"
STEP = 1000

WIDTH = 720
HEIGHT = 720

init()
font.init()

my_font = font.SysFont("Calibri", 20)

screen = display.set_mode((WIDTH, HEIGHT))
display.set_caption("Pi Estimation")


def draw_text(text, pos):
    screen.blit(
        my_font.render(
            text,
            False,
            "white",
            "black",
        ),
        pos,
    )


origin_x = WIDTH / 2
origin_y = HEIGHT / 2

in_circle = 0
total_points = 0
draw = 0

while True:
    a = uniform(-1.0, 1.0)
    b = uniform(-1.0, 1.0)
    fell_in = (a * a + b * b) <= 1

    in_circle += fell_in
    total_points += 1

    point = (int(origin_x + a * WIDTH / 2), int(origin_y + b * HEIGHT / 2))
    if fell_in:
        screen.set_at(point, IN_COLOR)
    else:
        screen.set_at(point, OUT_COLOR)

    draw += 1
    if draw >= STEP:
        draw = 0

        draw_text("pi ≈ " + str(4 * (in_circle / total_points)), (5, 5))
        draw_text("total = " + str(total_points), (5, 30))
        draw_text("in circle = " + str(in_circle), (5, 55))
        display.flip()
