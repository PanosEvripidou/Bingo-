# num1 = 34525
# text = 'abc'
# print('*{:>4d}*{:<4s}*'.format(num1, text))


import random

allCards = {1: [[], [], [], [], []], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [], 10: []}
# def GenerateCard():

# make another loop depending on the players
for x in range(5):
    B = []
    n = random.randint(1, 15)
    while n in B:
        n = random.randint(1, 15)
    B.append(n)
    allCards[1][x].append(n)

    I = []
    n = random.randint(16, 30)
    while n in I:
        n = random.randint(16, 30)
    I.append(n)
    allCards[1][x].append(n)

    N = []
    if x == 2:
        allCards[1][2].append('-')

    else:
        n = random.randint(31, 45)
        while n in N:
            n = random.randint(31, 45)
        N.append(n)
        allCards[1][x].append(n)

    G = []
    n = random.randint(46, 60)
    while n in G:
        n = random.randint(46, 60)
    G.append(n)
    allCards[1][x].append(n)

    O = []
    n = random.randint(61, 75)
    while n in O:
        n = random.randint(61, 75)
    O.append(n)
    allCards[1][x].append(n)

for row in range(5):  # prints list as a 2d card line
    for col in range(5):

        print(allCards[1][row][col], end=' ')
    print()


def draw_num():
    draw_num = []  # Saves the numbers already drawn
    rng = random.randint(1, 75)  # Gets a new num
    while rng in draw_num:  # Checks if num has already been drawn
        rng = random.randint(1, 75)
    draw_num.append(rng)
    print(rng)
    return rng


rng = draw_num()


def check_cards(rng):
    for row in range(5):  # if num exists in card it will erase it line
        for col in range(5):
            if rng == allCards[1][row][col]:
                allCards[1][row][col] = '-'
    for row in range(5):  # prints list as a 2d card
        for col in range(5):
            print(allCards[1][row][col], end=' ')
        print()


winner = False
while winner is False:
    for i in range(5):
        print(allCards[1][i])
        print(allCards[1][i].count('-'))
        if allCards[1][i].count('-') == 5:
            winner = True
            print("player 1 Won!")
    draw_num()
    check_cards(rng)
