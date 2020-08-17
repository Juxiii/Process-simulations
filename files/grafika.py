from graphics import *


def grafika(win, kolejka, i):
    xcord = 0
    ycord = 0
    tabelkaY = []
    tabelkaX = []
    Rectangle(Point(0, 0), Point(1650, 20)).draw(win)
    Rectangle(Point(0, 0), Point(30, 20)).draw(win)
    Line(Point(0, 20), Point(100000, 20)).draw(win)
    for j in range(i):  # tabelka na gorze
        tabelkaX.append(Text(Point(30 + 50 * (j + 1), 10), (j + 1) * 50))
        Line(Point(30 + 50 * j, 20), Point(30 + 50 * j, 30000)).draw(win)
        tabelkaX[j].setSize(6)
        tabelkaX[j].draw(win)
    for j in range(len(kolejka)):  # tabelka po lewej
        tabelkaY.append(Text(Point(15, 35 + j * 30), kolejka[j].id))
        Rectangle(Point(0, 20 + 30 * j), Point(30, 20 + 30 * (j + 1))).draw(win)
        Line(Point(0, 20 + 30 * (j + 1)), Point(100000, 20 + 30 * (j + 1))).draw(win)
        tabelkaY[j].setSize(6)
        tabelkaY[j].draw(win)
    win.getMouse()
    str = win.getKey()
    while str != "q":  # zmiana ekranu / wyjscie z diagramu
        str = win.getKey()
        if str == "a":
            xcord -= 1
            if xcord < 0:
                xcord = 0
            win.setCoords(xcord*1650, ycord*750+750, xcord*1650+1650, ycord*750)
        elif str == "w":
            ycord -= 1
            if ycord < 0:
                ycord = 0
            win.setCoords(xcord*1650, ycord*750+750, xcord*1650+1650, ycord*750)
        elif str == "s":
            ycord += 1
            win.setCoords(xcord*1650, ycord*750+750, xcord*1650+1650, ycord*750)
        elif str == "d":
            xcord += 1
            win.setCoords(xcord*1650, ycord*750+750, xcord*1650+1650, ycord*750)
    win.close()
