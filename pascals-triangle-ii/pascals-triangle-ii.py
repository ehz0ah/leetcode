class Solution:
    def getRow(self, n: int) -> List[int]:
        rows = []
        for x in range(0,n+1):
            rows.append([0]*(x+1))
            
        for i in range(0,n+1):
            for k in range(0,i+1):
                if (k == 0) or (k == i):
                    rows[i][k] = 1
                else:
                    rows[i][k] = rows[i-1][k] + rows[i-1][k-1]
        return rows[n]
