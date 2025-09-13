class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        friends.sort(key = lambda x: order.index(x))
        return friends