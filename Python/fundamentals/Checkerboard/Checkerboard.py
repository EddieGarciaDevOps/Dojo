from colorama import init
init()

def drawCheckerBoard(rows, collumns):
    black = " "
    red = "\033[01;37;41m" + " " + "\033[0;0m"
    squares = [black, red]

    for row in range(0, rows):
        offset = row % 2
        boardRow = ""
        for col in range(0, collumns):
            boardRow = boardRow + squares[(col + offset) % 2]
        print boardRow

length = 8
width = 8

drawCheckerBoard(length, width)
