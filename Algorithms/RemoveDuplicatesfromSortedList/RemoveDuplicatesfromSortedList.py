class Solution:
    def deleteDuplicates(self, head):
        res = head
        while res:
            tmp = res.next
            while tmp and res.val == tmp.val:
                tmp = tmp.next
            res.next = tmp
            res = tmp
        return head