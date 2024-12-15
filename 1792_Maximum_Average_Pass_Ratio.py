# import heapq
# class Solution:
#     def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
#         if len(classes) == 1:
#             return (classes[0]+extraStudents)/(classes[1]+extraStudents)
#         h = []
#         for p, t in classes:
#             heapq.heappush(h, (p/t, p,t))
#         print(h)
#         while extraStudents:
#             _, p, t = heapq.heappop(h)
#             # print(f"curr, delta={p/t}, p={p}, t={t}")
#             next_delta = (h[0][1]+1)/(h[0][2]+1)-h[0][0]
#             p+=1
#             t+=1
#             extraStudents-=1
#             # while extraStudents and ((p+1)/(t+1)-(p/t)) > next_delta:
#                 # p+=1
#                 # t+=1
#                 # extraStudents-=1
#             heapq.heappush(h, (p/t, p, t))
#         print(h)
#         return sum(curr[0] for curr in h)/len(classes)

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        import heapq

        def gain(pass_, total):
            return (pass_ + 1) / (total + 1) - pass_ / total

        max_heap = []
        sum_ = 0.0

        for pass_, total in classes:
            sum_ += pass_ / total
            heapq.heappush(max_heap, (-gain(pass_, total), pass_, total))

        while extraStudents:
            current_gain, pass_, total = heapq.heappop(max_heap)
            sum_ -= pass_ / total
            pass_ += 1
            total += 1
            extraStudents -= 1
            while extraStudents and gain(pass_, total) >= -max_heap[0][0]:
                pass_ += 1
                total += 1
                extraStudents -= 1
            sum_ += pass_ / total
            heapq.heappush(max_heap, (-gain(pass_, total), pass_, total))

        return sum_ / len(classes)