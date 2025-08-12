class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        root = self.root
        for letter in word:
            if letter not in root.children:
                root.children[letter] = TrieNode()
            root = root.children[letter]
        root.end = True

    def search(self, word: str) -> bool:
        root = self.root
        for letter in word:
            if letter not in root.children:
                return False
            root = root.children[letter]
        return root.end

    def startsWith(self, prefix: str) -> bool:
        root = self.root
        for letter in prefix:
            if letter not in root.children:
                return False
            root = root.children[letter]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)