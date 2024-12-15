class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        res = events[0][0]
        diff = events[0][1]
        for i in range(1, len(events)):
            if diff < events[i][1]-events[i-1][1]:
                diff = events[i][1]-events[i-1][1]
                res = events[i][0]
            if diff == events[i][1]-events[i-1][1]:
                res = min(res, events[i][0])
        return res