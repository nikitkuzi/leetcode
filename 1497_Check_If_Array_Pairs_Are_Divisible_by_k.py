class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        rem = defaultdict(int)
        res = True
        for n in arr:
            rem[n%k]+=1
        # print(rem)
        for n in arr:
            # print(rem[n%k],rem[k-n%k])
            if n%k == 0 and rem[n%k]%2:
                return False
            elif n%k == 0:
                continue
            if rem[n%k] != rem[k-n%k]:
                return False

        return True