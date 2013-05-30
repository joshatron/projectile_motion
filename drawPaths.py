import point
import numpy as np
import matplotlib.pyplot as plt

class drawPaths:
    
    def __init__(self, path, projected, mx, my):
        self.paths = [path, projected]
        self.maxX = mx
        self.maxY = my

    def addList(self, points):
        self.paths.append(points)
        
    def draw(self):
        x1 = []
        y1 = []
        x2 = []
        y2 = []
        for p in self.paths[0]:
            x1.append(p.x)
            y1.append(self.maxY - p.y)
        for p in self.paths[1]:
            x2.append(p.x)
            y2.append(self.maxY - p.y)

        plt.figure(1)
        plt.subplot(211)
        plt.plot(x1, y1)
        plt.plot(x2, y2)
        plt.show()
                
        
