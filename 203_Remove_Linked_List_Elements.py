# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        curr = dummy
        while curr and curr.next:
            while curr.next and curr.next.val == val:
                curr.next = None if not curr.next else curr.next.next
            curr = curr.next
        return dummy.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
#         dummy = ListNode(next=head)
#         prev = dummy
#         curr = head
#         while curr:
#             nxt = curr.next
#             if curr.val == val:
#                 prev.next = nxt
#             else:
#                 prev = curr
#             curr = nxt
#         return dummy.next