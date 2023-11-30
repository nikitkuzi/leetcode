from bisect import bisect


class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        if len(intervals) == 0:
            return [newInterval]
        x = bisect.bisect(intervals,newInterval[0],key=lambda x:x[0])
        intervals.insert(x,newInterval)
        ans = [intervals[0]]

        for i in range(1, len(intervals)):
            end = ans[-1][1]
            l = intervals[i][0]
            r = intervals[i][1]
            if l <= end:
                ans[-1][1] = max(end, r)
            else:
                ans.append(intervals[i])
        return ans

test = Solution()
# intervals = [[1,3],[6,9]]
# newInterval = [2, 5]
# intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
# newInterval = [4,8]
intervals = [[1,5]]
newInterval = [2,7]
# intervals = [[1,3],[6,9]]
# newInterval = [2,5]
print(test.insert(intervals, newInterval))
