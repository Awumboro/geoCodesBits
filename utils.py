# -*- coding: utf-8 -*-
"""
Name:LAVOE YAWA JENNIFER
Stud. ID: 20653245
"""

class Utils:
    def read_data(filename):
        with open(filename) as fid:
            data = fid.read().strip()
            data = data.lower() \
            .strip("linestring") \
            .replace("(", "") .replace(")", "") \
            .strip().split(",")
            data = [s.strip() for s in data]
            coordinates = []
            for token in data:
                x, y = token.split()
                coordinates.append((float(x), float(y)))
            #print(coordinates)
            return coordinates

    def write_csv(data):
        rows = []
        for item in data:
            i, j, dist = item
            rows.append(f"P{i},P{j}, {dist}")
        with open("output1.csv", "w") as fid:
            for row in rows:
                fid.write(row + "\n")










