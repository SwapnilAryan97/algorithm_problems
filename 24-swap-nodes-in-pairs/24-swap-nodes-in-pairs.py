# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # to swap nodes
        def swap(node = head):
            if node is not None and node.next is not None :
                l,r = node, node.next
                l.next = swap(node.next.next)
                r.next = l
                return r
            else:
                return node
        return swap(head)