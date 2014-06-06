
class Blob():
    def __init__(self): #construct an empty blob
        self.blob = []
    def add(self, i, j): # add a pixel (i, j) to the blob
        self.blob.append((i,j))
    def mass(self): # return number of pixels added = its mass
        self.mass = len(self.blob)
        return self.mass
    def distanceTo(self, b): # return distance between centers of masses of this blob and b
        x1 = self.centerOfMass()[0]
        x2 = b.centerOfMass()[0]
        y1 = self.centerOfMass()[1]
        y2 = b.centerOfMass()[1]
        distance = ((x2-x1)**2 + (y2-y1)**2)**0.5
        return distance
    def centerOfMass(self): # return tuple of (x,y) values for this blob's center of mass
        x = 0            # format center-of-mass coordinates with 4 digits to right
        y = 0            # of decimal point
        for coord in self.blob:
            x = x + coord[0]
            y = y + coord[1]
        xavg = (x)/(len(self.blob))
        yavg = (y)/(len(self.blob))
        return [xavg,yavg]

def monochrome(picture, threshold): #copied from counting stars, makes the picture black and white to be
    black = (0, 0, 0)               #used by the fill function
    white = (255, 255, 255)
    xsize, ysize = picture.size
    temp = picture.load()
    for x in range(xsize):
        for y in range(ysize):
            r,g,b = temp[x,y]
            if r+g+b <= threshold:
                temp[x,y] = black
            else:
                temp[x,y] = white

def fill(picture, xsize, ysize, xstart, ystart): #fill function from counting stars, fills blob and 
    queue = [(xstart,ystart)]                    #appends pixels to blob
    Blob_new = Blob()
    while queue:
        BLACK = (0,0,0)
        RED = (255,0,0)
        x,y,queue = queue[0][0], queue[0][1], queue[1:]
        if picture[x,y] == BLACK:
            picture[x,y] = RED
            Blob_new.add(x,y)
            if x > 0:
                queue.append((x-1,y))
            if x < (xsize-1):
                queue.append((x+1,y))
            if y > 0:
                queue.append((x, y-1))
            if y < (ysize-1):
                queue.append((x, y+1))
    return Blob_new


def count(picture):   #count function from counting stars, finds all the blobs and returns a list of
    xsize, ysize = picture.size #blobs in eache frame
    temp = picture.load()
    ListBlob = []
    result = 0
    BLACK = (0,0,0)
    RED = (255,0,0)
    for x in range(xsize):
        for y in range(ysize):
            if temp[x,y] == BLACK:
                ListBlob.append(fill(temp,xsize,ysize,x,y))
    return ListBlob

                
def BlobFinder(picture, tau): #600 works for run data, 180.0 works well for milk data
    '''find all blobs in the picture using the luminance threshold tau'''
    float(tau)
    monochrome(picture,tau)
    ListBlob = count(picture)
    return ListBlob
    
    
    
def countBeads(P,lst):
    '''return the number of beads with >= P pixels,
    scan the image top to bottom and left to right using a nested loop.
    when black pixel is found, increment the count, then call the fill
    function to fill in all the pixels connected to that one.'''
    Bigblobs = []
    for blob in lst:
        x = blob.mass()
        if x >= P:
            Bigblobs.append(blob)
    print "the number of blobs with", P, "or over pixels is",
    return len(Bigblobs)
                 

def getBeads(P,lst):
    '''return all beads with >= P pixels'''
    Beads = []
    for blob in lst:
        x = blob.mass()
        if x >= P:
            Beads.append(blob)
    return Beads