import cv2 as cv
import numpy as np
from random import randint
import math as math
from population import *
from path import *
from point import *

class evolution:
    def __init__(self, _pop_count = 0, _n = 0, _height = 0, _width = 0):
        self.pop = population(_pop_count, _n, _height, _width)
        self.pop_new = population()
        self.exp_beta = 3
