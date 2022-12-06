#!/usr/bin/env python3

'''
Day One AdventOfCode2022
'''

elves = []
cals = 0

with open('day_one_input.txt', 'r') as treats:
    deliciousness = treats.readlines()
    for deli in deliciousness:
        if deli.startswith(('\n', '\r\n')):
            elves.append(cals)
            cals = 0
        else:
            cals += int(deli)

elves.sort()
print(f"Biggest elf calories: {sort[-1]}")
