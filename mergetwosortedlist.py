# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ptr_l1, ptr_l2 = l1, l2
        ans_head = ListNode()
        ptr_ans = ans_head
        
        while ptr_l1 != None and ptr_l2 != None:
            # put smallest to your answer list
            if ptr_l1.val <= ptr_l2.val:
                ptr_ans.next = ListNode(ptr_l1.val)
                ptr_l1 = ptr_l1.next
            else:
                ptr_ans.next = ListNode(ptr_l2.val)
                ptr_l2 = ptr_l2.next
                
            ptr_ans = ptr_ans.next
            
        # put the remaining ptr to the answer list
        while ptr_l1 != None:
            ptr_ans.next = ListNode(ptr_l1.val)
            ptr_ans = ptr_ans.next
            ptr_l1 = ptr_l1.next
        
        while ptr_l2 != None:
            ptr_ans.next = ListNode(ptr_l2.val)
            ptr_ans = ptr_ans.next
            ptr_l2 = ptr_l2.next
            
        return ans_head.next
            
