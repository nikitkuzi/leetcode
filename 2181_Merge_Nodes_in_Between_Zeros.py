# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
    # def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     curr = head.next
    #     while curr:
    #         sm = 0
    #         start = curr
    #         while start and start.val != 0:
    #             sm += start.val
    #             start = start.next
    #         curr.val = sm
    #         curr.next = start.next
    #         curr = curr.next
    #     return head.next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        val = 0
        tail = head
        cutOff = head
        curr = head
        while curr :
            val += curr.val
            if curr.val == 0 and val > 0:
                tail.val = val
                cutOff = tail
                tail = tail.next
                val = 0
            curr = curr.next
        cutOff.next = None
        return head
