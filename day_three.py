#!/usr/bin/python3
'''
Day 3 AdventOfCode2022
'''

import string

indx = 1
list_of_contents = []
contents = string.ascii_letters
for i in contents:
    list_of_contents.append(f'{i}, {indx}')
    indx += 1

with open('day_three_input.txt', 'r') as file:
    data = file.read().splitlines()

total = 0
for line in data:
    firstpart, secondpart = line[:len(line)//2], line[len(line)//2:]
    match = [x for x in firstpart if x in secondpart]
    for item in list_of_contents:
        if match[0] in item:
            num = item.split(', ')[1]
            total += int(num)

print(f"Part One. Total of matches: {total}")

new_total = 0
groups = [data[i:i + 3] for i in range(0,len(data), 3)]
for group in groups:
    match = [x for x in group[2] if x in group[1] and x in group[0]]
    for item in list_of_contents:
        if match[0] in item:
            num = item.split(', ')[1]
            new_total += int(num)

print(f"Part Two. Total of backpacks: {new_total}")
