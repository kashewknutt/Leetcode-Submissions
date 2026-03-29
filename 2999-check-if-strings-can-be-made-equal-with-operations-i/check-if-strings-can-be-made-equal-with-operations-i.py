class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        l1 = list(s1)
        l2 = list(s2)
        if s1 == s2:
            return True
        l1[0],l1[2] = l1[2],l1[0]
        if l1 == l2:
            return True
        l1[1],l1[3] = l1[3],l1[1]
        if l1 == l2:
            return True
        l1[0],l1[2] = l1[2],l1[0]
        if l1 == l2:
            return True
        return False
        
        