class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
    
        alphabets = "abcedefghijklmnopqrstuvwxyz"
        word_set = set(wordList)
        from collections import deque
        bfs_q = deque()
        bfs_q.append(beginWord)
        visited = set()
        visited.add(beginWord)
        output = []
        queue = []
        transformation = {beginWord: None}
        transformation = {}
        #transformation.append(beginWord)
        while bfs_q:
            current_word = bfs_q.popleft()
            children = 0
            for i in range(0, len(current_word)):
                for letter in alphabets:
                    new_word = current_word[0:len(current_word)-i -1] + letter + current_word[len(current_word)-i:]
                    if new_word == endWord:
                        transformation[new_word] = current_word
                        output.append(Solution.construct_path(transformation, endWord))
                    elif new_word in word_set and new_word not in visited:
                        transformation[new_word] = current_word
                        visited.add(new_word)
                        bfs_q.append(new_word)
        print(output)
        return output

    @staticmethod
    def construct_path(path_map, end_word):
        from collections import deque
        output = deque()
        output.appendleft(end_word)
        node = path_map[end_word]
        output.appendleft(node)
        while node:
            node = path_map.get(node)
            if node:
                output.appendleft(node)
        return list(output)

if __name__ == "__main__":
	sol = Solution()
	begin = "hit"
	end = "cog"
	words = ["hot","dot","dog","lot","log","cog"]
	sol.findLadders(begin, end, words)


