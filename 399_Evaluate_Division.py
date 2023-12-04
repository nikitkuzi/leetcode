class Solution:
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        pass


equations =[["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]]
values =[3.0,4.0,5.0,6.0]
queries =[["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]]
Expected = [360.00000,0.00833,20.00000,1.00000,-1.00000,-1.00000]
test = Solution()
print(test.calcEquation(equations, values, queries))