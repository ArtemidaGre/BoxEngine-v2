from pygame import *
from random import randint
from tkinter import*

def startint():
    global black, white, red, green, blue, running, clock, fps
    global main
    black=(0, 0, 0)
    white=(255, 255, 255)
    red=(255, 0, 0)
    green=(0, 255, 0)
    blue=(0, 0, 255)
    init()
    mixer.init()
    display.set_caption('симулятор квеста 2')
    main=display.set_mode((720, 480))
    main.fill(black)
    fps=30
    running=True
    clock = time.Clock()
startint()

while running:  
    main.fill(red)
    clock.tick(fps)
    display.flip()
    evtype=event.get
    if evtype == QUIT:
        running = False
    main.fill(green)
    display.flip