class Solution:
    def isPalindrome(self, x: int) -> bool:
        integer_string = str(x)
        if integer_string[::-1] == integer_string:
            return True 