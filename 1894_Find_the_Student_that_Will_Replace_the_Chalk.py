class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        n = len(chalk)
        pref = [0] * n
        pref[0] = chalk[0]
        for i in range(1, n):
            pref[i] += chalk[i] + pref[i-1]
        k = k % pref[-1]
        l, r = 0, n-1
        print(k)
        print(pref)
        while l < r:
            mid = (l+r)//2
            print(mid, pref[mid])
            if pref[mid] >= k - pref[mid-1]:
                r = mid -1
            else:
                l = mid +1
        if l == 0 and pref[0] > k:
            return 0
        elif l > 0:
            if pref[l] < k:
                return l
        return l+1