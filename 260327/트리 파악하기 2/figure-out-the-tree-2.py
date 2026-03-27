class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        node.is_end = True

    
    def Print_Tire(self, node, depth=0):
        for char, child_node in sorted(node.children.items()):
            print("--" * depth + f"{char}")
            self.Print_Tire(child_node, depth + 1)


trie = Trie()
n = int(input())
for _ in range(n):
    k_str, *chars = input().split()
    k = int(k_str)
    x = "".join(chars)

    trie.insert(x)

trie.Print_Tire(trie.root)