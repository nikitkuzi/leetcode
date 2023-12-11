class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        n += 1

        def f(ar, curr, n, k):
            # print(ar,curr)
            if curr == n or k == 0:
                # print(ar)
                ans.append(ar)
                # print("return",ar)
                return None
            for i in range(curr + 1, n):
                # ar.append(i)
                f(ar + [i], i, n, k - 1)
                # ar.pop()
            # return ar

        ans = []
        for i in range(1, n):
            f([i], i, n, k - 1)

        return ans