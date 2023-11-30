class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: x[0])
        ans = []
        start = intervals[0][0]
        end = intervals[0][1]
        for l, r in intervals[1:]:
            if r <= end:
                continue
            if start <= l <= end and r > end:
                end = r
            elif l > start:
                ans.append([start, end])
                start = l
                end = r
        ans.append([start, end])
        return ans


test = Solution()
# intervals = [[1,3],[2,6],[8,10],[15,18]]
# intervals = [[15,18],[1,3],[2,6],[8,10]]
intervals = [[1, 4], [0, 4]]

print(test.merge(intervals))
