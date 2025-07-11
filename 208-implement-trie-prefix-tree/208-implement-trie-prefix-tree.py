class Trie:

    def __init__(self):
        self.trie = {}
        

    def insert(self, word: str) -> None:
        if word not in self.trie:
            self.trie[word] = True
        

    def search(self, word: str) -> bool:
        if word in self.trie:
            return True
        return False
        

    def startsWith(self, prefix: str) -> bool:
        words = self.trie.keys()
        for dWord in words:
            if len(dWord)>=len(prefix):
                if dWord[:len(prefix)]==prefix:
                    return True
        return False
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)