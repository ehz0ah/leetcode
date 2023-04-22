class Solution:
    def isValid(self, s: str) -> bool:
        dict_brackets = {'(':')', '[':']','{':'}'}
        placeholder = []
        if len(s) % 2 != 0:
            return False
        for brac in s:
            if brac in dict_brackets:
                placeholder.append(brac)
            elif len(placeholder) == 0 or dict_brackets[placeholder.pop()] != brac:
                return False
        return len(placeholder) == 0
         
     

            
             


