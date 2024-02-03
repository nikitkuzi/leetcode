# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy = ListNode(0,head)
        prev = head
        curr = head.next
        prev.next = curr.next
        curr.next = prev
        prev = curr.next.next
        curr = prev.next
        print(prev)
        print(curr)
        print(head)
        print(dummy)
#         dummy = ListNode(0)
#         dummy.next = head
#         curr = dummy
#         while curr.next and curr.next.next:
#             curr.next,curr.next.next,curr.next.next.next = curr.next.next,curr.next,curr.next.next.next
#             curr = curr.next.next
#         return dummy.next
# class Solution:
#     def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         dummy = ListNode(-1, head)
#         prev, cur = dummy, head
#         while cur and cur.next:
#             prev.next = cur.next
#             cur.next = cur.next.next
#             prev.next.next = cur
#             prev, cur = cur, cur.next
#         return dummy.next