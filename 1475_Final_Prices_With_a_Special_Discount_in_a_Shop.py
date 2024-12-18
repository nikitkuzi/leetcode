class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        st = []
        res = [0]*len(prices)
        for r in range(len(prices)):
            # print(st)
            while st and prices[st[-1]] >= prices[r]:
                pos = st.pop()
                res[pos] = prices[pos]-prices[r]
            st.append(r)
        while st:
            pos = st.pop()
            res[pos] = prices[pos]
        return res