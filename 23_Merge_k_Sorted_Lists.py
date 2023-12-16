# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # node = ListNode()
        # def merge(lists):
        # node = ListNode()
        if not lists:
            # return ListNode()
            return
        if len(lists) == 1:
            return lists[0]

        left = self.mergeKLists(lists[:len(lists) // 2])
        right = self.mergeKLists(lists[len(lists) // 2:])
        # print(left)
        # print(right)
        # print("end")
        # ans = ListNode()
        curr = ListNode()
        ans = curr
        while left and right:
            if left.val < right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next
        curr.next = left or right
        # print(ans.next)
        # return ans.next
        return ans.next
