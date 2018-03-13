class TrieNode:
    def __init__(self, character):
        self.character = character
        self.children = dict()
        self.terminus = False

    def add_child_node(self, character, node):
        self.children[character] = node

class Trie:
    def __init__(self):
        self.root = TrieNode('/')

    def insert_word(self, word):
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
            node.add_child_node(word[0], new_node)
            return self.__insert(word[1:], new_node)

    def search(self, word):
        if not word:
            return False
        print(word)        
        import sys
        max_length = -sys.maxsize-1
        best_result = ""
        for i in range(0, len(word)):
            if word[i] in self.root.children:
    #           print(word[i])
                result = False
                longestWord = []
                longestWord.append(word[i])
                result = self.__search(word[:i] + word[i+1:], self.root.children[word[i]],
                        longestWord)
                if result:
                    print("Found")
    #               print(''.join(longestWord))
                    if len(longestWord) > max_length:
                        max_length = len(longestWord)
                        best_result = ''.join(longestWord)
        return best_result

    def __search(self, word, node, longestWord):
        if not word and node.terminus:
            return True
        
        for i in range(0, len(word)):
            if word[i] in node.children:
                print(word[i])
                longestWord.append(word[i])
                return self.__search(word[:i] + word[i+1:], node.children[word[i]], longestWord)

        return False


if __name__ == "__main__":
    t = Trie()
    for word in ['toe', 'toes', 'god', 'dog']:
        t.insert_word(word)

    letters = "odg"

    print(t.search(letters))
