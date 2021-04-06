# -*- coding: utf-8 -*-
"""
Name:LAVOE YAWA JENNIFER
Stud. ID: 20653245
"""


    
path = r"C:\Users\awumb\Desktop\Projects\Coding\python\Fafali\data.wkt"

from utils import Utils
from area import Area
coords = Utils.read_data(path)
myArea = Area.area(coords)
