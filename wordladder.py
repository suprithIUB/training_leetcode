class Solution:
    
    def get_hop_count(self, map_of_paths, endWord):
        count = 1
        hop = map_of_paths[endWord]
        while hop:
            count += 1
            hop = map_of_paths[hop]
        return count
    
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        
        
        
        word_set = set(wordList)
        if endWord not in wordList:
            return 0
        
        from collections import deque
        
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        visited = set()
        bfs_queue = deque()
        word_length = len(beginWord)
        bfs_queue.append(beginWord)
        visited.add(beginWord)
        import sys
        shortest_path = sys.maxsize
        
        map_of_paths = dict()
        map_of_paths[beginWord] = ''
        
        while bfs_queue:
            current_word = bfs_queue.popleft()
            visited.add(current_word)
            if current_word == endWord:
                map_of_paths[next_word] = current_word
                shortest_path = min(shortest_path, self.get_hop_count(map_of_paths, endWord))
            
            #get neighbors
            for i in range(0, word_length):
                for c in alphabets:
                    next_word = current_word[0:word_length-i-1] + c + current_word[word_length-i:]
                    if next_word in word_set and next_word not in visited:
                        bfs_queue.append(next_word)
                        visited.add(next_word)
                        map_of_paths[next_word] = current_word
            
        if shortest_path == sys.maxsize:
            shortest_path = 0
        return shortest_path    

if __name__ == "__main__":
    s = Solution()
    print(s.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))

