from pygame import *
back = (200, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)

game = Trueclock = time.Clock()
FPS = 60

while game:
    for e in event.get():
        if e.type == QUET:
            game = False
    desplay.update()
    clock.tick(FPS)
