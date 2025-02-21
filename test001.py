def get_score(cards):
    a = [((card - 1) % 13) + 1 for card in cards]
    s = [(card - 1) // 13 for card in cards]

    d = {rank: a.count(rank) for rank in a}
    f = {suit: s.count(suit) for suit in s}

    g = {
        '同花順': (len(set(s)) == 1) and (sorted(a) == list(range(min(a), min(a) + 5))),
        '四條': 4 in d.values(),
        '葫蘆': 3 in d.values() and 2 in d.values(),
        '順子': len(set(a)) == 5 and max(a) - min(a) == 4,
        '三條': 3 in d.values(),
        '兩對': list(d.values()).count(2) == 2,
        '一對': 2 in d.values(),
        '雜牌': True
    }
    scores = {
        '同花順': 7,
        '四條': 6,
        '葫蘆': 5,
        '順子': 4,
        '三條': 3,
        '兩對': 2,
        '一對': 1,
        '雜牌': 0
    }
    return max(score for hand, score in scores.items() if g[hand])
n = int(input())
for _ in range(n):
    cards = list(map(int, input().split()))
    max_score = 0
    for i in range(6):
        temp_cards = cards[:i] + cards[i + 1:]
        max_score = max(max_score, get_score(temp_cards))

    print(max_score)
