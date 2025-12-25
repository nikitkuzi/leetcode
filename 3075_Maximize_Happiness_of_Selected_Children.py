class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        shift = 0
        sm = 0
        for i in range(len(happiness)-1, len(happiness)-k-1,-1):
            if happiness[i]-shift>=0:
                sm += happiness[i]-shift
                shift+=1
            else:
                break
        return sm
