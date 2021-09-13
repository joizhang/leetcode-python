class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = [None] * 26
        self.is_word = False

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self
        for ch in word:
            ch = ord(ch) - ord('a')
            if not node.children[ch]:
                node.children[ch] = Trie()
            node = node.children[ch]
        node.is_word = True

    def search_prefix(self, prefix):
        node = self
        for ch in prefix:
            ch = ord(ch) - ord('a')
            if not node.children[ch]:
                return None
            node = node.children[ch]
        return node

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.search_prefix(word)
        return node is not None and node.is_word

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.search_prefix(prefix)
        return node is not None

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
