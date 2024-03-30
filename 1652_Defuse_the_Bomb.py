class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        temp = code[-abs(k):] + code + code[:abs(k)]
        for i in range(len(code)):
            if k>0:
                # print(temp[i+k+1:i+2*k+1])
                code[i] = sum(temp[i+k+1:i+2*k+1])
            elif k < 0:
                # print(temp[i:i-k])
                code[i] = sum(temp[i:i-k])
            else:
                code[i] = 0
        return code

