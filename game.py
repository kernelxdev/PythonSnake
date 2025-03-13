from renderer import render
import time
import keyboard
import random

width = 50
height = 10

snakePos = 69
snakeX = 15
snakeY = 5

points = 0
applesCords = []
applesPos = []

def Update():
    Movement()

    print(f"{snakeX} {snakeY}")
    snakePos = (snakeY * 50) + snakeX

    if applesCords != []:
        for i in applesCords:
            applesPos.insert(i, (applesCords[i][0] * 50) + applesCords[i][1])

    print(applesPos)
    print(applesCords)

    render(width, height, snakePos, applesPos)

def Movement():
    global snakePos
    global snakeY, snakeX

    if keyboard.is_pressed('w'):
        if snakeY > 0:
            snakeY -= 1
    if keyboard.is_pressed('s'):
        if snakeY < (height - 1):
            snakeY += 1
    if keyboard.is_pressed('a'):
        if snakeX > 1:
            snakeX -= 1
    if keyboard.is_pressed('d'):
        if snakeX < 50:
            snakeX += 1

def PlaceApple():
    global applesCords

    applesCords.append([random.randint(0, (height - 1)), random.randint(1, (width - 1))])

while True:
    Update()
    PlaceApple()

    time.sleep(0.25)