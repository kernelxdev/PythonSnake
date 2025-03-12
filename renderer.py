# STYLE
BACKGROUNDCHAR = "o"
SNAKECHAR = "X"
APPLECHAR = "."

def render(width, height, currentSnakePos):
    fText = ""

    for y in range(height):
        line = ""
        for x in range(width):
            currentTile = (y * 50) + x
            if currentSnakePos == currentTile:
                line += SNAKECHAR
            else:
                line += BACKGROUNDCHAR
        fText += (line + "\n")

    print(f"\n{fText}")
