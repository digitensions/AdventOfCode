#!/usr/bin/python3
'''
Day 5 AdventOfCode2022
Working those Christmas lists
'''


def load_data():
    with open('day_five_input.txt', 'r') as file:
        data1 = file.read().splitlines()[:8]

    c1,c2,c3,c4,c5,c6,c7,c8,c9 = [],[],[],[],[],[],[],[],[]

    for line in data1:
        col = [*line]
        try:
            col1, col2 = col[1], col[5]
            col3, col4 = col[9], col[13]
            col5, col6 = col[17], col[21]
            col7, col8, col9 = col[25], col[29], col[33]
        except:
            pass

        c1.append(col1)
        c2.append(col2)
        c3.append(col3)
        c4.append(col4)
        c5.append(col5)
        c6.append(col6)
        c7.append(col7)
        c8.append(col8)
        c9.append(col9)

    c1 = [x.strip() for x in c1 if x.strip()]
    c2 = [x.strip() for x in c2 if x.strip()]
    c3 = [x.strip() for x in c3 if x.strip()]
    c4 = [x.strip() for x in c4 if x.strip()]
    c5 = [x.strip() for x in c5 if x.strip()]
    c6 = [x.strip() for x in c6 if x.strip()]
    c7 = [x.strip() for x in c7 if x.strip()]
    c8 = [x.strip() for x in c8 if x.strip()]
    c9 = [x.strip() for x in c9 if x.strip()]
    return c1, c2, c3, c4, c5, c6, c7, c8, c9


def stage_one(c1,c2,c3,c4,c5,c6,c7,c8,c9):
    with open('day_five_input.txt', 'r') as file:
        data2 = file.read().splitlines()

    for line in data2:
        if 'move' not in line:
            continue
        ls = line.split(' ')
        crates, frm, to = int(ls[1]), ls[3], ls[5]

        for num in range(1, (crates + 1)):
            char = frm
            if '1' in frm:
                char = c1[0]
                c1.remove(c1[0])
            elif '2' in frm:
                char = c2[0]
                c2.remove(c2[0])
            elif '3' in frm:
                char = c3[0]
                c3.remove(c3[0])
            elif '4' in frm:
                char = c4[0]
                c4.remove(c4[0])
            elif '5' in frm:
                char = c5[0]
                c5.remove(c5[0])
            elif '6' in frm:
                char = c6[0]
                c6.remove(c6[0])
            elif '7' in frm:
                char = c7[0]
                c7.remove(c7[0])
            elif '8' in frm:
                char = c8[0]
                c8.remove(c8[0])
            elif '9' in frm:
                char = c9[0]
                c9.remove(c9[0])
            if '1' in to:
                c1.insert(0, char)
            elif '2' in to:
                c2.insert(0, char)
            elif '3' in to:
                c3.insert(0, char)
            elif '4' in to:
                c4.insert(0, char)
            elif '5' in to:
                c5.insert(0, char)
            elif '6' in to:
                c6.insert(0, char)
            elif '7' in to:
                c7.insert(0, char)
            elif '8' in to:
                c8.insert(0, char)
            elif '9' in to:
                c9.insert(0, char)

    print(f'Cratemover 9000: {c1[0]}{c2[0]}{c3[0]}{c4[0]}{c5[0]}{c6[0]}{c7[0]}{c8[0]}{c9[0]}')


def stage_two(c1,c2,c3,c4,c5,c6,c7,c8,c9):
    with open('day_five_input.txt', 'r') as file:
        data2 = file.read().splitlines()

    for line in data2:
        if 'move' not in line:
            continue
        ls = line.split(' ')
        crates, frm, to = int(ls[1]), ls[3], ls[5]
        char = frm
        if '1' in frm:
            char = c1[:crates]
            del c1[:crates]
        elif '2' in frm:
            char = c2[:crates]
            del c2[:crates]
        elif '3' in frm:
            char = c3[:crates]
            del c3[:crates]
        elif '4' in frm:
            char = c4[:crates]
            del c4[:crates]
        elif '5' in frm:
            char = c5[:crates]
            del c5[:crates]
        elif '6' in frm:
            char = c6[:crates]
            del c6[:crates]
        elif '7' in frm:
            char = c7[:crates]
            del c7[:crates]
        elif '8' in frm:
            char = c8[:crates]
            del c8[:crates]
        elif '9' in frm:
            char = c9[:crates]
            del c9[:crates]
        if '1' in to:
            c1 = char + c1
        elif '2' in to:
            c2 = char + c2
        elif '3' in to:
            c3 = char + c3
        elif '4' in to:
            c4 = char + c4
        elif '5' in to:
            c5 = char + c5
        elif '6' in to:
            c6 = char + c6
        elif '7' in to:
            c7 = char + c7
        elif '8' in to:
            c8 = char + c8
        elif '9' in to:
            c9 = char + c9

    print(f'Cratemover 9001: {c1[0]}{c2[0]}{c3[0]}{c4[0]}{c5[0]}{c6[0]}{c7[0]}{c8[0]}{c9[0]}')


def main():
    c1,c2,c3,c4,c5,c6,c7,c8,c9 = load_data()
    stage_one(c1,c2,c3,c4,c5,c6,c7,c8,c9)
    c1,c2,c3,c4,c5,c6,c7,c8,c9 = load_data()
    stage_two(c1,c2,c3,c4,c5,c6,c7,c8,c9)


if __name__ == '__main__':
    main()
