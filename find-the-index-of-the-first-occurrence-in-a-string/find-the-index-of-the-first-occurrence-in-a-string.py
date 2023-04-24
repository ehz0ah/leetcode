class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1 
        if needle in haystack:
            return haystack.index(needle)


            