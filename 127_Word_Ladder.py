class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        wordList.append(beginWord)

        wordList = set(wordList)
        visited = set()
        q = deque()
        q.append((beginWord, 0))
        mn = 111111
        while q:
            curr_word, cnt = q.popleft()
            wordList.remove(curr_word)
            if curr_word == endWord:
                mn = min(mn, cnt)
                # return mn
            for i in range(len(beginWord)):
                pre = curr_word[:i]
                post = curr_word[i + 1:]
                for l in string.ascii_lowercase:
                    if l == curr_word[i]:
                        continue
                    word = pre + l + post
                    if word in wordList and word not in visited:
                        q.append((word, cnt + 1))
                        visited.add(word)

        if mn == 111111:
            return 0
        return mn + 1