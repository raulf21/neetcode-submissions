class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        
        parent, cur = None, root

        while cur and cur.val != key:
            parent = cur
            if key > cur.val:
                cur = cur.right
            else:
                cur = cur.left
        
        if not cur:
            return root
        # One or no children
        if not cur.left or not cur.right:
            child = cur.left if cur.left else cur.right
            if not parent:
                return child
            if parent.left == cur:
                parent.left = child
            else:
                parent.right = child
            return root
        # Two children
        par = cur
        delNode = cur
        cur = cur.right
        while cur.left:
            par = cur
            cur = cur.left
        if par != delNode:
            par.left = cur.right
            cur.right = delNode.right
        cur.left = delNode.left

        if not parent:
            return cur
        else:
            if parent.left == delNode:
                parent.left = cur
            else:
                parent.right = cur
        return root