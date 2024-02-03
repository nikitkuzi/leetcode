# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def reorderList(self, head: Optional[ListNode]) -> None:
#         """
#         Do not return anything, modify head in-place instead.
#         """
#         q = deque()
#         while head:
#             q.append(head)
#             head = head.next
#         ans = ListNode()
#         curr = ans
#         while len(q) >= 2:
#             first = q.popleft()
#             second = q.pop()
#             first.next = second
#             first.next.next = None
#             curr.next = first
#             curr = curr.next.next
#         if q:
#             curr.next = q.pop()
#             curr.next.next = None
#         return ans.next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # split node list into 2 halves
        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reverse second list
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # link first and second half
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
        return head