# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        d = set(nums)
        dummy = ListNode()
        dummy.next = head
        curr = head
        prev = dummy
        while prev and curr:
            if curr.val in d:
                prev.next = curr.next
            else:
                prev = prev.next
            curr = curr.next
        return dummy.next

