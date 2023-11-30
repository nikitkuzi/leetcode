class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="" : return ""

        t_counter , window = {} , {}

        for x in t:
            t_counter[x] = 1 + t_counter.get(x , 0)

        have , need = 0 , len(t_counter)
        ans , ans_size = [-1 , -1] , float("infinity")
        left = 0

        for right in range(len(s)):
            window[s[right]] = 1 + window.get(s[right] , 0)

            if s[right] in t_counter and window[s[right]] == t_counter[s[right]] :
                have += 1

            while have == need :
                if (right - left + 1) < ans_size:
                    ans = [left , right]
                    ans_size = (right - left + 1)

                window[s[left]] -= 1
                if s[left] in t_counter and window[s[left]] < t_counter[s[left]] :
                    have -= 1
                left += 1

        return s[ans[0] : ans[1]+1] if ans_size != float("infinity") else ""


test = Solution()
a = ["ADOBECODEBANC", "a", "a"]
b = ["ABC", "a", "aa"]
# for s,t in zip(a,b):
#     print(test.minWindow(s, t))
print(test.minWindow(a[-1], b[-1]))