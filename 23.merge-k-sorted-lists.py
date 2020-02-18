# @lc app=leetcode id=23 lang=python3

class Solution:
    
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not len(lists):
            return None
        return self.Helper(lists, 0, len(lists)-1)
        
    def Helper(self, lists: List[ListNode], l:int, r: int):
        if r == l :
            return lists[l]
        if r > l:
            return self.mergeTwoLists(self.Helper(lists, l, (l+r) // 2),self.Helper(lists, (l+r) // 2  +1, r)) 

        else:
            return None

    def mergeTwoLists(self, l1:ListNode, l2:ListNode) -> ListNode:
        head = temp = ListNode(-1)
        while l1 and l2:
            if l1.val <= l2.val:
                temp.next = l1
                l1 = l1.next
                temp = temp.next
            else:
                temp.next = l2
                l2 = l2.next
                temp = temp.next
        while l1:
            temp.next = l1
            l1 = l1.next
            temp = temp.next
        while l2:
            temp.next = l2
            l2 = l2.next
            temp = temp.next
        return head.next

# @lc code=end

