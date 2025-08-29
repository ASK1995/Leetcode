class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        l = [""]*len(s)

        for index in indices:
            l[indices[index]] = s[index]

        return "".join(l)