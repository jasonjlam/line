from graphics import *
width = 500
height = 500
maxval = 255
c = [ 0, 255, 0 ]

createPixels(width, height,maxval)
clearScreen();

#octants 1 and 5
drawLine([0, 0], [width-1, height-1], c)
drawLine([0, 0], [width-1, height / 2], c)
drawLine([width-1, height-1], [0, height / 2], c)

#octants 8 and 4
c[2] = 255;
drawLine([0, height-1], [width-1, 0], c);
drawLine([0, height-1], [width-1, height/2], c);
drawLine([width-1, 0], [0, height/2], c);

#octants 2 and 6
c[0] = 255;
c[1] = 0;
c[2] = 0;
drawLine([0, 0], [width/2, height-1], c);
drawLine([width-1, height-1], [width/2, 0], c);

#octants 7 and 3
c[2] = 255;
drawLine([0, height-1], [width/2, 0], c);
drawLine([width-1, 0], [width/2, height-1], c);

#horizontal and vertical
c[2] = 0;
c[1] = 255;
drawLine([0, height/2], [width-1, height/2], c);
drawLine([width/2, 0], [width/2, height-1], c);


writeImage("test.ppm")
