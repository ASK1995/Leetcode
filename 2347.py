from collections import Counter

class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if(all(suit == suits[0] for suit in suits)):
            return "Flush"

        count = Counter(ranks)
        max_val = 1
        for rank in count.elements():
            max_val = max(count[rank], max_val)
        if(max_val >= 3):
            return "Three of a Kind"
        elif(max_val == 2):
            return "Pair"
        else:
            return "High Card"