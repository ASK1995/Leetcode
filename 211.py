class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        root = self.root
        for letter in word:
            if letter not in root.children:
                root.children[letter] = TrieNode()
            root = root.children[letter]
        root.end = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            for index in range(j, len(word)):
                letter = word[index]
                if letter == '.':
                    for child in root.children.values():
                        if(dfs(index + 1, child)):
                            return True
                    return False
                else:
                    if letter not in root.children:
                        return False
                    root = root.children[letter]
            return root.end
        return dfs(0, self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)