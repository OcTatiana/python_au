# Linked List

+ [Merge Two Sorted Lists](#merge-two-sorted-lists)
+ [Linked List Cycle](#linked-list-cycle)
+ [Reverse Linked List](#reverse-linked-list)
+ [Palindrome Linked List](#palindrome-linked-list)
+ [Middle of the Linked List](#middle-of-the-linked-list)
[comment]: <> (Stop)

## Merge Two Sorted Lists

https://leetcode.com/problems/merge-two-sorted-lists/

```python
def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    l3 = head = ListNode()
    while l1 is not None and l2 is not None:
        if (l1.val <= l2.val):
            l3.next = ListNode(l1.val, None)
            l1 = l1.next
        else:
            l3.next = ListNode(l2.val, None)
            l2 = l2.next
        l3 = l3.next
    if l1 is None:
        while l2 is not None:
            l3.next = ListNode(l2.val, None)
            l3 = l3.next
            l2 = l2.next
    else:
        while l1 is not None:
            l3.next = ListNode(l1.val, None)
            l3 = l3.next
            l1 = l1.next
    return head.next
```
## Linked List Cycle

https://leetcode.com/problems/linked-list-cycle/

```python
def hasCycle(self, head: ListNode) -> bool:
    k = False
    first = second = head
    while (second is not None and second.next is not None):
        first = first.next
        second = second.next.next
        if (first == second):
            k = True
            break
    return k
```
## Reverse Linked List

https://leetcode.com/problems/reverse-linked-list/

```python
def reverseList(self, head: ListNode) -> ListNode:
    cur = None
    while head is not None:
        tmp = head.next
        head.next = cur
        cur = head
        head = tmp
    return cur
```
## Palindrome Linked List

https://leetcode.com/problems/palindrome-linked-list/

```python
def isPalindrome(self, head: ListNode) -> bool:
    arr = []
    k = True
    while head is not None:
        arr.append(head.val)
        head = head.next
    for i in range(0, len(arr)//2):
        if arr[i] != arr[-1-i]:
            k = False
            break
    return k
```
## Middle of the Linked List

https://leetcode.com/problems/middle-of-the-linked-list/

```python
def middleNode(self, head: ListNode) -> ListNode:
    arr = []
    l = 0
    while head is not None:
        arr.append(head)
        head = head.next
        l = l + 1
    return arr[l//2]
```
