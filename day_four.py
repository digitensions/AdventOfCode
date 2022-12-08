#!/usr/bin/python3
'''
Day 4 AdventOfCode2022
'''

with open('day_four_input.txt', 'r') as file:
    data = file.read().splitlines()

elfy_subset = 0
elfy_intersect = 0
for line in data:
    firstpart, secondpart = line.split(',')
    elf1_start, elf1_stop = firstpart.split('-')
    elf2_start, elf2_stop = secondpart.split('-')
    elf1_range = set(range(int(elf1_start), int(elf1_stop)+1))
    elf2_range = set(range(int(elf2_start), int(elf2_stop)+1))
    if elf1_range.issubset(elf2_range) or elf2_range.issubset(elf1_range):
        elfy_subset += 1
    if elf1_range.intersection(elf2_range):
        elfy_intersect += 1

print(f'Complete jobs within another: {elfy_subset}')
print(f'Complete jobs within another: {elfy_intersect}')
