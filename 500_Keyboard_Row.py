class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        s1 = set("qwertyuiop")
        s2 = set("asdfghjkl")
        s3 = set("zxcvbnm")
        r = []
        for word in words:
            word_set = set(word.lower())  # Converte la parola in minuscolo e crea un insieme
            if word_set.issubset(s1) or word_set.issubset(s2) or word_set.issubset(s3):
                r.append(word)
        return r