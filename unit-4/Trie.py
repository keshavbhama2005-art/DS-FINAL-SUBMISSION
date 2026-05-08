class TrieNode:
    def __init__(self):
        self.children = {}   # dictionary for child nodes
        self.is_end = False  # marks end of word


class Trie:
    def __init__(self):
        self.root = TrieNode()

    # Insert word
    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    # Search exact word
    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end

    # Prefix search
    def starts_with(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True


# 🔹 Main Program
trie = Trie()

n = int(input("Enter number of words: "))
print("Enter words:")

for _ in range(n):
    word = input().strip()
    trie.insert(word)

# Exact search
word = input("\nEnter word to search: ")
print("Search result:", trie.search(word))

# Prefix search
prefix = input("Enter prefix to check: ")
print("Starts with prefix:", trie.starts_with(prefix))