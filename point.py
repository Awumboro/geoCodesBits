# -*- coding: utf-8 -*-
"""
Name:LAVOE YAWA JENNIFER
Stud. ID: 20653245
"""

class Point ( object ):
    def __init__ (self , x, y):
        self .x = x
        self .y = y
        def __str__ ( self ):
            return f"({ self .x},{ self .y})"
        def __sub__ (self , other ):
            dx = self .x - other .x
            dy = self .y - other .y
            return dx , dy
        
