p1_lines, p2_lines = open("input", "r").read().split('\n\n')
p1_start_deck = [int(line) for line in p1_lines.strip().split('\n')[1:]]
p2_start_deck = [int(line) for line in p2_lines.strip().split('\n')[1:]]


def game(p1_deck, p2_deck):
    
    round_history = []

    while p1_deck !=[] and p2_deck != []:

        if (p1_deck, p2_deck) in round_history:
            print("Round already played.  P1 wins")
            return 1

        round_history.append((p1_deck.copy(), p2_deck.copy()))
        p1_card = p1_deck.pop(0)
        p2_card = p2_deck.pop(0)

        if p1_card <= len(p1_deck) and p2_card <= len(p2_deck):
            print("recursion")
            p1_new = p1_deck.copy()[:p1_card]
            p2_new = p2_deck.copy()[:p2_card]
            print(p1_new)
            print(p2_new)
            round_result = game(p1_new, p2_new)

        else:
            if p1_card > p2_card:
                round_result = 1
            else:
                round_result = 2

        if round_result == 1:
            card_pair = [p1_card, p2_card]
            #print(f"P1 wins round, {card_pair}")
            p1_deck.extend(card_pair)
        else:
            card_pair = [p2_card, p1_card]
            #print(f"P2 wins round, {card_pair}")
            p2_deck.extend(card_pair)



    if p1_deck != []:
        print(f"p1: {p1_deck}")
        print(score(p1_deck))
        return 1
         
    else:
        print(f"p2: {p2_deck}")
        print(score(p2_deck))
        return 2

def score(winning_deck):

    card_count = len(winning_deck)
    score = 0

    for i in range(card_count):
        score += winning_deck[i] * (card_count - i)

    print(score)

result = game(p1_start_deck, p2_start_deck)
breakpoint()
