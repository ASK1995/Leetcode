class Solution:
    def countOddLetters(self, n: int) -> int:
        letters = ""
        number_map = {0:"zero", 1:"one", 2:"two", 3:"three",
        4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine"}
        for letter in str(n):
            letters += number_map[int(letter)]
        count = Counter(letters)
        return sum(1 for key in count.keys() if count[key] % 2 != 0)