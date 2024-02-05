# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        first = False
        while curr:
            div, curr.val = divmod(curr.val * 2, 10)
            if div:
                if prev:
                    prev.val += 1
                else:
                    first = True
            prev, curr = curr, curr.next
        return head if not first else ListNode(1, head)

