import sys

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count += 1

        node.is_end = True

    
    def search(self, word):
        node = self.root
        result = 0
        for idx, char in enumerate(word):
            if char not in node.children:
                return 0
            node = node.children[char]

            current_score = (idx + 1) * node.count
            result = max(result, current_score)
        return result


trie = Trie()
input_data = sys.stdin.read().split()
N = int(input_data[0])
words = input_data[1:]
for word in words:
    trie.insert(word)

result = 0
for word in words:
    result = max(result, trie.search(word))

print(result)
    