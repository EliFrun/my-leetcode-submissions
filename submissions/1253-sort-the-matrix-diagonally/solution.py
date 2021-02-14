class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat[0])
        n = len(mat)
        for i in range(n):
            my_list = []
            for j in range(min(n-i, m)):
                my_list.append(mat[i + j][j])
               
            my_list.sort()
            for j in range(min(n - i, m)):
                mat[i + j][j] = my_list[j]
                
            print(str(my_list))
                
        for i in range(m):
            my_list = []
            for j in range(min(n, m - i)):
                my_list.append(mat[j][i + j])
               
            my_list.sort()
            for j in range(min(n, m-i)):
                mat[j][i + j] = my_list[j]
                
            print(str(my_list))
                
        return mat
        
