class Solution:
    def hasCycle(self, head):
        if not head or not head.next: return False
        slow = head.next
        fast = slow.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False