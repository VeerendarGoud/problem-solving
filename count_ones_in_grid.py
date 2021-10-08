def count_ones_in_grid(grid,sr,sc):
    count = 0
    #count_tag = 2
    R,C = len(grid),len(grid[0])
    #base case
    if grid[sr][sc] == 2:
        return 0

    # base case
    if grid[sr][sc] == 1:
        grid[sr][sc] = 2
        #print(sr,sc)
        count += 1
        # recursive case
        if sr+1 < R: 
            count += count_ones_in_grid(grid,sr+1,sc)
        if sr-1 >= 0:
            count += count_ones_in_grid(grid,sr-1,sc)
        if sc+1 < C:
            count += count_ones_in_grid(grid, sr,sc+1)
        if sc-1 >= 0:
            count += count_ones_in_grid(grid,sr,sc-1)
    return count

def max_area_of_island(grid):

    max_count = 0
    R,C = len(grid),len(grid[0])

    for r in range(R):
        for c in range(C):
            if grid[r][c] == 1:
                count = count_ones_in_grid(grid,r,c)
                if count > max_count:
                    max_count = count

    return max_count



def island_perimeter(grid):
    R,C = len(grid),len(grid[0])

    for r in range(R):
        for c in range(C):
            if grid[r][c] == 1:
                return count_edges(grid,r,c)
                

def count_edges(grid,sr,sc):
    count = 0
    #count_tag = 2
    R,C = len(grid),len(grid[0])
    #base case
    if grid[sr][sc] == 2:
        return 0

    # base case
    if grid[sr][sc] == 1:
        grid[sr][sc] = 2
        #count += 1
        # recursive case
        if sr+1 < R: 
            count += count_edges(grid,sr+1,sc)
        else:
            count +=1
        if sr-1 >= 0:
            count += count_edges(grid,sr-1,sc)
        else:
            count +=1
        if sc+1 < C:
            count += count_edges(grid, sr,sc+1)
        else:
            count +=1
        if sc-1 >= 0:
            count += count_edges(grid,sr,sc-1)
        else:
            count +=1
    elif grid[sr][sc] == 0:
        count += 1
        
    return count








# grid = [[1,1,1],[1,1,0],[1,0,1]]
# sr = 1
# sc = 1
# print(count_ones_in_grid(grid,sr,sc))

# grid = [[0,0,0,0],[0,1,1,0],[0,1,1,0],[0,0,0,0]]
# sr = 1
# sc = 1
# print(count_ones_in_grid(grid,sr,sc))

# grid = [[1,0],[1,0],[1,0]]
# sr = 0
# sc = 0
# print(count_ones_in_grid(grid,sr,sc))

# grid = [[1]]
# sr = 0
# sc = 0
# print(count_ones_in_grid(grid,sr,sc))

# grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# print(max_area_of_island(grid))

# grid = [[0,0,0,0,0,0,0,0]]
# print(max_area_of_island(grid))

grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
sr = 0
sc = 1
#print(count_edges(grid,sr,sc))

print(island_perimeter(grid))