  # Name: Bishwo Dallakoti
# Purpose: CSC 170, Word Guessing Game Mini Project
#
from graphics import *
import random

def get_random_word():
    file = open("puzzles.txt", "r")
    things = []
    line = file.readline()
    while line != "":
        w = line.strip()
        things.append(w)
        line = file.readline()
    file.close()
    idx = random.randint(0, len(things) - 1)
    return things[idx]


def show_blanks(word):
    win = GraphWin("Word Guessing Game", 800, 400)
    win.setBackground("grey")

    blanks = []
    if len(word) >= 1:
        b1 = Text(Point(150, 100), "_")
        b1.setSize(20)
        b1.draw(win)
        blanks.append(b1)
    if len(word) >= 2:
        b2 = Text(Point(180, 100), "_")
        b2.setSize(20)
        b2.draw(win)
        blanks.append(b2)
    if len(word) >= 3:
        b3 = Text(Point(210, 100), "_")
        b3.setSize(20)
        b3.draw(win)
        blanks.append(b3)
    if len(word) >= 4:
        b4 = Text(Point(240, 100), "_")
        b4.setSize(20)
        b4.draw(win)
        blanks.append(b4)
    if len(word) >= 5:
        b5 = Text(Point(270, 100), "_")
        b5.setSize(20)
        b5.draw(win)
        blanks.append(b5)
    if len(word) >= 6:
        b6 = Text(Point(300, 100), "_")
        b6.setSize(20)
        b6.draw(win)
        blanks.append(b6)
    if len(word) >= 7:
        b7 = Text(Point(330, 100), "_")
        b7.setSize(20)
        b7.draw(win)
        blanks.append(b7)
    if len(word) >= 8:
        b8 = Text(Point(360, 100), "_")
        b8.setSize(20)
        b8.draw(win)
        blanks.append(b8)
    if len(word) >= 9:
        b9 = Text(Point(390, 100), "_")
        b9.setSize(20)
        b9.draw(win)
        blanks.append(b9)

    txt = Text(Point(100, 160), "Enter a letter:")
    txt.draw(win)

    box = Entry(Point(200, 160), 2)
    box.setSize(14)
    box.draw(win)

    btn = Rectangle(Point(240, 145), Point(300, 175))
    btn.setFill("lightgray")
    btn.draw(win)
    btxt = Text(Point(270, 160), "Submit")
    btxt.draw(win)

    abc = "abcdefghijklmnopqrstuvwxyz"
    abc_label = Text(Point(350, 200), "Letters Available: " + abc)
    abc_label.setSize(12)
    abc_label.draw(win)

    c1 = Circle(Point(500, 100), 10)
    c1.setFill("white")
    c1.draw(win)
    c2 = Circle(Point(530, 100), 10)
    c2.setFill("white")
    c2.draw(win)
    c3 = Circle(Point(560, 100), 10)
    c3.setFill("white")
    c3.draw(win)
    c4 = Circle(Point(590, 100), 10)
    c4.setFill("white")
    c4.draw(win)
    c5 = Circle(Point(620, 100), 10)
    c5.setFill("white")
    c5.draw(win)
    c6 = Circle(Point(650, 100), 10)
    c6.setFill("white")
    c6.draw(win)

    wrongs = [c1, c2, c3, c4, c5, c6]
    guessed = []
    bad = 0

    go = True
    while go:
        click = win.getMouse()
        x = click.getX()
        y = click.getY()

        if x >= 240 and x <= 300 and y >= 145 and y <= 175:
            g = box.getText()
            box.setText("")

            if len(g) == 1:
                skip = False
                for ch in guessed:
                    if ch == g:
                        skip = True
                check = False
                for letter in abc:
                    if letter == g:
                        check = True
                if not skip and check:
                    guessed.append(g)
                    temp = ""
                    for l in abc:
                        if l == g:
                            temp = temp + "_"
                        else:
                            temp = temp + l
                    abc = temp
                    abc_label.setText("Letters Available: " + abc)

                    good = False
                    i = 0
                    while i < len(word):
                        if i < len(blanks):
                            if word[i] == g:
                                blanks[i].setText(g)
                                good = True
                        i = i + 1

                    if not good and bad < 6:
                        wrongs[bad].setFill("red")
                        bad = bad + 1

                    if bad == 6:
                        lose = Text(Point(400, 300), "You Lost!")
                        lose.setSize(20)
                        lose.setTextColor("red")
                        lose.draw(win)
                        r = 0
                        while r < len(word):
                            if r < len(blanks):
                                blanks[r].setText(word[r])
                            r = r + 1
                        win.getMouse()
                        win.close()
                        go = False

                    done = True
                    j = 0
                    while j < len(word):
                        if j < len(blanks):
                            if blanks[j].getText() == "_":
                                done = False
                        j = j + 1

                    if done:
                        win_msg = Text(Point(400, 300), "You Won!")
                        win_msg.setSize(20)
                        win_msg.setTextColor("green")
                        win_msg.draw(win)
                        r = 0
                        while r < len(word):
                            if r < len(blanks):
                                blanks[r].setText(word[r])
                            r = r + 1
                        win.getMouse()
                        win.close()
                        go = False

word = get_random_word()
show_blanks(word)
