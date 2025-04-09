# class Solution:
#     def minimumOperations(self, nums: List[int]) -> int:
#         seen = set()
#         for i in range(len(nums) - 1,  -1, -1):
#             if nums[i] in seen:
#                 return i // 3 + 1
#             seen.add(nums[i])
#         return 0
#         # c = defaultdict(list)
#         # for i, n in enumerate(nums):
#         #     c[n].append(i)
#         # mx = -1
#         # for num in c.keys():
#         #     if len(c[num])>1:
#         #         mx = max(mx, c[num][-2])
#         # # print(mx)
#         # return (mx) // 3+1
import re
with open(r'C:\Users\nikit\Downloads/test_delete.txt') as file:
    f = file.readline()
# email = '(?=([a-zA-Z]([a-zA-Z0-9]*(\\.[a-zA-Z0-9])?)*@(yandex.ru)|(gmail.com)))'
# email = '[a-zA-Z]([a-zA-Z0-9]*(\\.[a-zA-Z0-9])?)*@[a-z]+\\.[a-z]+'
num = '([12][012]*|0)'
email = rf'{num}[+*]{num}'
mx = 0
# f = 'alex@@s..ch@gmail.com.runet@yandex.rubo@yandex.ru'
print(len(f))

for line in re.finditer(email,f):
    # print(line.group(1))
    mx = max(len(line.group(0)), mx)
print(mx)