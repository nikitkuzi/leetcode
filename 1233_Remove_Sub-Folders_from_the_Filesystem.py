class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        result = []
        prev = ''
        for path in folder:
            if not prev or not path.startswith(prev +'/'):
                result.append(path)
                prev = path  # Update 'prev' to the current folder
        return result
# # class Solution:
# #     def removeSubfolders(self, folder: List[str]) -> List[str]:
# #         trie = {}
# #         for path in folder:
# #             curr = trie
# #             f = True
# #             for c in path.split('/'):
# #                 if c not in curr:
# #                     curr[c] = {}
# #                 curr = curr[c]
# #             curr["#"] = "#"
# #         res = 0
# #         ans = []
# #         for path in folder:
# #             curr = trie
# #             f = True
# #             for c in path.split('/'):
# #                 if '#' in curr:
# #                     f = False
# #                     break
# #                 curr = curr[c]
# #             if f:
# #                 ans.append(path)
# #         return ans
# class Solution:
#     def removeSubfolders(self, folder: List[str]) -> List[str]:
#         trie = {}
#         test = []
#         for path in folder:
#             curr = trie
#             f = True
#             for c in path.split('/'):
#                 if '#' in curr:
#                     f = False
#                     break
#                 if c not in curr:
#                     curr[c] = {}
#                 curr = curr[c]
#             if f:
#                 curr["#"] = "#"
#                 test.append(path)
#         res = 0
#         ans = []
#         for path in test:
#             curr = trie
#             f = True
#             for c in path.split("/"):
#                 if '#' in curr:
#                     f = False
#                     break
#                 curr = curr[c]
#             if f:
#                 ans.append(path)
#         return ans