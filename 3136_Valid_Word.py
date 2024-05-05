class Solution:
    def isValid(self, word: str) -> bool:
        if len(word)<3 or '@' in word or '#' in word or '$' in word:
            return False
        v=0
        c=0
        word=word.lower()
        for i in word:
            if i in 'aeiou':
                v=1
            elif ord(i)>97 and ord(i)<123:
                c=1
            if c and v:
                return True
        return False