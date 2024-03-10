class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # intervals.sort()
        intervals.sort(key=lambda x: x[1])
        # print(intervals)
        ans = 0
        cl, cr = intervals[0][0], intervals[0][1]
        for i in range(1, len(intervals)):
            l, r = intervals[i][0], intervals[i][1]
            if l < cr:
                # print(intervals[i])
                ans += 1
            else:
                cr = r

        return ans