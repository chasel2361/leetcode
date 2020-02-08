from ListNode import ListNode

class Solution:
    def sortList(self, head):
        if not head or not head.next: return head        
        def getSize(head):
            count = 0
            while head:
                count += 1
                head = head.next
            return count
        
        def split(head, count):
            i = 1
            while i < count and head:
                head = head.next
                i += 1
            if not head: return None
            temp = head.next
            head.next = None
            return temp
        
        def merge(l, r, head):
            cur = head
            while (l and r):
                if l.val < r.val:
                    cur.next = l
                    l = l.next
                else:
                    cur.next = r
                    r = r.next
                cur = cur.next                
            cur.next = l or r
            while cur.next:
                cur = cur.next
            return cur
        
        size = getSize(head)
        bs = 1
        dummy = ListNode(0)
        dummy.next = head
        l, r, tail = None, None, None
        
        while bs < size:
            cur = dummy.next
            tail = dummy  #[1]
            while cur:
                l = cur
                r = split(l, bs)
                cur = split(r, bs)
                tail = merge(l, r, tail)
            bs <<= 1  #[2]
        return dummy.next