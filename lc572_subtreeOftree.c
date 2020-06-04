/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

bool issame(struct TreeNode* s, struct TreeNode* t){
    if (s==NULL && t== NULL)return 1;
    if (s==NULL&&  t!= NULL)return 0;
    if (s!=NULL&&  t== NULL)return 0;
    if(s->val == t->val){
        return (issame(s->left, t->left) && issame(s->right, t->right));
    }else{
        return 0;
    }
}
bool isSubtree(struct TreeNode* s, struct TreeNode* t){
    
    if (issame(s, t)){
        return 1;
    }else{
        if(s!=NULL)
            return (isSubtree(s->left, t) || isSubtree(s->right, t));
        else
            return 0;
    }
}
