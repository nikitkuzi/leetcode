# class Solution:
#     def partition(self, s: str) -> List[List[str]]:
#         res = []
#         def dfs(i,curr):
#             if i >= len(s):
#                 res.append(curr[:])
#                 return
#             for j in range(i,len(s)):
#                 if s[i:j+1] == s[i:j+1][::-1]:
#                     curr.append(s[i:j+1])
#                     dfs(j+1,curr)
#                     curr.pop()
#         dfs(0,[])
#         return res
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def f(curr, st):
            # print(curr, st)
            if len(st)==1:
                ans.append(curr+[st])
                return
            if not st and curr:
                ans.append(curr)
                return
            for i in range(len(st)):
                if st[:i+1] == st[:i+1][::-1]:

                    f(curr+[st[:i+1]], st[i+1:])
            # return curr
        ans = []
        f([],s)
        # ans.append(f([], s))
        # print(ans)
        return ans