#542. 01 Matrix
def updateMatrix(mat):
        
    height = len(mat)
    width = len(mat[0])
    
    queue = []
    
    for i in range(height):
        for j in range(width):
            if mat[i][j] == 0:
                queue.append([i,j])
            else:
                mat[i][j] = '#'
    
    for row,col in queue:
        
        for idx,idy in (0,1),(0,-1),(-1,0),(1,0):
            
            nr = row + idx
            nc = col + idy
            
            if 0 <= nr < height and 0 <= nc < width and mat[nr][nc] == '#':
                
                mat[nr][nc] = mat[row][col] + 1
                
                queue.append([nr,nc])
                
    return mat

    
def matrix_shortest_path(mat):

    visited = dict()
    R,C = len(mat),len(mat[0])

    new_mat = []

    for i in range(R):
        row = [0]*C
        for j in range(C):
            if mat[i][j] == 1:
                if (i,j) in visited:
                    row[j] = visited[(i,j)]
                else:
                    row[j] = shortest_path(mat,[i,j],visited)
                    #visited[(i,j)] = row[j]
                #row[j] = shortest_path(mat,[i,j],visited)
        
        new_mat.append(row)
    #print(visited)
    return new_mat


def shortest_path(matrics,source,visited):

    R,C = len(matrics),len(matrics[0])

    queue = [[source,0]]

    while len(queue) > 0:

        [[r,c],curr_dist] = queue.pop(0)

        if matrics[r][c] == 0:
            return curr_dist

        if r-1 >=0:
            queue.append([[r-1,c],curr_dist+1])
        if r+1 < R:
            queue.append([[r+1,c],curr_dist+1])
        if c-1 >=0:
            queue.append([[r,c-1],curr_dist+1])
        if c+1 < C:
            queue.append([[r,c+1],curr_dist+1])
        
    return -1

# matrics =  [[0,0,0],[0,1,0],[0,0,0]]
# source = [1,1]
# print(shortest_path(matrics,source))

# matrics = [[0,0,0],[0,1,0],[1,1,1]]
# source = [2,1]
# print(shortest_path(matrics,source))

# matrics = [[0,1,1],[1,1,1],[1,1,1]]
# source = [2,2]
# print(shortest_path(matrics,source))

mat = [[0,0,0],[0,1,0],[0,0,0]]
mat = [[0,0,0],[0,1,0],[1,1,1]]
mat = [[0,0,1],[1,1,1],[1,1,1]]
mat = [[1,0,1,1,0,0,1,0,0,1],[0,1,1,0,1,0,1,0,1,1],[0,0,1,0,1,0,0,1,0,0],[1,0,1,0,1,1,1,1,1,1],[0,1,0,1,1,0,0,0,0,1],[0,0,1,0,1,1,1,0,1,0],[0,1,0,1,0,1,0,0,1,1],[1,0,0,0,1,1,1,1,0,1],[1,1,1,1,1,1,1,0,1,0],[1,1,1,1,0,1,0,0,1,1]]
expt = [[1,0,1,1,0,0,1,0,0,1],[0,1,1,0,1,0,1,0,1,1],[0,0,1,0,1,0,0,1,0,0],[1,0,1,0,1,1,1,1,1,1],[0,1,0,1,1,0,0,0,0,1],[0,0,1,0,1,1,1,0,1,0],[0,1,0,1,0,1,0,0,1,1],[1,0,0,0,1,2,1,1,0,1],[2,1,1,1,1,2,1,0,1,0],[3,2,2,1,0,1,0,0,1,1]]
result = matrix_shortest_path(mat)
print(result)
#print([[1,0,1,1,0,0,1,0,0,1],[0,1,1,0,1,0,1,0,1,1],[0,0,1,0,1,0,0,1,0,0],[1,0,1,0,1,1,1,1,1,1],[0,1,0,1,1,0,0,0,0,1],[0,0,1,0,1,1,1,0,1,0],[0,1,0,1,0,1,0,0,1,1],[1,0,0,0,1,2,1,1,0,1],[2,1,1,1,1,2,1,0,1,0],[3,2,2,1,0,1,0,0,1,1]])
print(expt==result)
