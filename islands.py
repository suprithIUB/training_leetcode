class Solution(object):
    def neighbors(self, i, j, grid):
	left = (i, j-1) if (j-1) >= 0 else None
	right = (i, j+1) if (j+1) < len(grid[i]) else None
	down = (i+1, j) if (i+1) < len(grid) else None
	up = (i-1, j) if (i-1) >= 0 else None

	directions = []
	if left and grid[left[0]][left[1]]:
	    directions.append(left)
        if right and grid[right[0]][right[1]]:
	    directions.append(right)
	if down and grid[down[0]][down[1]]:
	    directions.append(down)
	if up and grid[up[0]][up[1]]:
	    directions.append(up)
        print(directions, i, j)
        return directions

    def dfs_recur(self, grid, i,j, visited):
        visited.add((i, j))

        for step in self.neighbors(i,j, grid):
            if grid[step[0]][step[1]] and step not in visited:
                self.dfs(grid, step[0], step[1], visited)

    def dfs(self, grid, i,j, visited):
	visited.add((i, j))
	stack = []
	stack.append((i,j))
	while stack:
	    parent = stack.pop()
	    for node in self.neighbors(parent[0],parent[1], grid):
		if node not in visited:
	    	    visited.add((node[0], node[1]))
		    stack.append(node)	

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        if not grid:
            return 0
        
        visited = set()
        islands = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] and (i,j) not in visited:
                    print("calling dfs %s %s", i, j)
                    self.dfs(grid, i,j, visited)
                    islands += 1
        return islands

if __name__ =="__main__":
    sol = Solution()
    grid = [[1,1,1,1,0],
           [1,1,0,1,0],
           [1,1,0,0,0],
           [0,0,0,0,0]]

    #print(sol.numIslands(grid))
    grid = [[1,1,0,0,0],[1,1,0,0,0],
            [0,0,1,0,0],[0,0,0,1,1]]
    from pprint import pprint
    pprint(grid)
    print(sol.numIslands(grid))
