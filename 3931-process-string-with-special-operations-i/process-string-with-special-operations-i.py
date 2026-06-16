class Solution:
    def processStr(self, s: str) -> str:
        ans = ""
        for ch in s:
            if ch == '*' and len(ans) >= 1:
                ans = ans[:-1]
            elif ch == '#' and len(ans) >= 1:
                ans += ans
            elif ch == '%':
                ans = ans[::-1]
            if 'a' <= ch <= 'z':
                ans += ch
        return ans