class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1
        i = 0
        last_inserted = 0
        char = ''
        while i < len(chars):
            rep_count = 1
            char = chars[i]
            while i < len(chars)-1 and chars[i] == chars[i+1]:
                rep_count +=1
                i+=1
            chars[last_inserted] = char
            rep_count = str(rep_count)
            if int(rep_count) > 1:
                for j in range(len(rep_count)):
                    last_inserted +=1
                    chars[last_inserted] = rep_count[j]
                    # print(chars)
            last_inserted+=1
            i+=1
        while len(chars)!=last_inserted:
            chars.pop()
        return len(chars)