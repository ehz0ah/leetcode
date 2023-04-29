class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s2 = s.split(" ")
        s3 = s2[::-1]
        while s3[0] == "":
            s3.pop(0)
        return len(s3[0])


        