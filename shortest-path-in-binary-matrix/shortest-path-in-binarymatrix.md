# Graph

+ [Shortest Path in Binary Matrix](#shortest-path-in-binary-matrix)

[comment]: <> (Stop)

## Shortest Path in Binary Matrix

https://leetcode.com/problems/shortest-path-in-binary-matrix/

```python
def shortestPathBinaryMatrix(self, grid):
    if grid[0][0] == 1 or grid[-1][-1] == 1:
        return -1
    queue = [(0, 0, 1)]  # x, y, distance
    l = len(grid)
    count = 0
    while queue:
        x, y, d = queue.pop(0)
        if x == l-1 and y == l-1:
            return d
        for i, j in ((x-1, y-1), (x-1, y), (x-1, y+1), (x, y-1), (x, y+1), (x+1, y-1), (x+1, y), (x+1, y+1)):
            if l > i >= 0 and l > j >= 0 and grid[i][j] == 0:
                grid[i][j] = 1
                queue.append((i, j, d+1))
    return -1
```
