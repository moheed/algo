# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        val=node.val #val to delete.
        #approach: move all values before, free the last one.
        #atleast two element, we can move always. Tricky part is to terminate the modified list before
        #its pointer reaches to last node.
        t=node
        while t:
            t.val = t.next.val
            if t.next.next == None:
                t.next=None
                break
            t=t.next
        
        return
