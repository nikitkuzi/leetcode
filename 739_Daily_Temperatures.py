class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # ans = deque()
        # mx = 0
        # for i in range(len(temperatures)-1,-1,-1):
        #     if mx <= temperatures[i]:
        #         mx = temperatures[i]
        #         ans.appendleft(0)
        #     else:
        #         step = 1
        #         while step <= len(ans):# and step+i<len(temperatures):
        #             # print(temperatures[i], temperatures[i+step])
        #             if temperatures[i] < temperatures[i+step]:
        #                 ans.appendleft(step)
        #                 break
        #             if temperatures[i] == temperatures[i+step]:
        #                 ans.appendleft(ans[step-1]+step)
        #                 break
        #             step+=1
        # # print(ans)
        # return ans

        results = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                index = stack.pop()
                results[index] = i - index
            stack.append(i)

        return results

