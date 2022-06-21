from collections import deque

class Solution:
    def numIslands(self, grid):
        rows = len(grid)
        columns = len(grid[0])
        islandcnt = 0
        
        coordinates = [(x,y) for x in range(rows) for y in range(columns)]
        visited = set()
        
        def bfs(x,y):
          positions = [(-1,0), (0,-1),(1,0),(0,1)]
          visited.add((x,y))
          deq = deque([(x,y)])
          
          while deq:
            x,y = deq.popleft()
            for (dr,dc) in positions:
              if (x+dr) in range(rows) and (y+dc) in range(columns) and grid[x+dr][y+dc] == '1' and (x+dr, y+dc) not in visited:
                visited.add((x+dr,y+dc))
                deq.append((x+dr, y+dc))
        
        # starting coordinate
        for (x,y) in coordinates:
          if(grid[x][y] == '1' and (x,y) not in visited):
            bfs(x,y)
            islandcnt += 1

        return islandcnt



grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

s = Solution()
print(s.numIslands(grid))