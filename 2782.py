# Definition for a category handler.
# class CategoryHandler:
#     def haveSameCategory(self, a: int, b: int) -> bool:
#         pass
class Solution:
    def numberOfCategories(self, n: int, categoryHandler: Optional['CategoryHandler']) -> int:
        s = set([0])
        for i in range(1, n):
            found = False
            for j in s:
                if(categoryHandler.haveSameCategory(i, j)):
                    found = True
                    break
            if(not found):
                s.add(i)
        return len(s)