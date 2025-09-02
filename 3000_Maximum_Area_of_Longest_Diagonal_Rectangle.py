class Solution:
    @test
    def areaOfMaxDiagonal(self, dimensions: List[List[int]], test=None) -> int:
        mx = 0

        ans = 0
        for x,y in dimensions:
            d = (x*x+y*y)**0.5
            if d > mx:

                ans =  x*y
                mx = d
            elif d == mx:
                ans = max(ans, x*y)
        return ans
print("test")