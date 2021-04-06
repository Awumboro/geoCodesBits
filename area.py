# -*- coding: utf-8 -*-
"""
Name:LAVOE YAWA JENNIFER
Stud. ID: 20653245
"""

class Area:
    # function for shoelace area computations
    def area(coordinates):
        
        n = 0
    
        firstList = []
        secondList = []
        
        while n< len(coordinates)-1:
            a1 = coordinates[n][0] * coordinates[n+1][1] 
            firstList.append(a1)
            
            a2 = coordinates[n][1]*coordinates[n][0]
            secondList.append(a2)
            n = n+1
            
        area = abs(0.5 * (sum(firstList)-sum(secondList)))
        print("area of the polygon is {} sq. units".format(area))
        return area
