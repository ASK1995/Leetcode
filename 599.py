from collections import defaultdict

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        count = defaultdict(lambda:-1)
        s1, s2 = set(list1), set(list2)
        s1 = s1 & s2

        for index, word in enumerate(list1):
            if word in s1:
                count[word] = index
        for index, word in enumerate(list2):
            if word in s1:
                count[word] += index
        count = sorted(count.items(), key = lambda x: x[1])
        res = []
        lowest_value = count[0][1]
        for key, value in count:
            if(value == lowest_value):
                res.append(key)
        return res