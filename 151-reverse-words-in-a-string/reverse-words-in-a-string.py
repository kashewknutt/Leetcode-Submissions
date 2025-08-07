class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split(" ")
        new = [i for i in arr if i != ""]
        return " ".join(new[::-1])
        