row = 5
col = 5

def isVaildCell(r,c):

        #check (r-2,c) == (r-1,c) == (r,c) or (r,c) == (r+1,c) == (r+2,c) or (r,c) == (r,c+1) == (r,c+2) or (r,c)==(r,c-1)==(r,c-2)

        row_false_count = 0
        col_false_count = 0
        for i in range(r - 2, r + 1):
            if(not(i<0 or i >= row)):
                if not (i + 1 >= row) and (curr[i][c] != curr[i + 1][c]) or (not (i + 2 >= row) and (curr[i][c] != curr[i + 2][c])) or (not (i + 2 >= col) and (curr[i + 1][c] != curr[i + 2][c])):
                    pass

                else:
                    if not(i+2>= col):
                        return False

        # check 3 cell by colume
        for j in range(c - 2, c + 1):
            if(not(j<0 or j >= col)):
                if (not (j + 1 >= col) and (curr[r][j] != curr[r][j+1])) or (not (j + 2 >= col) and (curr[r][j] != curr[r][j+2])) or (not (j + 2 >= col) and (curr[r][j+1] != curr[r][j+2])):
                    pass
                else:
                    if not(j+2>= row):
                        return False
        return True

curr = [[0,0,1,0,0]
       ,[0,0,0,0,0]
       ,[1,1,0,1,1]
       ,[0,0,1,0,0]
       ,[0,0,1,0,0]]

print(isVaildCell(2,4))
