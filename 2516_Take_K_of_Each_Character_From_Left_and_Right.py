class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        c = Counter(s)
        if k == 0:
            return 0
        if 'a' not in c or 'b' not in c or 'c' not in c:
            return -1
        if c['a'] < k or c['b'] < k or c['c'] < k:
            return -1

        def f(s, counter):
            if not s:
                return inf
            if counter['a'] >= k and counter['b'] >= k and counter['c'] >= k:
                return 0
            res = inf
            counter[s[0]] += 1
            res = min(res, f(s[1:], counter) + 1)
            counter[s[0]] -= 1
            counter[s[-1]] += 1
            res = min(res, f(s[:-1], counter) + 1)
            counter[s[-1]] -= 1
            return res

        counter = defaultdict(int)
        return f(s, counter)