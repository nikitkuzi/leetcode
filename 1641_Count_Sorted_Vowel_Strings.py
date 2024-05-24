# class Solution:
#     def countVowelStrings(self, n: int) -> int:
#         ans = 0
#         def f(level,prev_max):
#             if level == n+1:
#                 # print(s)
#                 nonlocal ans
#                 ans+=1
#                 return
#             for i in range(prev_max, 5):
#                 f(level+1, i)
#         f(1,0)
#         return ans
import pytest
class Solution:
    def countVowelStrings(self, n: int) -> int:
        if (n == 1):
            return 5
        if (n == 2):
            return 15
        lst = [[5, 4, 3, 2, 1]]
        lmt = [5, 15]

        while (len(lmt) != n):
            st = lst.pop()
            ct = lmt[-1]
            count = ct
            tmp = [count]
            while (st):
                val = st.pop(0)
                if (val <= 0):
                    break
                ct += count - val
                count = count - val
                tmp.append(count)

            lst.append(tmp.copy())
            lmt.append(ct)
            # print(lmt,lst)
        return lmt[-1]

def test_fun():
    assert 2+2==5