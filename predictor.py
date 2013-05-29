import point
import math

class predictor:
    
    def __init__(self):
        self.screenWidth = 640
        self.screenHeight = 480
        self.path = []
        self.projected = []
        self.horizontalA = 0
        self.verticalA = 10
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
        return self.getDistance(p1,p2)

    def velocityX(self, p1, p2):
        return self.dX(p1, p2)

    def velocityY(self, p1, p2):
        return self.dY(p1, p2)

    def nextX(self, p1, p2):
        return p2.x + (self.dX(p1, p2) + self.horizontalA)

    def nextY(self, p1, p2):
        vStart = self.velocityY(p1, p2)
        return p2.y + (vStart + self.verticalA)

    def detectHA(self, p1, p2, p3):
        start = p1.x
        mid = p2.x
        end = p3.x
        d1 = mid - start
        d2 = end - mid
        dd = d2 - d1
        return dd

    def detectVA(self, p1, p2, p3):
        start = p1.y
        mid = p2.y
        end = p3.y
        d1 = mid - start
        d2 = end - mid
        dd = d2 - d1
        return dd

    def projectPath(self):
        self.projected = []
        p1 = self.path[-3]
        p2 = self.path[-2]
        p3 = self.path[-1]
        self.horizontalA = self.detectHA(p1,p2,p3)
        self.verticalA = self.detectVA(p1,p2,p3)
        p1 = p2
        p2 = p3

        while (p2.x > 0 and p2.x < self.screenWidth) and (p2.y > 0 and p2.y < self.screenHeight):
            newX = int(self.nextX(p1, p2))
            newY = int(self.nextY(p1, p2))
            p1 = p2
            p2 = point(newX, newY)
            self.projected.append(p2)
