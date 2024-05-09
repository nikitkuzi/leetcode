class Solution:
    def minOperations(self, k: int) -> int:
        if k == 1:
            return 0
        mn = k
        count = 0
        last_num = 1
        while mn >= (k - count + last_num - 2) // last_num + count:
            last_num += 1
            count += 1

            mn = min(mn, (k - count + last_num - 2) // last_num + count)
            # print(last_num, current_sum, (k-current_sum+last_num-1)//last_num, count, mn)

        return mn
