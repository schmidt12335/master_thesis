import sys
import numpy as np
np.set_printoptions(precision=3, suppress=True)
import brkraw
import pprint as pp

path = 'D:/Uni/Master/Masterarbeit/rabies/bruker_conversion/YaMa_OPT4_24_MRI_GFP_006_1_YaMa_OPT4_24_MRI_1_1_20240927_144547.zip'
pvdset = brkraw.load(path)