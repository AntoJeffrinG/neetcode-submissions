from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        seen = set(wordList)
        q = deque()
        q.append((beginWord,1))

        while q:
            word, length = q.popleft()
            original = word
            if word == endWord:
                return length
            for i in range(len(word)):
                for j in range(97,123):
                    new_word = word[:i] + chr(j) + word[i+1:]
                    if new_word in seen:
                        q.append((new_word,length+1))
                        seen.remove(new_word)
        return 0
                


        