class Solution:
    def isValid(self, s: str) -> bool:
        hm = {")": "(", "]": "[", "}": "{"}
        st = []
        for i in s:
            if i in hm:
                if st and st[-1] == hm[i]:
                    st.pop()
                else:
                    return False
            else:
                st.append(i)
        if not st:
            return True
        else:
            return False