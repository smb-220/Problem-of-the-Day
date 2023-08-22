#Surround the 1's

class Solution:
    def Count(self, matrix):
        n = len(matrix)
        m = len(matrix[0])
        ans = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j]:
                    c = 0
                    if i - 1 >= 0:
                        c += matrix[i-1][j] == 0
                    if i + 1 < n:
                        c += matrix[i+1][j] == 0
                    if j - 1 >= 0:
                        c += matrix[i][j-1] == 0
                    if j + 1 < m:
                        c += matrix[i][j+1] == 0
                    if i - 1 >= 0 and j - 1 >= 0:
                        c += matrix[i-1][j-1] == 0
                    if i - 1 >= 0 and j + 1 < m:
                        c += matrix[i-1][j+1] == 0
                    if i + 1 < n and j - 1 >= 0:
                        c += matrix[i+1][j-1] == 0
                    if i + 1 < n and j + 1 < m:
                        c += matrix[i+1][j+1] == 0
                    if not (c & 1) and c:
                        ans += 1
        return ans
