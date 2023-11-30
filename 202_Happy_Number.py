class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n > 1:
            if n not in visited:
                visited.add(n)
            else:
                return False
            n = sum([int(i)**2 for i in str(n)])
        return True

test = Solution()
# n = 19
n = 2

print(test.isHappy(n))
