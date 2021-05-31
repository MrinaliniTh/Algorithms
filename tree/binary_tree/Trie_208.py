class TrieNode():
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        import pdb;pdb.set_trace()
        current_node = self.root
        for letter in word:
            if letter not in current_node.children:
                current_node.children[letter] = TrieNode()
            current_node = current_node.children[letter]
        current_node.is_word = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        searched_node = self.node_starts_with(word)
        return searched_node.is_word if searched_node else False
    

    def node_starts_with(self, prefix):
        current_node = self.root
        for letter in prefix:
            if letter in current_node.children:
                current_node = current_node.children[letter]
            else:
                return None
        return current_node

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        return self.node_starts_with(prefix)

trie = Trie()
trie.insert(['the', 'then', 'thesis'])