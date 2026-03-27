class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, words):
        node = self.root
        for word in words:
            if word not in node.children:
                node.children[word] = TrieNode()
            node = node.children[word]


    def print_trie(self, node, depth= 0):
        sorted_keys = sorted(node.children.keys())
        for key in sorted_keys:
            print("--" * depth + key)
            self.print_trie(node.children[key], depth + 1)


trie = Trie()
N = int(input())
for _ in range(N):
    k, *data = input().split()
    trie.insert(data)

trie.print_trie(trie.root)