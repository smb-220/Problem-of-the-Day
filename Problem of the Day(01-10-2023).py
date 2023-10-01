class Solution:
    def BoundaryTraversal(self,matrix, n, m):
        output = []
        
        if(n == 1):
            i = 0;
            while i < m:
                output.append(matrix[0][i])
                i+=1
        elif(m == 1):
            i = 0;
            while i < n:
                output.append(matrix[i][0])
                i+=1
        else:
            
            row_ind = 0
            col_ind = 0
            while col_ind < m:
                output.append(matrix[row_ind][col_ind])
                col_ind+=1
    
            col_ind = m-1
            row_ind += 1
            while row_ind < n:
                output.append(matrix[row_ind][col_ind])
                row_ind += 1
    
            row_ind = n-1
            col_ind -= 1
            while col_ind > -1:
                output.append(matrix[row_ind][col_ind])
                col_ind -= 1
    
            col_ind = 0
            row_ind -= 1
            while row_ind > 0:
                output.append(matrix[row_ind][col_ind])
                row_ind -= 1
    
        return output
