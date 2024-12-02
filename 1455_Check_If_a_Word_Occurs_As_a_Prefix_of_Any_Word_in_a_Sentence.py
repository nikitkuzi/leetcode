class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split()
        curr_len = 0
        for i, word in enumerate(words):
            if word.startswith(searchWord):
                return i+1
            # curr_len+=len(word)+1
        return -1