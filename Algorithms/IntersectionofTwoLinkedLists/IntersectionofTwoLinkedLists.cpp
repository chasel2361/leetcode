/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB){
        int len_A = size(headA);
        int len_B = size(headB);
        int diff = len_A - len_B;
        
        if(diff > 0){
            while(diff > 0){
                headA = headA->next;
                diff--;
            }
        }
        else{
            while (diff < 0){
                headB = headB->next;
                diff++;
            }
        }
        
        while(headA){
            if(headA == headB) return headA;
            headA = headA->next;
            headB = headB->next;
        }
        return NULL;
    }
    
    int size(ListNode* node){
        if(node == NULL) return 0;
        return size(node->next) + 1;
    }
};