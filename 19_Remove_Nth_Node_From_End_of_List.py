# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ans = ListNode()
        ans.next = head
        curr = head
        k = 0
        while curr:
            k+=1
            curr = curr.next
        curr = ans
        for _ in range(k-n):
            curr = curr.next
        curr.next = curr.next.next if curr.next is not None else None
        return ans.next