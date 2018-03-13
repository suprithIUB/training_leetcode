class TrieNode:
    def __init__(self, character):
        self.character = character if character is None else character.lower()
        self.children = dict()
        self.terminus = False
    
    def add(self, child_node):
        self.children[child_node.character] = child_node

class Trie:
    def __init__(self):
        self.root = TrieNode('/')
    
    def insert(self, word):
        if not word:
            return
        self.__insert(word, self.root).terminus = True

    def __insert(self, word, node):
        if not word:
            return node
        if {word[0]} & node.children.keys():
            return self.__insert(word[1:], node.children[word[0]])
        else:
            new_node = TrieNode(word[0])
            node.add(new_node)
            return self.__insert(word[1:], new_node)

    def lcp(self):
        node = self.root
        ret = ''
        while len(node.children) == 1:
            node_keys = list(node.children.keys())
            ret += node_keys[0]
            node = node.children[node_keys[0]]

        return ret

if __name__ == "__main__":
    words = ["apple", "ape", "april"]
    trie = Trie()
    for word in words:
        trie.insert(word)
    print(trie.lcp())
