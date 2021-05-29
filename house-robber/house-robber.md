# Dynamic Programming

+ [House Robber](#house-robber)

[comment]: <> (Stop)
## House Robber

https://leetcode.com/problems/house-robber/

```python
def rob(self, nums):
    a = 0
    b = 0
    for num in nums:
        tmp = b
        b = max(a+num, b)
        a = tmp
    return b
```