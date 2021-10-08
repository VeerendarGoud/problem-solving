

def floodFill(image, sr: int, sc: int, newColor: int):
    
    R, C = len(image), len(image[0])
    color = image[sr][sc]
    if color == newColor: return image
    def dfs(r, c):
        if image[r][c] == color:
            image[r][c] = newColor
            if r >= 1: dfs(r-1, c)
            if r+1 < R: dfs(r+1, c)
            if c >= 1: dfs(r, c-1)
            if c+1 < C: dfs(r, c+1)

    dfs(sr, sc)
    return image

    
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 0
sc = 0
new_color = 2

print(flood_fill(image,sr,sc,new_color,i=None,j=None))

