import os
from collections import Counter

def get_input(name="input"):
    current_directory = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(current_directory, name)
    with open(input_file_path, 'r') as file:
        input_file = file.read().strip().split('\n')
    
    return input_file


def get_hand_type(hand):
    card_counts = Counter(hand)
    quantity_counts = Counter(card_counts.values())
    if quantity_counts.get(5, -1) == 1:
        return 7
    elif quantity_counts.get(4, -1) == 1:
        return 6
    elif quantity_counts.get(3, -1) == 1:
        if quantity_counts.get(2, -1) == 1:
            return 5
        else:
            return 4
    elif quantity_counts.get(2, -1) == 2:
        return 3
    elif quantity_counts.get(2, -1) == 1:
        return 2
    else:
        return 1
    
def get_hand_value(hand):
    card_value = {
        'A': 13,
        'K': 12,
        'Q': 11,
        'J': 10,
        'T': 9,
        '9': 8,
        '8': 7,
        '7': 6,
        '6': 5,
        '5': 4,
        '4': 3,
        '3': 2,
        '2': 1
    }
    value = 0
    for exp, card in enumerate(hand):
        value += card_value[card] * 10 ** (2*(len(hand) - exp - 1))
    return value

def get_hand_rank(hand):
    return 10**10 * get_hand_type(hand) + get_hand_value(hand)

def main():
    input_file = get_input()
    
    hands = []
    for line in input_file:
        hand, bid = line.split(" ")
        hands.append((get_hand_rank(hand), int(bid)))
        
    hands.sort(key=lambda x: x[0])
    
    total = 0
    for i, hand in enumerate(hands):
        total += (i+1)*hand[1]
        
    print(total)
        



if __name__ == "__main__":
    main()
