class Solution:
    def generate(self, n: int) -> List[List[int]]:
        rows = []
        for x in range(1,n+1):
            rows.append([0]*x)
        for i in range(0,n):
            for k in range(0,i+1):
                if (k == 0) or (k == i):
                    rows[i][k] = 1
                else:
                    rows[i][k] = rows[i-1][k] + rows[i-1][k-1]
        return rows

