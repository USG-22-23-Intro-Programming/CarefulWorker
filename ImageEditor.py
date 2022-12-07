from graphics import*
from button import*

def darken(img):
    x = img.getWidth()
    y = img.getHeight()

    for i in range(x):
        for j in range(y):
            pix = img.getPixel(i,j)
            red = pix[0]
            green = pix[1]
            blue = pix[2]
            red = red - 40
            green = green - 40
            blue = blue - 40
            if red < 0:
                red = 0
            if green < 0:
                green = 0
            if blue < 0:
                blue = 0
           
            c = color_rgb(red,green,blue)
            img.setPixel(i,j,c)

def lighten(img):
    x = img.getWidth()
    y = img.getHeight()

    for i in range(x):
        for j in range(y):
            pix = img.getPixel(i,j)
            red = pix[0]
            green = pix[1]
            blue = pix[2]
            red = red + 40
            green = green + 40
            blue = blue + 40

            if red > 255:
                red = 255
            if green > 255:
                green = 255
            if blue > 255:
                blue = 255

            c = color_rgb(red, green, blue)
            img.setPixel(i, j, c)
            
def grayscale(img):
    x = img.getWidth()
    y = img.getHeight()
    
    for i in range(x):
        for j in range(y):
            pix = img.getPixel(i,j)
            red = pix[0]
            green = pix[1]
            blue = pix[2]
            if ((red == green) and (red == blue)):
                c = color_rgb(red, green, blue)
            else:
                    x = (red+green+blue)/3
                    c = color_rgb(int(x), int(x), int(x))
                    img.setPixel(i,j,c)

def contrast(img):
    x = img.getWidth()
    y = img.getHeight()

    for i in range(x):
        for j in range(y):
            pix = img.getPixel(i,j)
            red = pix[0]
            green = pix[1]
            blue = pix[2]
            TotalLight = pix[0]+ pix[1] + pix[2]
            q = 40
            if TotalLight > 382:
                red = red + q
                green = green + q
                blue = blue + q
                
            else:
                red = red - q
                green = green - q
                blue = blue - q
            if red < 0:
                red = 0
            if green < 0:
                green = 0
            if blue < 0:
                blue = 0
            if red > 255:
                red = 255
            if green > 255:
                green = 255
            if blue > 255:
                blue = 255
            
            
            c = color_rgb(red,green,blue)
            img.setPixel(i,j,c)
           

def main():

    win = GraphWin("Image Editor", 800, 600)
    win.setBackground("SkyBlue3")

    I = Image(Point(300,275), "SnowyImage.png")
    I.draw(win)

    
    B = Button(win, Point(655, 100), Point(755, 175), "HotPink1", "Darken")
    B2 = Button(win, Point(655, 200), Point(755, 275), "HotPink1", "Lighten")
    B3 = Button(win, Point(655, 300), Point(755, 375), "HotPink1", "Grayscale")
    B4 = Button(win, Point(655, 400), Point(755, 475), "HotPink1", "Contrast")

    Q = Button(win, Point(655, 500), Point(755, 575), "OrangeRed", "QUIT")

    while True:
        
        m = win.getMouse()

        if B.isClicked(m):
            darken(I)
        
        if B2.isClicked(m):
            lighten(I)

        if B3.isClicked(m):
            grayscale(I)

        if B4.isClicked(m):
            contrast(I)
            
           
        #if B2.isClicked(m):
           

        if Q.isClicked(m):
            break

    win.close()

if __name__ == "__main__":
    main()
