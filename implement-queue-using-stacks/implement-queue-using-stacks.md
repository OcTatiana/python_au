# Design

+ [Implement Queue using Stacks](#implement-queue-using-stacks)

[comment]: <> (Stop)

## Implement Queue using Stacks

https://leetcode.com/problems/implement-queue-using-stacks/

```python
def __init__(self):
    self.queue = []
def push(self, x: int) -> None:
    self.queue.append(x)
def pop(self) -> int:
    return self.queue.pop(0)
def peek(self) -> int:
    return self.queue[0]
def empty(self) -> bool:
    return self.queue == []
```