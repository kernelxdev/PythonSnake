from renderer import render
import time
import keyboard

width = 50
height = 10

snakePos = 69
snakeX = 15
snakeY = 5

def Update():
    Movement()

    print(f"{snakeX} {snakeY}")
    snakePos = (snakeY * 50) + snakeX

    render(width, height, snakePos)

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

while True:
    Update()
    time.sleep(0.25)
