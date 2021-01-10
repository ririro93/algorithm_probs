# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        my_list = []
        val = head.val
        head = head.next
        my_list.append(val)
        if not head:
            return ListNode(val)
        while head:
            val = head.val
            head = head.next
            my_list.append(val)
        my_list[k-1], my_list[-k] = my_list[-k], my_list[k-1]

        for i, ele in enumerate(my_list[::-1]):
            if i == 0:
                next_node = ListNode(ele)
            else:
                curr_node = ListNode(ele, next_node)
                next_node = curr_node
        return curr_node
            