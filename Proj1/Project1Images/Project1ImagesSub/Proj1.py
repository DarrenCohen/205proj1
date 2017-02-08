from PIL import Image

def medianOdd(myList):
    listLength = len(myList)
    sortedValues = sorted(myList)
    middleIndex = ((listLength + 1 )/2) - 1
    return sortedValues[middleIndex]

pics = []
redList = []
greenList = []
blueList = []

for i in range(9):
    im = Image.open(str(i+1) + ".png")
    pics.append(im)
    print (len(pics))
    
imgsize = pics[1].size
    
newimg = Image.new("RGB", imgsize)

print (imgsize)

for x in range(495):
    for y in range(557):
        for i in pics:
            r, g, b = i.getpixel((x, y))
            redList.append(r)
            greenList.append(g)
            blueList.append(b)
            
        redValue = medianOdd(redList)
        greenValue = medianOdd(greenList)
        blueValue = medianOdd(blueList)
        
        newimg.putpixel((x,y), (redValue, greenValue, blueValue))
        redList = []
        greenList = []
        blueList = []
        
newimg.save("TouristGone.png")
