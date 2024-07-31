# class Solution:
#
#     def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
#
#         n = len(books)
#
#         f = [0] * (n + 1)
#
#         for i, (w, h) in enumerate(books, 1):
#
#             f[i] = f[i - 1] + h
#
#             for j in range(i - 1, 0, -1):
#
#                 w += books[j - 1][0]
#
#                 if w > shelfWidth:
#
#                     break
#
#                 h = max(h, books[j - 1][1])
#
#                 f[i] = min(f[i], f[j - 1] + h)
#
#         return f[n]
class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_wdth: int) -> int:

        @lru_cache(None)
        def dfs(i: int, wdth: int, hght: int)-> int:

            if i == len(books): return 0

            bookwdth, bookhght = books[i]
            wdth+= bookwdth
            ans = inf

            if wdth <= shelf_wdth:

                if bookhght <= hght:
                    ans = dfs(i+1, wdth,  hght)
                else:
                    ans = min(ans, bookhght - hght + dfs(i+1, wdth,  bookhght))

            return min(ans, bookhght + dfs(i+1, bookwdth, bookhght))


        return dfs(0, 0, 0)