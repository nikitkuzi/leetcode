class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        if len(nums) == 1 and nums[0] == 0:
            return 2
        pref = [0]*len(nums)
        zeros = []
        for i, n in enumerate(nums):
            pref[i]+=pref[i-1]+n
            if n == 0:
                zeros.append(i)
        if pref[-1]==0:
            return len(nums)*2
        # print(pref)
        res = 0
        for zero_pos in zeros:
            # print(pref[zero_pos], pref[-1]-pref[zero_pos])
            if pref[zero_pos] == pref[-1]-pref[zero_pos]:
                res+=2
            elif abs(pref[zero_pos] - (pref[-1]-pref[zero_pos])) == 1:
                res+=1
        return res