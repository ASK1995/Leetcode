from collections import defaultdict

class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if(len(sentence1) != len(sentence2)):
            return False
        mapper = defaultdict(lambda: set())
        for key, value in similarPairs:
            mapper[key].add(value)
            mapper[value].add(key)
        print(mapper)
        for w1, w2 in zip(sentence1, sentence2):
            if w1 != w2 and w2 not in mapper[w1]:
                return False
        return True