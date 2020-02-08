class Solution:
    def mergeTwoLists(self, l1, l2):
        if not l1 or not l2:
            return l2 or l1

        dummy = cur = ListNode(None)  # [1]
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next  # [2]
            else:
                cur = l2
                l2.next = l2.next  # [2]
            cur = cur.next  # [3]
        cur.next = l1 or l2  # [4]
        return dummy.next  # [5]