class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        get_length = self.get_length
        move_eq = self.move_to_equal
        
        ptr_A, ptr_B = headA, headB
        len_A = get_length(headA)
        len_B = get_length(headB)
        
        if len_A > len_B:
            ptr_A = move_eq(ptr_A, len_A-len_B)
        else:
            ptr_B = move_eq(ptr_B, len_B-len_A)
        
        while ptr_A is not None:
            if ptr_A == ptr_B:
                return ptr_A
            ptr_A = ptr_A.next
            ptr_B = ptr_B.next
        return None
        
    def move_to_equal(self, head, steps):
        ptr = head
        for _ in range(steps):
            ptr = ptr.next
        return ptr
    
    def get_length(self, head):
        length = 0
        ptr = head
        while ptr is not None:
            length += 1
            ptr = ptr.next
        return length