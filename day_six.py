#!/usr/bin/python3
'''
Day 6 AdventOfCode2022
'''

with open('day_six_input.txt', 'r') as transmission:
    signal = transmission.read().splitlines()

signals = list(signal[0])
for i, v in enumerate(signals):
    end = i + 4
    data = ''.join(signals[i:end])
    if len(set(data)) == 4:
        start_of_packet = end
        break

print(f"Start of packet: {start_of_packet}")


for i, v in enumerate(signals):
    end = i + 14 
    data = ''.join(signals[i:end])
    if len(set(data)) == 14:
        start_of_message = end 
        break

print(f"Start of message data: {start_of_message}")
