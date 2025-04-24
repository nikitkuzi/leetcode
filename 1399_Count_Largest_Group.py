
class Solution:
    def countLargestGroup(self, n):
        categorii=[0]*37 #ignor 0. am 36 de categorii
        tablouSumaCifrelor=[0]*(n+1)
        for i in range(1,n+1):
            sc=i%10+tablouSumaCifrelor[i//10]
            tablouSumaCifrelor[i]=sc
            categorii[sc] += 1
        valMax=max(categorii)
        nrGrupuri=categorii.count(valMax)
        return nrGrupuri
#sol=Solution()
#print(sol.countLargestGroup(13))