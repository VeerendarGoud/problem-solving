def count_loops(grid,sr,sc):

    count1,count2,count3,count4 = 0,0,0,0

    R,C = len(grid),len(grid[0])

    if grid[sr][sc] == 2:
        return 0

    if grid[sr][sc] == 1:
        grid[sr][sc] = 2
        if sr+1 < R:
            count1 = count_loops(grid,sr+1,sc)
        if sr-1 >=0:
            count2 = count_loops(grid,sr-1,sc)
        if sc-1 >= 0:
            count3 = count_loops(grid,sr,sc-1)
        if sc+1 < C:
            count4 = count_loops(grid,sr,sc+1)

    print(count1,count2,count3,count4)

    return max(count1,count2,count3,count4)+1

grid = [[2,1,1],[1,1,0],[0,1,1]]
sr = 0
sc = 1
print(count_loops(grid,sr,sc))

