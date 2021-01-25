# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def solve(self, currNode, target):
        if currNode.val == target.val:
            return True
        else:
            # go deeper
            if currNode.left and self.solve(currNode.left, target):
                self.results.append('left')
                return True
            if currNode.right and self.solve(currNode.right, target):
                self.results.append('right')
                return True
            # if last node -> pass
            
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        self.results = []
        self.solve(original, target)
        print(self.results)
        ans = cloned
        for result in self.results[::-1]:
            if result == 'right':
                ans = ans.right
            elif result == 'left':
                ans = ans.left
        return ans
            
        
                