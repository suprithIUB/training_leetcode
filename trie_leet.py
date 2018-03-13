class TrieNode:
    def __init__(self, character):
        self.character = character
        self.children = dict()
        self.terminus = False
    
    def add(self, character, node):
        self.children[character] = node

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode('/')
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        if not word:
            return
        self.__insert(word, self.root).terminus = True
        
    def __insert(self, word, node):
        if not word:
            return node
        
        if word[0] in node.children:
            return self.__insert(word[1:], node.children[word[0]])
        else:
            new_node = TrieNode(word[0])
            node.add(word[0], new_node)
            return self.__insert(word[1:], new_node)

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        if not word:
            return True
        
        node = self.root
        return self.__search(word, node)
        
        
        
    def __search(self, word, node):
        if node.terminus and not word:
            return True
        elif not word and not node.terminus:
            return False
        
        if word[0] in node.children:
            return self.__search(word[1:], node.children[word[0]])
        else:
            return False


    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        if not prefix:
            return True
        
        node = self.root
        return self.__starts(prefix, node)
        

    def __starts(self, prefix, node):
        if not prefix and node:
            return True
        
        if prefix[0] in node.children:
            return self.__starts(prefix[1:], node.children[prefix[0]])
        else:
            return False
        
    

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

