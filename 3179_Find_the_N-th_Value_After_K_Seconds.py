class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        pref = [1]*n
        mod = 10**9+7
        for i in range(1,k+1):
            prev = 1
            for i in range(1,n):
                # prev += pref[i]
                # curr = pref[i]
                pref[i]=(pref[i-1]+pref[i])%(mod)
            # print(pref)
        return pref[-1]