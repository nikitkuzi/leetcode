# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if not head.next.next:
            return head.val + head.next.val
        slow = head
        fast = head
        prev = None
        curr = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            curr.next, prev, curr  = prev, curr, curr.next
        # curr.next,prev,curr = prev,curr,curr.next
        mx = float(-inf)
        while prev:
            mx = max(mx, prev.val + slow.val)
            prev = prev.next
            slow = slow.next

        return mx
