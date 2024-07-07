class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        curr=defaultdict(int)
        total_count=0
        for i in nums:
            new_curr=defaultdict(int)
            for j in curr:
                new_curr[j&i]+=curr[j]
            new_curr[i]+=1
            curr=new_curr
            total_count+=curr[k]
        return total_count