# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        placeholder = ListNode()
        tail = placeholder
        while list1 or list2:
            h1 = list1.val if list1 is not None else 51
            h2 = list2.val if list2 is not None else 51
            if h1 < h2:
                tail.next = ListNode(h1)
                ans = ans.next
                list1 = list1.next if list1 is not None else 51
            else:
                tail.next = ListNode(h2)
                ans = ans.next
                list2 = list2.next if list2 is not None else 51
        return placeholder.next