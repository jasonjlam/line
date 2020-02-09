import graphics
import random

width = 512
height = 512
maxval = 255

graphics.createPixels(width, height,maxval)
graphics.clearScreen();
x = 0;
for i in range(0, 300000):
    graphics.drawLine([x * i, x - i] , [i^2, i + x],
            [random.randint(150,255), random.randint(0,60), random.randint(150,255)])
    x += 1
    x *= i
graphics.drawLine([100,0],[100,500], [0,0,0])
graphics.writeImage("test.ppm")
