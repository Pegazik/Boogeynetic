##___point.py___
import cv2 as cv
import numpy as np
from random import randint
import math as math

class point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
    def getPoint(self):
        return self.x, self.y
