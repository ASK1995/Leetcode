class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        l1, l2 = 0, 0
        merge = ""
        while(l1 < len(word1) and l2 < len(word2)):
            if(word1[l1:] >= word2[l2:]):
                merge += word1[l1]
                l1 += 1
            else:
                merge += word2[l2]
                l2 += 1

        while(l1 < len(word1)):
            merge += word1[l1]
            l1 += 1
        while(l2 < len(word2)):
            merge += word2[l2]
            l2 += 1
        return merge