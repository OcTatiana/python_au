class Solution:
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
