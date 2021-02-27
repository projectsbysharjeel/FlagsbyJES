#Author: Sharjeel & Zain (Pindi Boys)
#Date: 12/Sept/2018
#task: Assignment part 2 (Medium Flags)

def mediumFlags(width):
   #Return two Medium Flags with any width given
   repaint(ghanaFlag(width))
   repaint(panamaFlag(width))

def ghanaFlag(width):
   #Return a medium flag of ghana with any width given
   height = width * 2 / 3
   stripeHeight = width * 2 / 9
   #make specific colors for the flag
   philippineRed = makeColor(206, 17, 28)
   metallicYellow = makeColor(252, 209, 22)
   cadmiumGreen = makeColor(0, 107, 63)
   ghanaFlag = makeEmptyPicture(width, height, metallicYellow)#make empty picture for the flag
   #Make rectangles for Ghana flag
   addRectFilled(ghanaFlag, 0, 0, width, stripeHeight, philippineRed)
   addRectFilled(ghanaFlag, 0, height - stripeHeight, width, stripeHeight, cadmiumGreen)
   #Make a star in the centre by setting up the
   #Values of startXY and endXY
   x1 = width / 2.301   
   addLine(ghanaFlag, width / 2, stripeHeight, int(x1), stripeHeight * 2)
   x2 = width / 1.771
   addLine(ghanaFlag, width / 2, stripeHeight, int(x2), stripeHeight * 2)
   x3 = width / 2.564
   y1 = height / 2.120
   addLine(ghanaFlag, int(x2), stripeHeight * 2, int(x3), int(y1))
   x4 = width / 1.639
   addLine(ghanaFlag, int(x3), int(y1), int(x4), int(y1))
   addLine(ghanaFlag, int(x4), int(y1), int(x1), stripeHeight * 2) 
   return(ghanaFlag)
   
def panamaFlag(width):
   #Return the panama flag with any width given
   height = width * 2 / 3
   #Make specific color for the flag
   crimson = makeColor(210, 16, 52)
   eBlue = makeColor(0, 82, 147)
   panamaFlag = makeEmptyPicture(width, height, white) #make an empty picture for the flag
   #Add rectangles into the empty picuture
   addRectFilled(panamaFlag, 0, height / 2, width /2, height /2, eBlue)
   addRectFilled(panamaFlag, width / 2, 0, width /2, height / 2, crimson)
   #Make a star at the top left by setting up the
   #Values of startXY and endXY
   x1 = width / 4.972 
   y1 = height / 2.843 
   addLine(panamaFlag, width / 4, height / 8, int(x1), int(y1), eBlue)
   x2 = width / 3.345 
   addLine(panamaFlag, width / 4, height / 8, int(x2), int(y1), eBlue) 
   x3 = width / 5.844
   y2 = height / 4.724
   addLine(panamaFlag, int(x2), int(y1), int(x3), int(y2), eBlue) 
   x4 = width / 3.040
   addLine(panamaFlag, int(x3), int(y2), int(x4), int(y2), eBlue) 
   addLine(panamaFlag, int(x4), int(y2), int(x1), int(y1), eBlue) 
   
   #Make the second star at the bottom right by setting up the
   #Values of startXY and endXY
   x01 = width / 1.426 #631
   y01 = height / 1.174 #511
   #define starting points of X and Y for the second star
   startX2 = width * 3 / 4
   startY2 = height * 5 / 8
   addLine(panamaFlag, startX2, startY2, int(x01), int(y01), crimson) 
   x02 = width / 1.251 #719
   addLine(panamaFlag, startX2, startY2, int(x02), int(y01), crimson) 
   x03 = width / 1.490 #604
   y02 = height / 1.405 #427
   addLine(panamaFlag, int(x02), int(y01), int(x03), int(y02), crimson) 
   x04 = width / 1.206 #746
   addLine(panamaFlag, int(x03), int(y02), int(x04), int(y02), crimson) 
   addLine(panamaFlag, int(x04), int(y02), int(x01), int(y01), crimson) 
   return(panamaFlag)
   