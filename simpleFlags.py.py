#Author: Sharjeel & Zain (Pindi Boys)
#Date: 12/Sept/2018
#task: Assignment part 1 (Simple Flags)

def simpleFlags(width):
   #Returns two simple flags on any width given 
   repaint(swissFlag(width))
   repaint(nigeriaFlag(width))

def swissFlag(width):
   #Return a swiss flag with any width selected
   height = width * 1 
   redSwiss = makeColor(216, 0, 0) #Set the color of the background
   flag = makeEmptyPicture(width, height, redSwiss)
   #Set their starting/ending/width/height values and make rectangles
   #rectangle no. 1 (horizontal)
   startX1 = width / 5 
   startY1 = height / 2.5
   widthOf1 = width / 1.666
   heightOf1 = height / 5
   addRectFilled(flag, startX1, int(startY1), int(widthOf1), heightOf1, white)
   #rectangle no. 2 (vertical)
   startX2 = width / 2.5
   startY2 = height / 5
   widthOf2 = width / 5
   heightOf2 = height / 1.666
   addRectFilled(flag, int(startX2), startY2, widthOf2, int(heightOf2), white)
   return(flag)
   
def nigeriaFlag(width):
   #Return a nigeria flag with any width
   height = width / 2
   stripeWidth = width / 3 #Width of the rectangles
   greenNiger = makeColor(0, 135, 83) #Set the color of the background
   flag = makeEmptyPicture(width, height, greenNiger)
   #Make white rectangle in the middle
   addRectFilled(flag, stripeWidth, 0, stripeWidth, height, white)
   return(flag)