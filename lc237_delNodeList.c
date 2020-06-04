/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
void deleteNode(struct ListNode* node) {
    struct ListNode *t;
    t=node;
        while(t){  //4,5,6 delete 5, t points index1
            t->val=t->next->val;   //4,6,6 t points index1
            
            if(t->next->next == NULL){//we moved all vals we are pointing to the last node, however we should terminate the list
                // that means, we need access of previous node
                free(t->next->next);
                t->next=NULL;
                break;
            }
            t=t->next;
        }
    return;
}
