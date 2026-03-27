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

    
    def search(self, prefix, len_prefix):
        node = self.root
        for i in range(len_prefix):
            if prefix[i] not in node.children:
                for _ in range(len_prefix - i):
                    print(0, end=" ")
                return 

            node = node.children[prefix[i]]
            print(node.count, end=" ")


trie = Trie()
n, m = map(int, input().split())
words = list(input().split())
for word in words:
    trie.insert(word)
    
find_word = input()
trie.search(find_word, m)