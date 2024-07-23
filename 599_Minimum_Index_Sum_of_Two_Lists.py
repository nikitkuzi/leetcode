class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d = {list1[i]:i for i in range(len(list1))}
        mn = []
        mni = inf
        for i in range(len(list2)):
            if list2[i] in d:
                if mni > i+d[list2[i]]:
                    mni = i+d[list2[i]]
                    mn = [list2[i]]
                elif mni == i+d[list2[i]]:
                    mn.append(list2[i])
        return mn