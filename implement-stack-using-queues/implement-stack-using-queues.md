# Design

+ [Implement Stack using Queues](#implement-stack-using-queues)

[comment]: <> (Stop)

## Implement Stack using Queues

https://leetcode.com/problems/implement-stack-using-queues/

```python
def __init__(self):
    self.stack = []
def push(self, x: int) -> None:
    self.stack.insert(0, x)
def pop(self) -> int:
    return self.stack.pop(0)
def top(self) -> int:
    return self.stack[0]
def empty(self) -> bool:
    return self.stack == []
def getMin(self) -> int:
    return min(self.stack)
```