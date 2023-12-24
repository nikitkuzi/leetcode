class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        if m > n:
            nums1,nums2 = nums2,nums1
            n,m = m,n
        # print(n,n//2,n//2+1)
        # if m == 0:
            # return nums2[n//2] if n%2 else (nums2[n//2]+nums2[n//2-1])/2
        N = m+n
        l = 0
        r = m
        while l<=r:
            mid = (l+r)//2
            a = ((N+1)//2)-mid
            x1 = nums1[mid-1] if mid != 0 else float('-inf')
            x2 = nums1[mid] if mid!=m else float("inf")
            y1 = nums2[a-1] if a!=0 else float("-inf")
            y2 = nums2[a] if a!=n else float("inf")
            # print(x1,x2,y1,y2)
            # if x1 >= y1 and x1 <= y2:
            if x1<=y2 and y1<=x2:
                if N%2:
                    # print("here",x1)
                    return max(x1,y1)
                else:
                    # print("here1",(x1+min(x2,y2))/2)
                    return (max(x1,y1)+min(x2,y2))/2
            elif x1 > y2:
                r = mid-1
            else:
                l = mid+1

