/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2){
    struct ListNode* t, *pl1, *pl2;
    int carry=0;
    t=l1;
    while(l1 && l2){
        if( carry ){
            l1->val = l1->val + l2->val +1;
            if (l1->val >=10 ){
                l1->val %= 10;
                carry=1;
            }else{
                carry=0;
            }
        }else{
            l1->val = l1->val + l2->val;
            if (l1->val >=10 ){
                l1->val %= 10;
                //printf("l1->val=%d\n", l1->val);
                carry=1;
            }else{
                carry=0;
            }
        }
        pl1=l1;
        pl2=l2;
        l1=l1->next;
        l2=l2->next;
    }//done while
    
    if(l1==NULL && l2 != NULL){//l1 finished, l2 remaining: make l1 point to remaining of l2
            l1=pl1;
            l1->next=l2;
            l1=l1->next;//now l1 points to remaining of l2
    }//process carry, if any
    if(l1 != NULL && l2 == NULL);//process if any carry
    if(l1==NULL && l2 == NULL);//process if any carry
    if(carry){
        while(l1){
            if(carry){
                l1->val = l1->val +1;
                if(l1->val >= 10){
                    l1->val %= 10;
                    carry=1;
                }else{
                    carry=0;        
                }
            }else{
                //No more carry, no more addition
                break;
            }
            pl1=l1;
            l1=l1->next;
        }
        //at this point all nodes are finished.
        if (carry){
            printf("here\n");
            l1=pl1;
            l1->next=malloc(sizeof(struct ListNode));
            l1->next->val=1;
            l1->next->next=NULL;
        }
    }
    
    return t;
}
