class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        c = 0
        vovels = set("aeuoi")
        for i in range(k):
            if s[i] in vovels:
                c+= 1
        mx = c
        for i in range(k,len(s)):
            if s[i] in vovels:
                c+=1
            if s[i-k] in vovels:
                c-=1
            if c > mx:
                mx = c
        return mx

d = dict(one = 1, two = 2, three = "3", four = "4")
d2 = {2: "неудовлетворительно", 3: "удовлетворительно", 'four': "хорошо", 5: "отлично"}
d.update(d2)
print(d,d2)