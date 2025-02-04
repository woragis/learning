import random
from typing import List


my_cards: List[str] = ['jack', 'queen', 'king']
print('My cards: ', ', '.join(my_cards))
random.shuffle(my_cards)
print('My cards: ', ', '.join(my_cards))
