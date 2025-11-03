class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res = 0
        st = [(colors[0], neededTime[0])]
        for i in range(1, len(colors)):
            # print(st)
            if st[-1][0] == colors[i]:
                if neededTime[i] < st[-1][1]:
                    res+=neededTime[i]
                else:
                    res+=st.pop()[1]
                    st.append((colors[i], neededTime[i]))
            else:
                st.append((colors[i], neededTime[i]))
        return res