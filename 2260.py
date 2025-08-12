from collections import defaultdict

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        index_map = defaultdict(lambda:-1)
        min_cards = len(cards) + 1
        for index, card in enumerate(cards):
            if(index_map[card] != -1):
                min_cards = min(min_cards, index - index_map[card] + 1)
            index_map[card] = index
        
        return min_cards if (min_cards != len(cards) + 1) else -1