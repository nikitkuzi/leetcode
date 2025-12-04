class Solution:
    def countCollisions(self, directions: str) -> int:
        st = []
        res = 0
        for d in directions:
            if d == 'L' and not st:
                continue
            if d == 'R':
                st.append(d)
            if d == 'S':
                while st and st[-1] == 'R':
                    res+=1
                    st.pop()
                st.append(d)
            if d == "L":
                if st[-1] == 'S':
                    res+=1
                else:
                    st.pop()
                    res+=2
                    while st and st[-1] == 'R':
                        st.pop()
                        res+=1
                    st.append("S")
        return res


