class Solution:
    def getRow(self, n: int) -> List[int]:
        ## prev = [1]
        ## curr = [1,1]
        if n == 0:
            return [1]
        if n == 1:
            return [1,1]
        # for i in range(2,n+1):
        prev = self.getRow(n-1)
        curr = [1]
        for j in range(1,n):
            curr.append(prev[j-1] + prev[j])
        curr.append(1)
        return curr
        
