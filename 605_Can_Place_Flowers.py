class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        b = 0
        c = 0
        # for i,f in enumerate(flowerbed):
        #     b += f* 2**(len(flowerbed)-1-i)
        #     if f:
        #         c+=1
        if n == 0:
            return True
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
                flowerbed[i] = 1
                n -= 1
                if n == 0:
                    return True
        return False