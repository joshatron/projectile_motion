import point

class tracker:

    def __init__(self, p):
        self.points = [p,]

    def addPoint(self, p):
        self.points.append(p)

    def getPoints(self):
        return self.points
