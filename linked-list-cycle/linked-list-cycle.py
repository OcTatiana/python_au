class Solution:
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
