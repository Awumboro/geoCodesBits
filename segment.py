# -*- coding: utf-8 -*-
"""
Name:LAVOE YAWA JENNIFER
Stud. ID: 20653245
"""
import math

class Segment ( object ):
    def __init__ (self , a, b):
        self .a = a
        self .b = b
        @property
        def distance ( self ):
            # dx = self .a.x - self .b.x
            # dy = self .a.y - self .b.y
            # return math . hypot (dx , dy)
            return math . hypot (*( self .a - self .b))
        @property
        def bearing ( self ):
            pass