class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = {}
        for path in folder:
            curr = trie
            f = True
            for c in path.split('/'):
                if c not in curr:
                    curr[c] = {}
                curr = curr[c]
            curr["#"] = "#"
        res = 0
        ans = []
        for path in folder:
            curr = trie
            f = True
            for c in path.split('/'):
                if '#' in curr:
                    f = False
                    break
                curr = curr[c]
            if f:
                ans.append(path)
        return ans