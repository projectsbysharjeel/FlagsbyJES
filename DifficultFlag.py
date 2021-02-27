#Author: Sharjeel & Zain (pindi boys)
#date: 12/Sept/2018
#Task: Assignment part 4 - (difficult flags)

def drawDifficultFlag(width):
   #Returns two difficult flags with any width given
   #Repaint flags
   repaint (jordanFlag(width))
   repaint (singaporeFlag(width))


def jordanFlag(width):
   #Return a difficult flag with any width
   height = width / 2
   stripeHeight = height / 3
   #make colors the jordan flag
   jordanRed = makeColor(206, 17, 38)
   jordanGreen = makeColor(0, 122, 61)
   flag = makeEmptyPicture(width, height, jordanGreen)
   #Add three rectangles into the flag
   addRectFilled(flag, 0, 0, width, stripeHeight, black)
   addRectFilled(flag, 0, stripeHeight, width, stripeHeight, white)
   #Add cross lines at both starting point till midpoint of the width
   addLine(flag, 0, 0, width / 2, height / 2, red)
   addLine(flag, width / 2, height / 2, 0, width / 2, red)
   #Add lines to make a star polygon by
   #setting the values of startingXY and endingXY locations  
   x1 = width / 5.555
   y1 = height / 2.586
   x01 = width / 6.465
   y01 = height / 1.677
   addLine(flag, int(x1), int(y1), int(x01), int(y01))
   x2 = width / 4.950
   y2 = height / 1.670
   addLine(flag, int(x1), int(y1), int(x2), int(y2))
   x02 = width / 7.281
   y02 = height / 2.343
   addLine(flag, int(x2), int(y2), int(x02), int(y02))
   x3 = width / 4.285
   y3 = height / 1.903
   addLine(flag, int(x02), int(y02), int(x3), int(y3))
   x03 = width / 7.936
   y03 = height / 1.918
   addLine(flag, int(x3), int(y3), int(x03), int(y03))
   x4 = width / 4.437
   y4 = height / 2.307
   addLine(flag, int(x03), int(y03), int(x4), int(y4))
   addLine(flag, int(x4), int(y4), int(x01), int(y01))
   return(flag)
   
def singaporeFlag(width):
   #Return a difficult flag with any width given
   height = width * 2 / 3
   stripeHeight = height / 2
   #make colors first for the flag
   imperialRed = makeColor(237, 41, 57) 
   flag = makeEmptyPicture(width, height, white)
   heightOfInner = width / 4.25
   widthOfInner = width / 4.15
   addRectFilled(flag, 0, 0, width, stripeHeight, imperialRed)
   addArcFilled(flag, width / 9, stripeHeight / 8, width / 4, width / 4, 0, 360,  white) 
   addArcFilled(flag, width / 6, stripeHeight / 7, int(widthOfInner), int(heightOfInner), 0, 360, imperialRed)
   broFloat = width / 3.6
   sisFloat = stripeHeight / 5
   addArc(flag, int(broFloat) , int(sisFloat), width / 23, width / 23, 0, 360)
   return(flag)
   