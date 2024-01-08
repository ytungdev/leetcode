# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        L = list1
        R = list2
        res_head = None
        
        if L == None and R == None:
            return None
        if L != None and R == None:
            return L
        if L == None and R != None:
            return R
        if L.val <= R.val:
            res_head = L
            L = L.next
        else:
            res_head = R
            R = R.next

        res_curr = res_head

        while L != None or R != None:
            # L empty, R not
            if L == None:
                res_curr.next = R
                return res_head
            # R empty, L not
            elif R == None:
                res_curr.next = L
                return res_head
            # L and R both not empty
            else:
                if L.val <= R.val:
                    res_curr.next = L
                    L = L.next
                    res_curr = res_curr.next
                else:
                    res_curr.next = R
                    R = R.next
                    res_curr = res_curr.next
        return res_head