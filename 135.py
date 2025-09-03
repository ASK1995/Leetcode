class Solution:
    def candy(self, ratings: List[int]) -> int:
        res = [1]*len(ratings)

        index = 1
        while(index < len(res)):
            if(ratings[index] > ratings[index - 1]):
                res[index] = res[index - 1] + 1
            index += 1

        index = len(ratings) - 2
        while(index >= 0):
            if(ratings[index] > ratings[index + 1]):
                res[index] = max(res[index], res[index + 1] + 1)
            index -= 1

        return sum(res)