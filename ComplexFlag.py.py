#Author: Sharjeel & Zain (Pindi Boys)
#Date: 12/Sept/2018
#Task: Assignment part 3 - (Complex Flags)

def complexFlag():
   #Return two complex flags (Two collages)
   setMediaPath()
   #repaint each collage
   repaint(createCollage1())
   repaint(createCollage2())

def copy(source, target, targX, targY):
   #This function copy the pixels of source at the target
   targetX = targX
   for sourceX in range(0, getWidth(source)):
     targetY = targY
     for sourceY in range(0, getHeight(source)):
       px = getPixel(source, sourceX, sourceY) #Get pixel of the source
       tx = getPixel(target, targetX, targetY)
       setColor(tx, getColor(px)) #copy the source pixel color to the target pixel
       targetY = targetY + 1
     targetX = targetX + 1
     
def createCollage1():
   #make picture of each source you want to add in the collage
   source1 = makePicture("01 - Canada.png")
   source2 = makePicture("02 - Cuba.png")
   source3 = makePicture("03 - Azerbaijan.png")
   source4 = makePicture("04 - Armenia.png")
   target = makeEmptyPicture(640, 320) #make an empty picture for collage
   #first flag 
   copy(source1, target, 0, 0)
   #second flag 
   copy(source2, target, 320, 0)
   #third flag 
   copy(source3, target, 0, getHeight(target) - getHeight(source1))
   #fourth flag 
   copy(source4, target, 320, getHeight(target) - getHeight(source2))
   #Add caption below each flag
   addText(target, 5, 156, "Flag of Canada", black) #flag number one
   addText(target, 325, 156, "Flag of Cuba", black) #flag number two
   addText(target, 5, 316, "Flag of Azerbaijan", black) #flag number three
   addText(target, 325, 316, "Flag of Armenia", black) #flag number four
   return(target)
   
def createCollage2():
   #make picture of each source you want to add in the collage
   flag1 = makePicture("05 - Anguilla.png")
   flag2 = makePicture("06 - bermuda.png")
   flag3 = makePicture("07 - Bahamas.png")
   flag4 = makePicture("08 - RepublicOfAbkhazia.png")
   collage = makeEmptyPicture(640, 320) #make an empty picture for the collage
   #first flag 
   copy(flag1, collage, 0, 0)
   #second flag 
   copy(flag2, collage, 320, 0)
   #third flag 
   copy(flag3, collage, 0, getHeight(collage) - getHeight(flag1))
   #fourth flag 
   copy(flag4, collage, 320, getHeight(collage) - getHeight(flag2))
   #Add caption below each flag 
   addText(collage, 5, 156, "Flag of Angullia", black) #flag number one
   addText(collage, 325, 156, "Flag of Bermuda", black) #flag number two
   addText(collage, 5, 316, "Flag of Bahamas", black) #flag number three
   addText(collage, 325, 316, "Flag of Abkhazia", black) #flag number four
   return(collage)