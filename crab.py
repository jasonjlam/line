import graphics
import random
import math

width = 1000
height = 1000
maxval = 255
crabRed = [190,25,49]
crabBlack = [0,0,0]
graphics.createPixels(width, height,maxval)
graphics.clearScreen();
points = [87,68,87,78,62,88,49,102,39,77,48,73,65,58,80,37,80,19,
        75,7,72,20,66,28,54,39,
         71,2, 56,3,41,11,22,46,18,65,21,74,19,82,43,112,39,124,
         35,122,29,123,5,100,2,104,13,126,18,130,24,130,28,135,36,136,
         48,143,31,149,6,144,1,147,0,150,24,164,34,161,42,162,54,150,64,157,
         50,167,42,172,40,175,16,184,9,189,14,193,33,193,
         44,189,48,185,53,184,61,171,67,160,77,171,67,184,67,187,
         61,193,61,209,64,221,69,223,76,217,78,208,78,192,84,185,88,177,
         104,180,120,181,136,177,141,187,145,191,146,210,150,220,154,223,
         159,223,162,211,162,192,158,187,156,182,147,171,157,162,164,176,
         171,184,176,184,181,190,196,193,208,193,213,191,212,187,196,178,
         188,176,183,176,182,172,177,169,174,168,162,159,170,151,180,160,
         183,162,190,161,193,163,201,163,217,156,224,150,223,146,207,145,
         194,150,178,145,187,137,194,136,199,132,199,131,206,131,211,126,
         221,109,222,101,220,100,216,101,195,123,194,123,185,123,180,113,
         204,88,206,78,203,75,206,69,205,52,190,17,171,4,154,2,153,4,171,39,
         156,27,150,8,144,18,144,26,155,55,184,78,175,102,157,85,137,78,
         136,78, 137,68]
for i in range(0,len(points)):
    points[i]*=4
for i in range(0, int(math.floor(len(points) / 2) - 1)):
    graphics.drawLine([points[i * 2], points[i * 2 + 1]],
                      [points[i * 2 + 2], points[i * 2 + 3]], crabRed)
graphics.drawLine([547,272],[568,255], crabBlack)
graphics.drawLine([568,255],[568,218], crabBlack)
graphics.drawLine([568,218],[543,200], crabBlack)
graphics.drawLine([543,200],[516,204], crabBlack)
graphics.drawLine([516,204],[503,224], crabBlack)
graphics.drawLine([503,224],[503,250], crabBlack)
graphics.drawLine([394,250],[394,221], crabBlack)
graphics.drawLine([394,221],[375,200], crabBlack)
graphics.drawLine([375,200],[345,200], crabBlack)
graphics.drawLine([345,200],[328,216], crabBlack)
graphics.drawLine([328,216],[328,255], crabBlack)
graphics.drawLine([328,255],[344,271], crabBlack)
graphics.drawLine([344,271],[352,271], crabBlack)
graphics.drawLine([394,250],[424,299], crabRed)
graphics.drawLine([424,299],[475,299], crabRed)
graphics.drawLine([475,299],[503,250], crabRed)
# graphics.drawLine([344,271],[395,225], crabBlack)

graphics.writeImage("crabrave.ppm")
