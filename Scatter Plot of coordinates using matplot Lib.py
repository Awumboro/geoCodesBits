# -*- coding: utf-8 -*-
"""
Name:LAVOE YAWA JENNIFER
Stud. ID: 20653245
"""
import math

from matplotlib import pyplot as plt
from utils import Utils
path = r"C:\Users\awumb\Desktop\Projects\Coding\python\Fafali\data.wkt"

coords = Utils.read_data(path)

for i in coords:
    plt.scatter(i[0], i[1])
    
plt.show()