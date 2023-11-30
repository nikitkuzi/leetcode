class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        l = 0
        r = 0
        last_visited = 0
        ans = 0
        for i, h in enumerate(height[1:], start=1):
            if h >= height[l]:
                r = i
                # print("l r:", l, r, end=",")
                for j in range(l,r):
                    ans += (height[l] - height[j])
                l = i
                last_visited = l
                # print("sum:", ans)

        # print(height[:last_visited-1:-1])
        l = n - 1
        r = 0
        for i in range(n - 2, last_visited - 1, -1):
            # print(height[i], height[l])
            if height[i] >= height[l]:
                # print("here")
                r = i
                for j in range(l, r,-1):
                    ans += (height[l] - height[j])
                l = i

        # print(height)
        # print(len(height)-1-last_visited)
        # print(height[:last_visited-1:-1])
        return ans


test = Solution()
# height = [0,1,0,2,1,0,1,3,2,1,2,1]
height = [4,2,0,3,2,5]
print(test.trap(height))
