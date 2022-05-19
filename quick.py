from pokereval.card import Card
from pokereval.hand_evaluator import HandEvaluator

def k(s):
    s = list(s)

    if len(s) > 2:
        s = [s[0]+s[1], s[2]]

    d1 = {
        'a':2,
        '2':3,
        '3':4,
        '4':5,
        '5':6,
        '6':7,
        '7':8,
        '8':9,
        '9':10,
        '10':11,
        'j':12,
        'q':13,
        'k':14,
    }

    d2 = {
        's':1,
        'h':2,
        'c':3,
        'd':4,
    }

    return d1[s[0]], d2[s[1]]

def xs(g):
    l = 

def f():
    hole = []
    board = []
    for i in range(2):
        print("=============")
        a = input("Val  : ")
        a,b = k(a)
        hole.append(Card(a, b))

    
    print("2 Card Eval : ", HandEvaluator.evaluate_hand(hole, board))

    for i in range(3):
        print("=============")
        a = input("Val  : ")
        a,b = k(a)
        board.append(Card(a, b))

    print("5 Card Eval : ", HandEvaluator.evaluate_hand(hole, board))


    print("=============")
    a = input("Val  : ")
    a,b = k(a)
    board.append(Card(a, b))
    print("6 Card Eval : ", HandEvaluator.evaluate_hand(hole, board))

    print("=============")
    a = input("Val  : ")
    a,b = k(a)
    board.append(Card(a, b))
    print("7 Card Eval : ", HandEvaluator.evaluate_hand(hole, board))
