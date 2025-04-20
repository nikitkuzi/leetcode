import math
from collections import Counter

class Solution:
    def numRabbits(self, answers):
        f = Counter(answers)
        res = 0
        for ans, count in f.items():
            if ans == 0:
                res += count
            else:
                res += math.ceil(count / (ans + 1)) * (ans + 1)
        return res