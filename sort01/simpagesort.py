#!/usr/bin/env python3

simpsons = [('Moe', "?"), ('Otto', '?'), ('Lisa', 8), ('Bart', 10), ('Maggie', 2), ('Homer', 36), ('Marge', 34)]

def ageSort(simpChar):
    if type(simpChar[1]) is int:
        return simpChar[1]
    else:
        return 200  

simpsonsAge = sorted(simpsons, key=ageSort)

print('Result of sorted(simpsons, key=byAge): ', simpsonsAge)

