class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur = None
        while head is not None:
            tmp = head.next
            head.next = cur
            cur = head
            head = tmp
        return cur
