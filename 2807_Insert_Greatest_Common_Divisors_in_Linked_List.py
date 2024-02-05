# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head
        curr = head
        while curr and curr.next:
            g = gcd(curr.val,curr.next.val)
            curr.next = ListNode(g,curr.next)
            curr = curr.next.next
        return head