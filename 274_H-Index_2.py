class Solution:
    def hIndex(self, citations: list[int]) -> int:
        length = len(citations)
        l = 0
        r = length - 1
        while l <= r:
            mid = (l + r) // 2
            if citations[mid] == length - mid:
                return length - mid
            if citations[mid] < length - mid:
                l = mid + 1
            else:
                r = mid - 1

        # for i in range(length):
        #     if citations[i] >= length - i:
        #         return length - i
        return length - l


test = Solution()
# citations = [3,0,6,1,5]
# citations = [3,0,6,1,5,1,1,1]
# citations = [1, 3, 2]
citations = [11, 15]
print(test.hIndex(citations))