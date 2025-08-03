class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        arr = haystack.split(needle)
        if arr == [haystack]:
            return -1
        else:
            return len(arr[0])
        