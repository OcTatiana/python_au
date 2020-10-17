class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        arr = []
        l = 0
        while head is not None:
            arr.append(head)
            head = head.next
            l = l + 1
        return arr[l//2]
