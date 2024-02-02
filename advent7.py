f = open("adventinput.txt", "r")
lines = f.readlines()
total = 0

def handtype(card1, card2, card3, card4, card5):
    if card1 == 11:
        card1 = 0
    if card2 == 11:
        card2 = 0
    if card3 == 11:
        card3 = 0
    if card4 == 11:
        card4 = 0
    if card5 == 11:
        card5 = 0
    hand = [card1, card2, card3, card4, card5]
    counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    #first_joker = 6
    jokers = [6, 6, 6, 6, 6]
    curr = 0
    for i in range(0, 5):
        if hand[i] == 0:
            jokers[curr] = i
            curr += 1
    for i in range(0, 15):
        if i == 0:
            joker_count = hand.count(i)
        counts[i] = hand.count(i)
    if max(counts)==5:
        if joker_count == 5:
            return (7, card1, card2, card3, card4, card5, jokers[0], jokers[1], jokers[2], jokers[3], jokers[4])
        return (7, card1, card2, card3, card4, card5, jokers[0], jokers[1], jokers[2], jokers[3], jokers[4])
    if max(counts)==4:
        if joker_count > 0:
            other_card = 0
            for card in hand:
                if card != 0:
                    other_card = card
            return (7, card1, card2, card3, card4, card5, jokers[0], jokers[1], jokers[2], jokers[3], jokers[4])
        return (6, card1, card2, card3, card4, card5, jokers[0], jokers[1], jokers[2], jokers[3], jokers[4])
    if max(counts)==3 and 2 in counts:
        if joker_count > 0:
            other_card = 0
            for card in hand:
                if card != 0:
                    other_card = card
            return (7, card1, card2, card3, card4, card5, jokers[0], jokers[1], jokers[2], jokers[3], jokers[4])
        return (5, card1, card2, card3, card4, card5, jokers[0], jokers[1], jokers[2], jokers[3], jokers[4])
    if max(counts)==3:
        if joker_count == 3:
            other_card = 0
            for card in hand:
                if card != 0:
                    other_card = card
            for i in range(0, 5):
                if hand[i] == 0:
                    hand[i] = other_card
            return (6, card1, card2, card3, card4, card5, jokers[0], jokers[1], jokers[2], jokers[3], jokers[4])
        if joker_count == 1:
            trip_card = 0
            for i in range(0, 15):
                if counts[i] == 3:
                    trip_card = i
            for i in range(0, 5):
                if hand[i] == 0:
                    hand[i] = trip_card
            return (6, card1, card2, card3, card4, card5, jokers[0], jokers[1], jokers[2], jokers[3], jokers[4])
        return (4, card1, card2, card3, card4, card5, jokers[0], jokers[1], jokers[2], jokers[3], jokers[4])
    if counts.count(2)==2:
        if joker_count == 2:
            pair_card = 0
            for i in range(0, 15):
                if counts[i] == 2 and i != 0:
                    pair_card = i
            for i in range(0, 5):
                if hand[i] == 0:
                    hand[i] = pair_card
            return (6, card1, card2, card3, card4, card5, jokers[0], jokers[1], jokers[2], jokers[3], jokers[4])
        if joker_count == 1:
            pair_card = 0
            for i in range(0, 15):
                if counts[i] == 2:
                    pair_card = i
            for i in range(0, 5):
                if hand[i] == 0:
                    hand[i] = pair_card
            return (5, card1, card2, card3, card4, card5, jokers[0], jokers[1], jokers[2], jokers[3], jokers[4])
        return (3, card1, card2, card3, card4, card5, jokers[0], jokers[1], jokers[2], jokers[3], jokers[4])
    if 2 in counts:
        if joker_count == 2:
            max_card = 0
            for i in range(0, 15):
                if counts[i] == 1:
                    max_card = i
            for i in range(0, 5):
                if hand[i] == 0:
                    hand[i] = max_card
            return (4, card1, card2, card3, card4, card5, jokers[0], jokers[1], jokers[2], jokers[3], jokers[4])
        if joker_count == 1:
            pair_card = 0
            for i in range(0, 15):
                if counts[i] == 2:
                    pair_card = i
            for i in range(0, 5):
                if hand[i] == 0:
                    hand[i] = pair_card
            return (4, card1, card2, card3, card4, card5, jokers[0], jokers[1], jokers[2], jokers[3], jokers[4])
        return (2, card1, card2, card3, card4, card5, jokers[0], jokers[1], jokers[2], jokers[3], jokers[4])
    if joker_count == 1:
        max_card = 0
        for i in range(0, 15):
            if counts[i] == 1 and i!=0:
                max_card = i
        for i in range(0, 5):
            if hand[i] == 0:
                hand[i] = max_card
        return (2, card1, card2, card3, card4, card5, jokers[0], jokers[1], jokers[2], jokers[3], jokers[4])
    return (1, card1, card2, card3, card4, card5, jokers[0], jokers[1], jokers[2], jokers[3], jokers[4])

list = []
for i in range(0, len(lines)):
    line = lines[i].split()
    card1 = 0
    card2 = 0
    card3 = 0
    card4 = 0
    card5 = 0
    if line[0][0].isnumeric():
        card1 = int(line[0][0])
    elif line[0][0]=='T':
        card1 = 10
    elif line[0][0]=='J':
        card1 = 11
    elif line[0][0]=='Q':
        card1 = 12
    elif line[0][0]=='K':
        card1 = 13
    else:
        card1 = 14
    
    if line[0][1].isnumeric():
        card2 = int(line[0][1])
    elif line[0][1]=='T':
        card2 = 10
    elif line[0][1]=='J':
        card2 = 11
    elif line[0][1]=='Q':
        card2 = 12
    elif line[0][1]=='K':
        card2 = 13
    else:
        card2 = 14

    if line[0][2].isnumeric():
        card3 = int(line[0][2])
    elif line[0][2]=='T':
        card3 = 10
    elif line[0][2]=='J':
        card3 = 11
    elif line[0][2]=='Q':
        card3 = 12
    elif line[0][2]=='K':
        card3 = 13
    else:
        card3 = 14

    if line[0][3].isnumeric():
        card4 = int(line[0][3])
    elif line[0][3]=='T':
        card4 = 10
    elif line[0][3]=='J':
        card4 = 11
    elif line[0][3]=='Q':
        card4 = 12
    elif line[0][3]=='K':
        card4 = 13
    else:
        card4 = 14

    if line[0][4].isnumeric():
        card5 = int(line[0][4])
    elif line[0][4]=='T':
        card5 = 10
    elif line[0][4]=='J':
        card5 = 11
    elif line[0][4]=='Q':
        card5 = 12
    elif line[0][4]=='K':
        card5 = 13
    else:
        card5 = 14

    new_hand = handtype(card1, card2, card3, card4, card5)
    #print(hand)
    #print(new_hand)
    #print(str(card1)+', '+str(card2)+', '+str(card3)+', '+str(card4)+', '+str(card5)+' to '+str(new_hand[1])+', '+str(new_hand[2])+', '+str(new_hand[3])+', '+str(new_hand[4])+', '+str(new_hand[5]))
    list.append((new_hand[0], new_hand[1], new_hand[2], new_hand[3], new_hand[4], new_hand[5], new_hand[6], new_hand[7], new_hand[8], new_hand[9], new_hand[10], int(line[1])))

list.sort()
print(list)
for i in range(0, len(list)):
    #print('rank '+str(i+1)+' bid '+str(list[i][6]))
    total += (i+1)*list[i][11]
print(total)
