class Solution:
    def candy(self, ratings: list[int]) -> int:
        n, ans = len(ratings), [1] * len(ratings)

        for i in range(n - 1):
            if ratings[i] < ratings[i + 1]:
                ans[i + 1] = max(1 + ans[i], ans[i + 1])

        for i in range(n - 2, -1, -1):
            if ratings[i + 1] < ratings[i]:
                ans[i] = max(1 + ans[i + 1], ans[i])

        print(ans)
        return sum(ans)


test = Solution()
# ratings = [1, 0, 2, 3, 4, 5, 1, 2, 4, 3, 2, 1, 0]
# ratings = [0, 0, 2, 3, 4, 5, 1, 2, 4, 3, 2, 1, 0]
ratings = [1,2,87,87,87,2,1]
# ratings = [1,3,2,2,1]
# ratings = [1,0,2]
# ratings = [1,2,2]
# ratings = [1,6,10,8,7,3,2]
print(test.candy(ratings))
print(ratings)
