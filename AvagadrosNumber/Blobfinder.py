
class Blob():
    def __init__(self): #construct an empty blob
        self.blob = []
    def add(self, i, j): # add a pixel (i, j) to the blob
        self.blob.append(i,j)
    def mass(self): # return number of pixels added = its mass
        return len(self.blob)
    def distanceTo(self, blob): # return distance between centers of masses of this blob and b
        
    def centerOfMass(self): # return tuple of (x,y) values for this blob's center of mass
        x = 0            # format center-of-mass coordinates with 4 digits to right
        y = 0            # of decimal point
        for coord in self.blob:
            x = x + coord[0]
            y = y + coord[1]
        xavg = (x)/(len(self.blob))
        yavg = (y)/(len(self.blob))
        return [xavg,yavg]

def BlobFinder(picture, tau):
    '''find all blobs in the picture using the luminance threshold tau,
    loops over the pixels in the loaded image, 
    replacing the RGB values of each with either 
    black or white depending on whether its total 
    luminance is above or below some threshold 
    passed in by the user'''
    black = (0, 0, 0)
    white = (255, 255, 255)
    xsize, ysize = picture.size
    temp = picture.load()
    for x in range(xsize):
        for y in range(ysize):
            r,g,b = temp[x,y]
            if r+g+b >= tau: 
                temp[x,y] = black
            else:
                temp[x,y] = white
    
def countBeads(P):
    '''return the number of beads with >= P pixels,
    scan the image top to bottom and left to right using a nested loop.
    when black pixel is found, increment the count, then call the fill
    function to fill in all the pixels connected to that one.'''
    BLACK = (0,0,0)
    RED = (255,0,0)
    xsize, ysize = picture.size
    temp = picture.load()
    result = 0
    for x in range(xsize):
        for y in range(ysize):
            if temp[x,y] == BLACK:
                result += 1
                fill(temp,xsize,ysize,x,y)
    return result



def getBeads(P):
    '''return all beads with >= P pixels'''