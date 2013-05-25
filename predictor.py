import tracker
import point
import math

class predictor:
    
    def __init__(self, p1, p2):
        self.path = []
        #self.t = tracker(p1)
        #t.addPoint(p2)
        self.interval = .1

    def getDistance(self, p1, p2):
        startX = p1.x
        startY = p1.y
        endX = p2.x
        endY = p2.y

        dX = endX - startX
        dY = endY - startY
        return math.sqrt(pow(dX, 2) + pow(dY, 2))
