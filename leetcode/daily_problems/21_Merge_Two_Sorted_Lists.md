# 21. Merge Two Sorted Lists

<details open>
<summary>문제</summary>
<p>
Merge two sorted linked lists and return it as a **sorted** list. The list should be made by splicing together the nodes of the first two lists.

**Example 1:**

```
Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]
```

**Example 2:**

```
Input: l1 = [], l2 = []
Output: []
```

**Example 3:**

```
Input: l1 = [], l2 = [0]
Output: [0]
```

**Constraints:**
- The number of nodes in both lists is in the range `[0, 50]`.
- `-100 <= Node.val <= 100`
- Both `l1` and `l2` are sorted in **non-decreasing** order.
</p>
</details>



<details open>
<summary>1st solve: 새로운 리스트를 생성해서 거기에 적합한 원소들 집어넣기</summary>

- 새로 만드는거보다 .next를 활용해서 바로 원래 있던 애들을 연결해보기

```python
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
```
</details/>

<details open>
<summary>2nd solve: 더미 노드 생성해서 head 가리키게 하고 진행</summary>

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # dummy to point to head and tail to point to last node
        dummy = tail = ListNode()
        
        # continue until one is empty
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
            
        # if either ended or was empty from beginning 
        tail.next = l1 or l2
        return dummy.next  
```
</details/>
