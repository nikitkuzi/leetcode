# class Solution:
#     def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
#         def compare(gene1 , gene2): # return the number of different chars between 2 genes
#             diffNum = 0
#             for i in range(len(gene1)):
#                 if gene1[i] != gene2[i]:
#                     diffNum += 1
#             return diffNum
#
#         visited = set()
#         q = deque()
#         q.append([startGene, 0])
#         ansFound = False
#         while q:
#             cur, numChanges = q.popleft()
#             if cur == endGene:
#                 ansFound = True
#                 break
#             for gene in bank:
#                 if gene not in visited:
#                     if compare(cur, gene) == 1:
#                         visited.add(gene)
#                         q.append([gene, numChanges+1])
#         if ansFound == True:
#             return numChanges
#         else:
#             return -1


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank = set(bank)
        print(bank)
        visited = set()
        q = deque()
        q.append((startGene, 0))
        mn = 111111
        while q:
            gene, cnt = q.popleft()
            if gene == endGene:
                mn = min(mn, cnt)
            for i in range(8):
                for l in 'ACGT':
                    if l == gene[i]:
                        continue
                    new_gene = gene[:i] + l + gene[i + 1:]
                    # if new_gene == endGene:
                    # mn = min(mn,cnt)
                    # print(gene,new_gene,cnt,new_gene in bank)
                    if new_gene in bank and new_gene not in visited:
                        q.append((new_gene, cnt + 1))
                        visited.add(new_gene)

        # print(mn)
        if not bank or mn == 111111:
            return -1
        return mn
