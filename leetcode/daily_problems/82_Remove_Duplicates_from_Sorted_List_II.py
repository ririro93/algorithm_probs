# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # 애초에 없을 때
        if not head:
            return head
        
        # init
        dummy = tail = ListNode()
        prev = ListNode(101)
        curr = head.next
        
        # prev-head-curr 순으로 생각해서 head 가 prev랑도 다르고 curr랑도 다르면 추가
        while curr:
            if prev.val != head.val and head.val != curr.val:
                tail.next = head
                tail = head
            prev = head
            head = curr
            curr = head.next
        # 마지막에 두개 남았을 때 or 애초에 1개 밖에 없을 때
        if prev.val != head.val:
            tail.next = head
            tail = head
        tail.next = None # 이걸 해줘야지 뒤에 붙어있던 애들 자를수있다
        return dummy.next