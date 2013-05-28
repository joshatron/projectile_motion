import point
import math

class predictor:
    
    def __init__(self, points = None):
        self.screenWidth = 640
        self.screenHeight = 480
        self.path = []
        self.projected = []
        self.airResistance = 1. 
        #effect of air resitance. Value should be less than or equal to 1.
        if points is None:
            start = 0
        else:
            path.extend(points)
        self.interval = .0333
        self.g = 100000

    def addPointPath(self, p):
        self.path.append(p)

    def distance(self, p1, p2):
        startX = p1.x
        startY = p1.y
        endX = p2.x
        endY = p2.y

        dX = endX - startX
        dY = endY - startY
        return math.sqrt(pow(dX, 2) + pow(dY, 2))

    def dX(self, p1, p2):
        start = p1.x
        end = p2.x
        return end - start

    def dY(self, p1, p2):
        start = p1.x
        end = p2.x
        return end - start

    def velocity(self, p1, p2):
        return self.getDistance(p1,p2) / self.interval

    def velocityX(self, p1, p2):
        return self.dX(p1, p2) / self.interval

    def velocityY(self, p1, p2):
        return self.dY(p1, p2) / self.interval

    def nextX(self, p1, p2):
        return (p2.x + self.dX(p1, p2)) * self.airResistance

    def nextY(self, p1, p2):
        vStart = self.velocityY(p1, p2)
        return (p2.y + (vStart * self.interval - .5 * self.g * pow(self.interval, 2))) * self.airResistance

    def projectPath(self):
        p1 = self.path[-2]
        p2 = self.path[-1]

        while (p2.x > 0 and p2.x < self.screenWidth) and (p2.y > 0 and p2.y < self.screenHeight):
            newX = int(self.nextX(p1, p2))
            newY = int(self.nextY(p1, p2))
            p1 = p2
            p2 = point(newX, newY)
            self.projected.append(p2)
