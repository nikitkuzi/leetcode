# Definition for singly-linked list.
from typing import Optional


class Node:

    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to reverse the linked list

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Utility function to print the LinkedList
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            temp = temp.next




class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        _ = head
        n = 0
        while _:
            n += 1
            _ = _.next
        # for i in range(n//k):
        ans = ListNode(0)
        ans.next = head
        prev = ans

        for i in range(n // k):

            current = prev.next

            for _ in range(k - 1):
                next_node = current.next
                current.next, prev.next, next_node.next = next_node.next, next_node, prev.next
            prev = current
        return ans.next



# Driver code
llist = LinkedList()
llist.push(1)
llist.push(2)
llist.push(3)
llist.push(4)
llist.push(5)
print(llist.next)
llist.printList()
k = 2
test = Solution()
llist = test.reverseKGroup(llist, k)
llist.printList()