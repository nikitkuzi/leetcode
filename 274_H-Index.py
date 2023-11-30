class Solution:
    def hIndex(self, citations: list[int]) -> int:
        length = len(citations)
        citations.sort()
        for i in range(length):
            if citations[i] >= length - i:
                return length - i
        return 0


test = Solution()
citations = [3,0,6,1,5]
# citations = [3,0,6,1,5,1,1,1]
# citations = [1, 3, 2]
# citations = [11, 15]
print(test.hIndex(citations))