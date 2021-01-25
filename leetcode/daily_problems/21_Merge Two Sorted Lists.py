# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # if either has no nodes
        if not l1:
            return l2
        if not l2:
            return l1
        
        # if both has nodes
        result = []
        a = l1
        b = l2
        
        while a and b:
            if a.val < b.val:
                result.append(a)
                a = a.next
            else:
                result.append(b)
                b = b.next
        while a:
            result.append(a)
            a = a.next
        while b:
            result.append(b)
            b = b.next

        # 여기 이렇게 두개나 먼저 빼는거 보다 좋은 방법 있을거 같은데 잘 모르겠다..
        start = result[0]
        curr = result[1]
        start.next = curr
        for node in result[2:]:
            curr.next = node
            curr = node
        return start
            
        
        
        