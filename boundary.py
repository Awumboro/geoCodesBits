# -*- coding: utf-8 -*-
"""
Name:LAVOE YAWA JENNIFER
Stud. ID: 20653245
"""

import Point
import Segment


class Boundary ( object ):
    def __init__ (self , segments ):
        self . segments = segments
        @property
        def area ( self ):
            pass
        @property
        def perimeter ( self ):
            pass
            if __name__ == '__main__ ':
                p = Point (3, 4)
                q = Point (7, 10)
                # print (p - q) # prints dx , dy of p - q
                seg = Segment (p, q)
                print (seg. distance )