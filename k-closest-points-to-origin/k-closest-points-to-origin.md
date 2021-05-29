# Math

+ [K Closest Points to Origin](#k-closest-points-to-origin)

[comment]: <> (Stop)

## K Closest Points to Origin

https://leetcode.com/problems/k-closest-points-to-origin/

```python
def kClosest(self, points, k):
    distances = []
    for point in points:
        x = point[0]
        y = point[1]
        distance = (x**2 + y**2) ** 0.5
        distances.append([distance, point])
    result = []
    distances.sort()
    for i in range(k):
        result.append(distances[i][1])
    return result
```