# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:

#     def __init__(self, head: Optional[ListNode]):
#         self.head = []
#         while head:
#             self.head.append(head.val)
#             head = head.next

#     def getRandom(self) -> int:
#         return choice(self.head)


# # Your Solution object will be instantiated and called as such:
# # obj = Solution(head)
# # param_1 = obj.getRandom()
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import random as r;  # random = r.randint(0, x)   inclusive


class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.frequencies = {}
        self.total = 0

        node = head
        while (node):
            if node.val in self.frequencies:
                self.frequencies[node.val] += 1
            else:
                self.frequencies[node.val] = 1

            node = node.next
            self.total += 1

        cdf_val = 0

        for val in self.frequencies:
            cdf_val += self.frequencies[val] / self.total
            self.frequencies[val] = cdf_val

    def getRandom(self) -> int:
        return_val = None
        min_frequency = 1  # we need to find the minimum of the CDF to account for the first case
        min_key = 0

        val = r.random()  # value from 0 to 1
        for key, value in self.frequencies.items():
            if (val <= value):
                return_val = key
                return key

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()