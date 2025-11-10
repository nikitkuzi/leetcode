class Solution:
    def minOperations(self, nums: List[int]) -> int:
        st = []
        if nums[0]:
            st.append(nums[0])
        res = 0
        for i in range(1, len(nums)):
            curr = nums[i]
            # print("start", curr, res, st)
            while st and st[-1] >= curr:
                prev = st.pop()
                # print("in", res)
                if prev == curr:
                    break
                res+=1
            if curr == 0:
                res+=len(st)
                st = []
            else:
                st.append(curr)
        return res + len(st)