class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        placeholder = ''
        for i in digits:
            placeholder += str(i)
        new_digit = int(placeholder) + 1
        return [int(x) for x in list(str(new_digit))]
        

