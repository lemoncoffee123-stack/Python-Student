class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert_and_check_prefix(self, word):
        node = self.root
        for char in word:
            if node.is_end:
                return True

            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        if len(node.children) > 0:
            return True

        node.is_end = True
        return False


trie = Trie()
N = int(input())
for _ in range(N):
    data = input()
    if trie.insert_and_check_prefix(data):
        print(0)
        exit()

print(1)