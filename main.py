import cv2 as cv
import numpy as np
from random import randint
import math as math
from evolution import *
from population import *
from path import *
from point import *
from main_window import *

if __name__ == '__main__':
    window = mainWindow()
    n = 5
    pop_count = 5
    evo = evolution(pop_count, n, window.height, window.width)

    window.drawPop(evo.pop)

    while(True):
        cv.imshow(window.window_name, window.tmp_map)
        window.key = cv.waitKey(0)
        if(window.key == esc):
            break
    cv.destroyAllWindows()
