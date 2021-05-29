# Dynamic Programming

+ [House Robber II](#house-robber-ii)

[comment]: <> (Stop)

## House Robber II

https://leetcode.com/problems/house-robber-ii/

```python
def rob(self, nums):
    if len(nums) == 1:
        return nums[0]
    def line_rob(nums):
        a = 0
        b = 0
        for num in nums:
            tmp = b
            b = max(a+num, b)
            a = tmp
        return b
    return max(line_rob(nums[1:]), line_rob(nums[:-1]))
```