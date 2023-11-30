from collections import defaultdict, Counter


class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        wordLength = len(words[0])
        substrLength = wordLength * len(words)
        expectedWordCounts = Counter(words)
        result = []

        # Trying each way to split `s`
        # into consecutive words of length `substrLength`
        for offset in range(wordLength):
            wordCounts = {word: 0 for word in expectedWordCounts.keys()}

            # Start with counting words in the first substring
            for i in range(offset, substrLength + offset, wordLength):
                word = s[i: i + wordLength]
                if word in wordCounts:
                    wordCounts[word] += 1

            if wordCounts == expectedWordCounts:
                result.append(offset)

            # Then iterate the other substrings
            # by adding a word at the end and removing the first word
            for start in range(
                    offset + wordLength,
                    len(s) - substrLength + 1,
                    wordLength,
            ):
                removedWord = s[start - wordLength: start]
                addedWord = s[
                            start + substrLength - wordLength:
                            start + substrLength
                            ]
                if removedWord in wordCounts:
                    wordCounts[removedWord] -= 1
                if addedWord in wordCounts:
                    wordCounts[addedWord] += 1

                if wordCounts == expectedWordCounts:
                    result.append(start)

        return result
test = Solution()
a = ["barfoothefoobarman", "wordgoodgoodgoodbestword", "barfoofoobarthefoobarman", "wordgoodgoodgoodbestword", "a", "aaaa", "asdsa", "ababaab"]
b = [["foo", "bar"], ["word","good","best","word"], ["bar","foo","the"], ["word","good","best","good"], ["a"], ["a"], ["dsa"], ["ab","ba","ba"]]
# for s,words in zip(a,b):
#     print(test.findSubstring(s, words))
print(test.findSubstring(a[-1], b[-1]))