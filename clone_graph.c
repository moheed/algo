/**
 * Definition for a Node.
 * struct Node {
 *     int val;
 *     int numNeighbors;
 *     struct Node** neighbors;
 * };
 */


struct HashTable{
    struct Node* orig;
    struct Node* newg;
};
struct HashTable HashTable[100];//hashtable[0] will have first-node of graph

//returns node of the newGraph corresponding to the oldGraph, if present. otherwise NULL
struct Node* table_lookup(struct Node* node){
    int i=0;
    for(i=0; i< 100; i++){
        if (HashTable[i].orig==node)
            return HashTable[i].newg;
    }
    return NULL;
}
void init_table(){
    int i=0;
    for(i=0; i< 100; i++){
        HashTable[i].orig=NULL;
        HashTable[i].newg=NULL;
    }
}
void add_to_table(struct Node* orig, struct Node* newg){
    int i=0;
    for(i=0; i< 100; i++){
        if (HashTable[i].orig==NULL){
            HashTable[i].orig=orig;
            HashTable[i].newg=newg;
        }
    }
}

struct Node* makeNode(struct Node **orig){
    if (*orig == NULL) return NULL;
    struct Node* n ;
    if ((n=table_lookup(*orig)) != NULL){
        return n;
    }else{
        n= malloc(sizeof(struct Node));
        n->val =(*orig)->val;
        n->numNeighbors =(*orig)->numNeighbors;
        *(n->neighbors)=makeNode((*orig)->neighbors);
        add_to_table(*orig, n);
    }
    return n;
}
struct Iter{
    struct Node* node;
    struct Iter* next;
    int cloned;
};
void traverse_list_init(struct Iter **tRef, struct Node* s){
    struct Iter* tmp=malloc(sizeof(struct Iter));
            tmp->next=NULL;
            tmp->node=s;
            tmp->cloned=0;
            *tRef=tmp;
}
struct Node* traverse_list_pop(struct Iter **tRef){
    //returns the first node which is not yet cloned.
    struct Iter* t=*tRef;
    while(t){ 
        if(t->cloned){
            t=t->next;
        }else{
            t->cloned=1;
            return t->node;
        }     
    }
    return NULL;//NULL
}
void traverse_list_update(struct Iter **tRef, struct Node ** neighbor_nodes){
    //updates the iterator with neighbor_nodes
    struct Node* n= *neighbor_nodes;
    struct Iter* t=*tRef;
    //checks for duplicates
    int duplicate=0;
    while(n){
        duplicate=0;
        while(t){
            if(n->val==t->node->val){
                duplicate=1;
                break;
            } 
            t=t->next;
        }        
        if(duplicate == 0){//add to the head
            struct Iter* tmp=malloc(sizeof(struct Iter));
            tmp->next=*tRef;
            tmp->node=n;
            tmp->cloned=0;
            *tRef=tmp;
        }
        n=*(n->neighbors);
    }
}
void traverse_list_free(struct Iter **tRef){
    return;
}
struct Node *cloneGraph(struct Node *s) {
    
    if (s == NULL) return s;//empty graph
    
    /*idea is to have  a hash_table to keep track of cloned nodes.
    and maintain a traverse_list which keeps track of nodes traveresed so far.
    */
    init_table();//initailize the hashtable
    struct Iter* traverse_list=NULL;//to store nodes that needs to be traversed
    traverse_list_init(&traverse_list, s);//initially to first input graph node.
    struct Node* currentNode=NULL, *newGnode;
    while((currentNode = traverse_list_pop(&traverse_list)) != NULL){
        //currentNode->cloned=1;
        if ((newGnode=table_lookup(currentNode))==NULL){
            //hashtable doesnt have this node. clone this node and its neighbors
            //
            newGnode=makeNode(&currentNode);
            //add_to_table(currentNode, newGNode);
            //update traverse_list, so that other nodes can be processed on next iteration
            traverse_list_update(&traverse_list, currentNode->neighbors);//update traverse_list with all neighbors that are not in hashtable
            
        }//else hashtable has-this node so its already cloned.
    }
    traverse_list_free(&traverse_list);
    return table_lookup(s);
}
