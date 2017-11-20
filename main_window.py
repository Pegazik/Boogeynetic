import cv2 as cv
import numpy as np
from random import randint
import math as math
from population import *
from path import *
from point import *

global esc
esc = 27

class mainWindow:
    def __init__(self):
        self.heightmap = cv.imread('terrain.png')
        self.tmp_map = self.heightmap.copy()
        self.height, self.width = self.tmp_map.shape[:2]
        self.window_name = 'PAPAJ'
        self.mWindow = cv.namedWindow(self.window_name, cv.WINDOW_GUI_NORMAL)
        self.maphandle = cv.imshow(self.window_name, self.tmp_map)
        self.key = 155
        esc = 27
    def drawPath(self, path):
        cv.line(self.tmp_map, path.start_point.getPoint(), path.getPoint(0), (255, 0, 0), 1)
        for i in range(1, path.length):
            cv.line(self.tmp_map, path.getPoint(i-1), path.getPoint(i), (0, 255, 0), 1)
        cv.line(self.tmp_map, path.end_point.getPoint(), path.getPoint(path.length-1), (255, 0, 0), 1)
    def drawPop(self, _population):
        for i in range(0, len(_population.paths)):
            self.drawPath(_population.paths[i])
