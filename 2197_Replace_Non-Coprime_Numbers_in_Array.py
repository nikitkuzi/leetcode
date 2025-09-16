class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        st = []
        st.append(nums[0])
        for i in range(1, len(nums)):
            curr = nums[i]

            while st:
                g = gcd(curr, st[-1])
                if g > 1:

                    curr = st[-1] * curr // g
                    st.pop()
                else:

                    break
            st.append(curr)
        return st
