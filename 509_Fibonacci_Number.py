class Solution:
    def fib(self, n: int) -> int:
        mylist = [-1]*(n+1)
        mylist[0] = 0
        if n > 0:
            mylist[1] = 1
            for j in range(2, n+1):
                mylist[j] = mylist[j-1] + mylist[j-2]
        return mylist[n]