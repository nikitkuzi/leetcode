# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
#         q = deque()
#         q.append(root)
#         sms = []
#         sm = 0
#         lvl = 0
#         while q:
#             lvl_len = len(q)
#             sm = 0
#             for i in range(lvl_len):
#                 curr = q.popleft()
#                 sm += curr.val
#                 if curr.left:
#                     q.append(curr.left)
#                 if curr.right:
#                     q.append(curr.right)
#             sms.append(sm)
#         sms.append(0)
#         q.append(root)
#         lvl = 0
#         while q:
#             lvl_len = len(q)
#             lvl += 1
#             for i in range(lvl_len):
#                 curr = q.popleft()
#                 # print(lvl,sms[lvl], curr)
#                 # print(curr.left)
#                 # print(curr.right)
#                 # print()
#                 if curr.left and curr.right:
#                     curr.left.val, curr.right.val = sms[lvl] - curr.right.val - curr.left.val, sms[
#                         lvl] - curr.left.val - curr.right.val
#                     q.append(curr.left)
#                     q.append(curr.right)
#                 elif curr.left:
#                     curr.left.val = sms[lvl] - curr.left.val
#                     q.append(curr.left)
#                 elif curr.right:
#                     curr.right.val = sms[lvl] - curr.right.val
#                     q.append(curr.right)
#         root.val = 0
#         # print(root)
#         return root
#
#
#
#
#
from collections import deque

class Solution:
    def replaceValueInTree(self, root):
        if root is None:
            return root

        nodeQueue = deque()
        nodeQueue.append(root)
        previousLevelSum = root.val

        while nodeQueue:
            levelSize = len(nodeQueue)
            currentLevelSum = 0

            for _ in range(levelSize):
                currentNode = nodeQueue.popleft()
                # Update node value to cousin sum
                currentNode.val = previousLevelSum - currentNode.val

                # Calculate sibling sum
                siblingSum = (0 if currentNode.left is None else currentNode.left.val) + \
                             (0 if currentNode.right is None else currentNode.right.val)

                if currentNode.left is not None:
                    currentLevelSum += currentNode.left.val  # Accumulate current level sum
                    currentNode.left.val = siblingSum  # Update left child's value
                    nodeQueue.append(currentNode.left)  # Add to queue for next level
                if currentNode.right is not None:
                    currentLevelSum += currentNode.right.val  # Accumulate current level sum
                    currentNode.right.val = siblingSum  # Update right child's value
                    nodeQueue.append(currentNode.right)  # Add to queue for next level

            previousLevelSum = currentLevelSum  # Update previous level sum for next iteration

        return root