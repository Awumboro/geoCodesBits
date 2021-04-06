# -*- coding: utf-8 -*-
"""
Name:LAVOE YAWA JENNIFER
Stud. ID: 20653245
"""
import math

class Distance:
    distanceList=[]


    def distance(a, b):
        dx = a[0] - b[0]
        dy = a[1] - b[1]
    
        return math.hypot(dx, dy)


    def compute_distances(coords):
        n = len(coords)
        

        
        results = []
        
        for i in range(0, n - 1):
            a = coords[i]
            b = coords[i + 1]
            dist = Distance.distance(a, b)
            Distance.distanceList.append(dist)

    
    
            dist = (i, i + 1, round(dist, 2))
    
            results.append(dist)
    
        return results, Distance.distanceList
    
    
    def Perimeter(lists):
        perimeter = sum(lists)
        return perimeter
    
    