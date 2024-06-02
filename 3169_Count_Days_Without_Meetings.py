class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        merged = [[0,0]]
        # print(meetings)
        l,r = meetings[0][0],meetings[0][1]
        merged.append([l,r])
        for i in range(1, len(meetings)):
            st = meetings[i][0]
            en = meetings[i][1]
            # print(l,r,st,en)
            if l<=st and r>=st:
                r = max(r,en)
                merged[-1][1]=r
            elif r < st:
                l,r=st,en
                merged.append([l,r])
        ans = 0
        merged.append([days+1,days+1])
        # print(merged)
        for i in range(len(merged)-1):
            ans+=merged[i+1][0]-merged[i][1]-1
        # mx = merged[-1][1]
        # mn = merged[0][0]
        # return ans+days-1-mx+mn-1
        return ans

