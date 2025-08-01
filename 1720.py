class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        res = [first]

        for index in range(len(encoded)):
            res.append(res[index] ^ encoded[index])

        return res