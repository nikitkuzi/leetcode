class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        lines = [[] for _ in range(len(words))]
        words_len = [len(word) for word in words]
        curr_len = 0
        curr_line = 0
        first_in_line = True
        for i, length in enumerate(words_len):
            curr_len += length
            if not first_in_line:
                curr_len += 1
            if curr_len <= maxWidth:
                lines[curr_line].append(words[i])
                first_in_line = False
            else:
                curr_line += 1
                curr_len = length
                lines[curr_line].append(words[i])
        spaces = [[] for _ in range(curr_line + 1)]

        for i in range(curr_line + 1):
            total_len = sum(map(len, lines[i]))
            diff = maxWidth - total_len
            words_in_line = len(lines[i])
            print(diff, words_in_line)
            if words_in_line == 1:
                spaces[i].append(" " * diff)
                continue
            if i == curr_line:
                spaces[i] = [' '] * (words_in_line - 1)
                spaces[i].append((' ' * (diff - words_in_line + 1)))
                break
            for j in range(words_in_line - 1):
                if diff % (words_in_line - 1):
                    spaces[i].append(" " * (diff // (words_in_line - 1) + 1))
                    diff -= 1
                else:
                    spaces[i].append(" " * (diff // (words_in_line - 1)))
                if j == words_in_line - 2:
                    spaces[i].append('')

        ans = []
        for l, s in zip(lines, spaces):
            line = [a + b for a,b in zip(l,s)]
            if len(line) == 0:
                break
            ans.append("".join(line))
        return ans


test = Solution()
# words = ["This", "is", "an", "example", "of", "text", "justification."]
# maxWidth = 16
# words = ["What", "must", "be", "acknowledgment", "shall", "be"]
# maxWidth = 16
words = ["Listen","to","many,","speak","to","a","few."]
maxWidth = 6
# words = ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.", "Art",
#          "is", "everything", "else", "we", "do"]
# maxWidth = 20

print(test.fullJustify(words, maxWidth))
