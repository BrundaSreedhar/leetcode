# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    #Brute force, slow, time = O(n), space = O(n)
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        #in inorder traversal, successor is the right cchild usually or a number greater than the right node

        min_abs = float("inf")

        inorder = []
        def _inorder(node):
            if not node:
                return
            _inorder(node.left)
            inorder.append(node)
            _inorder(node.right)
        

        _inorder(root)
        for i, node in enumerate(inorder):
            if p.val == node.val and i + 1 < len(inorder):
                return inorder[i+1]
        return None
            
    #Optimal
    """
    If p.val < root.val:
	•	Root is a potential successor
	•	But maybe there’s a smaller valid one in left subtree

    If p.val >= root.val:
	•	Successor must be in right subtree
    """
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        #in inorder traversal, successor is the right cchild usually or a number greater than the right node, either root or right
        successor = None
        while root:
            if p.val < root.val:
                successor=root
                root = root.left
            else:
                root = root.right
        return successor

