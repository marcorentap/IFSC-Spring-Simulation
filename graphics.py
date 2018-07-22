import numpy as np
import time
import tkinter as tk


class Object:
    def __init__(self, displacement):
        self.displacement = displacement
        # TODO: Update the displacement over time

class Spring:
    def __init__(self, object, position, equilibriumHeight, length, endLength, segmentNumber):
        # Static supplied variables
        self.object = object
        self.position = position
        self.length = length
        self.endLength = endLength
        self.segmentNumber = segmentNumber
        self.equilibriumHeight = equilibriumHeight
        self.direction = 1

        # Static calculated variables
        self.segmentLength = (
            self.length - 2 * (self.endLength)) / (self.segmentNumber - 1)

        # Dynamic variables
        self.height = self.equilibriumHeight + self.object.displacement
        self.segmentAngle = 2 * \
            np.arcsin((self.height) / (self.length - 2 * self.endLength))
        self.deltaX = int(round(self.segmentLength * np.cos(self.segmentAngle / 2)))
        self.deltaY = int(round(self.segmentLength * np.sin(self.segmentAngle / 2)))

    def Update(self):
        # Recalculate when object's displacement changes
        self.height = self.equilibriumHeight + self.object.displacement
        self.segmentAngle = 2 * \
            np.arcsin((self.height) / (self.length - 2 * self.endLength))
        self.deltaX = self.segmentLength * np.cos(self.segmentAngle / 2)
        self.deltaY = self.segmentLength * np.sin(self.segmentAngle / 2)

    def Draw(self, canvas):
        self.points = []
        for i in range(self.segmentNumber):
            #Determine left or right. -1 = Left, 1 = Right
            if i%2 == 0:
                direction = -1
            else:
                direction = 1

            #Set coordinates of the points
            # [(X0, Y0), (X1, Y1), (X2, Y2), ...]
            if i == 0:
                self.points.append((self.position[0], self.position[1] + self.endLength))
            elif i == 1:
                self.points.append((self.points[i-1][0] + self.deltaX/2, self.points[i-1][1] + self.deltaY/2))

            elif i == self.segmentNumber - 1:
                self.points.append((self.points[i-1][0] + direction*self.deltaX/2, self.points[i-1][1] + self.deltaY/2))
            else:
                self.points.append((self.points[i-1][0] + direction*self.deltaX, self.points[i-1][1] + self.deltaY))

        #Draw ending lines
        canvas.create_line(self.position[0], self.position[1], self.position[0], self.position[1] + self.endLength, width=2)
        canvas.create_line(self.points[-1][0], self.points[-1][1], self.points[-1][0], self.points[-1][1] + self.endLength, width=2)
        #Draw segments
        for index, point in enumerate(self.points):
            if index != 0:
                canvas.create_line(self.points[index-1][0], self.points[index-1][1], point[0], point[1], width=2)
        #Draw object
        canvas.create_rectangle(self.points[-1][0] - 30, self.points[-1][1] + self.endLength, self.points[-1][0] + 30, self.points[-1][1] + self.endLength + 60, width=3)
