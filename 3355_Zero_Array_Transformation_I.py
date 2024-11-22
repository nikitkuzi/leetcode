class Solution(object):
    def isZeroArray(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: bool
        """
        n = len(nums)
        # Initialize difference array
        diff = [0] * (n + 1)

        # Process queries using difference array technique
        for l, r in queries:
            diff[l] += 1  # Add 1 at start
            diff[r + 1] -= 1  # Subtract 1 after end

        # Calculate prefix sum to get coverage
        coverage = 0
        for i in range(n):
            coverage += diff[i]
            # Check if current number can be reduced to zero
            if nums[i] > coverage:
                return False

        return True
