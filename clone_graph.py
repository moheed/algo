"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    #return a list of current_node neighbors after cloning them, if they are not
    #cloned already, also updates the hash_table with these new clones. these neighbor_list
    #may/may_not have their neighbors set correctly
    def clone_neighbors(self, current_node, hash_table):
        n_list=[]
        for x in current_node.neighbors:
            if x not in hash_table:
                #clone
                n=Node(x.val, None)
                hash_table[x]=n
            #already cloned
            n_list+=[x]
        return n_list
                
        
    def cloneGraph(self, node: 'Node') -> 'Node':
        """
        A BFS solution: idea is to have a traverse_list, initially with the given node.
        Clone the node, update the traverse list with the neighbors of just cloned node.
        keep looping on traverse list, untill it becomes empty.
        while updating traverse_list ensure that duplicates dont go into it, hence a set is
        good idea.
        """
        
        if not node:
            #empty set
            return None
        elif not node.neighbors:
            return Node(node.val, None)
        
        hash_table=dict() #stores old and new graphs node mapping
        
        traverse_list=[(node, False)];
        current_node=traverse_list[0]
        while( True ):
            if current_node[0] in hash_table and not current_node[1]:
                #already cloned but not neighbored
                hash_table[current_node[0]].neighbors=self.clone_neighbors(current_node[0], hash_table)
                traverse_list.append((current_node, True))
            elif current_node[0] not in hash_table:#current_node not in hash_table
                t=self.clone_neighbors(current_node[0], hash_table)
                n=Node(current_node[0].val, t)
                hash_table[current_node[0]]= n
                traverse_list.append((current_node, True))
                for x in t:
                    traverse_list.append((t, False))
            else:
                #current node in hash_table and neighbored, check next
                try:
                    current_node=traverse_list.pop()
                except IndexError:
                    break
            
                
        return hash_table[node]
