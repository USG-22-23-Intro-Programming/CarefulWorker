from graphics import*
from button import*


def main():

    win = GraphWin("character creator", 800, 600)
    win.setBackground("PaleVioletRed1")

    C = Circle(Point(300, 300), 150)
    C.draw(win)

    BigEye1 = Circle(Point(220, 250), 35)
    BigEye2 = Circle(Point(380, 250), 35)

    smallEye1 = Circle(Point(250, 250), 20)
    smallEye2 = Circle(Point(350, 250), 20)

    CircleNose1 = Circle(Point(300,300), 25)
    CircleNose2 = Circle(Point(300,300), 15)

    StraightFacedMouth = Line(Point(250, 370), Point(350, 370))

    CircleMouth = Circle(Point(300,370), 35)

    B = Button(win, Point(500, 100), Point(600, 175), "CadetBlue2", "Big Eyes")
    B2 = Button(win, Point(630, 100), Point(730, 175), "CadetBlue2", "Small Eyes")
    B3 = Button(win, Point(500, 200), Point(600, 275), "CadetBlue2", "Medium Circle Nose")
    B4 = Button(win, Point(630, 200), Point(730, 275), "CadetBlue2", " Small Circle Nose")
    B5 = Button(win, Point(500, 300), Point(600, 375), "CadetBlue2", "Line Mouth")
    B6 = Button(win, Point(630, 300), Point(730, 375), "CadetBlue2", "Circle Mouth")

    Q = Button(win, Point(560, 400), Point(660, 475), "tomato", "QUIT")

    while True:
        m = win.getMouse()
        
        if B.isClicked(m):
            BigEye1.undraw()
            BigEye2.undraw()
            smallEye1.undraw()
            smallEye2.undraw()
            
            BigEye1.draw(win)
            BigEye2.draw(win)

        if B2.isClicked(m):
            smallEye1.undraw()
            smallEye2.undraw()
            BigEye1.undraw()
            BigEye2.undraw()
            
            smallEye1.draw(win)
            smallEye2.draw(win)

        if B3.isClicked(m):
            CircleNose2.undraw()

            CircleNose1.draw(win)

        if B4.isClicked(m):
            CircleNose1.undraw()

            CircleNose2.draw(win)

        if B5.isClicked(m):
            CircleMouth.undraw()

            StraightFacedMouth.draw(win)

        if B6.isClicked(m):
            StraightFacedMouth.undraw()

            CircleMouth.draw(win)

        if Q.isClicked(m):
            break

    win.close()

if __name__ == "__main__":
    main()
