class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        trie1 = {}
        trie2 = {}
        def f(trie, arr):
            for num in arr:
                curr = trie
                for char in str(num):
                    if char not in curr:
                        curr[char] = {}
                    curr = curr[char]
                curr["end"] = True

        f(trie1, arr1)
        f(trie2, arr2)

        def f2(target_trie, source):
            mx = 0
            for num in source:
                curr = 0
                curr_trie = target_trie
                print(num)
                for char in str(num):
                    print(char)
                    if char in curr_trie:
                        curr+=1
                        curr_trie = curr_trie[char]
                        mx = max(curr, mx)
                    else:
                        curr = 0
                        break
                print("end")
            return mx
        mx1 = f2(trie2, arr1)
        mx2 = f2(trie1, arr2)
        return max(mx1, mx2)