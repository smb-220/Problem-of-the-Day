#Find the string in grid
class Solution:
    def search2D(self, grid, row, col, word, x, y):
        R = len(grid)
        C = len(grid[0])
        
        if grid[row][col] != word[0]:
            return False
        
        length = len(word)
        
        for direction in range(8):
            k, rd, cd = 1, row + x[direction], col + y[direction]
            
            while k < length:
                if rd >= R or rd < 0 or cd >= C or cd < 0:
                    break
                
                if grid[rd][cd] != word[k]:
                    break
                
                rd += x[direction]
                cd += y[direction]
                k += 1
            
            if k == length:
                return True
        
        return False
    
    def searchWord(self, grid, word):
        row = len(grid)
        col = len(grid[0])
        x = [-1, -1, -1, 0, 0, 1, 1, 1]
        y = [-1, 0, 1, -1, 1, -1, 0, 1]
        ans = []
        
        for i in range(row):
            for j in range(col):
                if self.search2D(grid, i, j, word, x, y):
                    ans.append([i, j])
        
        return ans