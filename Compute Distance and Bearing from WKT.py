# -*- coding: utf-8 -*-
"""
Name:LAVOE YAWA JENNIFER
Stud. ID: 20653245
"""
from utils import Utils
from distance import Distance



path = r"C:\Users\awumb\Desktop\Projects\Coding\python\Fafali\data.wkt"

coords = Utils.read_data(path)

distance = Distance.compute_distances(coords)
# print(distance)


# bearing computations

output = Utils.write_csv(distance)

