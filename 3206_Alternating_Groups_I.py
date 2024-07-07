class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        res = 0
        # print(colors[-1], colors[0], colors[1])
        if colors[0] != colors[-1] and colors[0] != colors[1]:
            res+=1
        colors.append(colors[0])
        for i in range(1, len(colors)-1):
            # print(colors[i-1], colors[i], colors[i+1])
            if colors[i] != colors[i-1] and colors[i] != colors[i+1]:
                res +=1
        return res