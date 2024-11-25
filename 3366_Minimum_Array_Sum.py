class Solution:
    def minArraySum(self, nums: List[int], k: int, op1: int, op2: int) -> int:
        h = [-n for n in nums]
        heapq.heapify(h)
        while op1 and op2:
            curr = -heapq.heappop(h)
            first = False
            if (curr+1) // 2 >= k:
                curr = (curr+1) // 2
                op1 -= 1
                first = True
            elif curr >= k:
                curr -= k
                op2 -= 1
            if curr >= -h[0] and op1 and op2:
                if first:
                    if curr >= k:
                        cur -= k
                        op2 -= 1
                    else:
                        break
                else:
                    if curr > 1:
                        curr = (curr+1)//2
                        op1 -= 1
            heapq.heappush(h, -curr)
        while op1 and -h[0] > 1:
            curr = -heapq.heappop(h)
            curr = (curr+1)//2
            heapq.heappush(h, -curr)
            op1 -= 1
        while op2 and -h[0] >= k:
            curr = -heapq.heappop(h)
            curr -= k
            heapq.heappush(h, -curr)
            op2 -= 1
        return -sum(h)



