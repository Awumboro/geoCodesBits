# -*- coding: utf-8 -*-
"""
Name:LAVOE YAWA JENNIFER
Stud. ID: 20653245
"""

path = r"C:\Users\awumb\Desktop\Projects\Coding\python\Fafali\data.wkt"


from distance import Distance

from utils import Utils

coords = Utils.read_data(path)


perimeter = Distance.Perimeter(Distance.compute_distances(coords)[1])

print(perimeter)



