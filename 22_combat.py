p1_lines, p2_lines = open("input", "r").read().split('\n\n')
p1_deck = [int(line) for line in p1_lines.strip().split('\n')[1:]]
p2_deck = [int(line) for line in p2_lines.strip().split('\n')[1:]]


while p1_deck !=[] and p2_deck != []:
    p1_card = p1_deck.pop(0)
    p2_card = p2_deck.pop(0)
    
    if p1_card > p2_card:
        p1_deck.extend([p1_card, p2_card])
    else:
        p2_deck.extend([p2_card, p1_card])

if p1_deck != []:
    winning_deck = p1_deck
else:
    winning_deck = p2_deck

card_count = len(winning_deck)
score = 0

for i in range(card_count):
    score += winning_deck[i] * (card_count - i)

print(score)



breakpoint()
