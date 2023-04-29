class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        i, j, carry = len(a) - 1, len(b) - 1, 0
        # the while loop ensures that all elements in i and j is iterated through and the carry is to ensure that the very last part when carry = 1 if there is is added to the equation.
        while i >= 0 or j >= 0 or carry:
          # carry on value must initially be equal to total so that it will be added
          total = carry
          if i >= 0:
            total += int(a[i])
            i -= 1
          if j >= 0:
            total += int(b[j])
            j -= 1
            # this is technically if 1+1 then carry 1 print 0 then if 0+1 then carry 0 print 1
          result.append(str(total % 2))
          carry = total // 2
          # since i and j is initially from the back we have to reversed it and join it to make it a string from a list
        return ''.join(reversed(result))