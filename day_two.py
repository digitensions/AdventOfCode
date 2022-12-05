SCORES1 = {
          #Rock     Paper     Scissors
    'X': (['A', 4], ['B', 1], ['C', 7]), # Rock
    'Y': (['A', 8], ['B', 5], ['C', 2]), # Paper
    'Z': (['A', 3], ['B', 9], ['C', 6])  # Scissors
}

SCORES2 = {
          #Rock     Paper     Scissors
    'X': (['A', 3], ['B', 1], ['C', 2]), # Lose
    'Y': (['A', 4], ['B', 5], ['C', 6]), # Draw
    'Z': (['A', 8], ['B', 9], ['C', 7])  # Win
}

with open('day_two_input.txt', 'r') as file:
    cheat_sheet = file.readlines()

score_add = 0
for row in cheat_sheet:
    play1, play2 = row.split(' ')
    for k, v in SCORES1.items():
        if str(k) in str(play2):
            score = [ x for x in v if play1 in x ]
            score_add += int(score[0][1])

print(score_add)
