class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        res = 0
        for index, ticket in enumerate(tickets):
            if(index <= k):
                res += min(ticket, tickets[k])
            else:
                res += min(ticket, tickets[k] - 1)
        return res