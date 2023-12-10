class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        dig = {'2': ['a', 'b', 'c'],
               '3': ['d', 'e', 'f'],
               '4': ['g', 'h', 'i'],
               '5': ['j', 'k', 'l'],
               '6': ['m', 'n', 'o'],
               '7': ['p', 'q', 'r', 's'],
               '8': ['t', 'u', 'v'],
               '9': ['w', 'x', 'y', 'z']
               }

        def dfs(word, next):
            if not next:
                ans.append(word)
                return
            for l in dig[next[0]]:
                dfs(word + l, next[1:])

        ans = []
        dfs("", digits)
        return ans



