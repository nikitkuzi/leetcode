# class Solution:
#     def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
#         divs = defaultdict(int)
#         ans = 0
#         for n in nums2:
#             divs[n*k]+=1
#         for n in nums1:
#             for d in range(1, int(sqrt(n))):
#                 if n%d==0:
#                     if d in divs:
#                         ans+=divs[d]
#                     if n//d in divs:# and n//d!=d:
#                         ans+=divs[n//d]
#                     # if n//d==d:
#                         # ans-=divs[d]
#             if sqrt(n)%1==0:
#                 if sqrt(n) in divs:
#                     ans-=divs[sqrt(n)]
#         return ans
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        divs = defaultdict(int)
        ans = 0
        for n in nums2:
            divs[n*k]+=1
        for n in nums1:
            for d in range(1, int(sqrt(n))+1):
                if n%d==0:
                    if d in divs:
                        ans+=divs[d]
                    if n//d in divs and n//d!=d:
                        ans+=divs[n//d]
                    # if n//d==d:
                        # ans-=divs[d]
        return ans