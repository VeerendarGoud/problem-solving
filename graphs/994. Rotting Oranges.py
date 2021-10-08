
def orangesRotting(grid) -> int:
    dist = 0
    queue = []
    fresh_queue = 0
    height = len(grid)
    width = len(grid[0])
    
    for i in range(height):
        for j in range(width):
            if grid[i][j] == 2:
                queue.append([[i,j],dist])
            elif grid[i][j] == 1:
                fresh_queue +=1
                
    for [row,col],dist in queue:
        for idx,idy in (0,1),(0,-1),(1,0),(-1,0):
            
            nr = row+idx
            nc = col+idy
            
            if 0<= nr < height and 0<= nc < width and grid[nr][nc] == 1:
                queue.append([[nr,nc],dist+1])
                grid[nr][nc] = 2
                fresh_queue -=1

    if fresh_queue > 0:
        return -1
    else:   
        return dist

grid = [[2,1,1],[1,1,0],[0,1,1]]
grid = [[2,1,1],[0,1,1],[1,0,1]]
grid = [[0]]
print(orangesRotting(grid))