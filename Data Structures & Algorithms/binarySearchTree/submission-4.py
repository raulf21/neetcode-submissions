class TreeNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class TreeMap:
    
    def __init__(self):
        self.root = None


    def insert(self, key: int, val: int) -> None:
        node = TreeNode(key, val)
        if self.root == None:
            self.root = node
            return
        
        current = self.root
        while True:
            if key<current.key:
                if current.left == None:
                    current.left = node
                    return
                current = current.left
            elif key > current.key:
                if current.right == None:
                    current.right = node
                    return 
                current = current.right
            else:
                current.val = val
                return 


    def get(self, key: int) -> int:
        current = self.root
        while current != None:
            if key < current.key:
                current = current.left
            elif key > current.key:
                current = current.right
            else:
                return current.val
        return -1


    def getMin(self) -> int:
        current = self.findMin(self.root)
        return current.val if current else -1

    def findMin(self, node: TreeNode) -> TreeNode:
        while node and node.left:
            node = node.left
        return node

    def findMax(self, node: TreeNode)-> TreeNode:
        while node and node.right:
            node = node.right
        return node

    def getMax(self) -> int:
        current = self.findMax(self.root)
        return current.val if current else -1

    def remove(self, key: int) -> None:
        self.root = self.removeHelper(self.root, key)
    def removeHelper(self, cur: TreeNode, key: int) -> TreeNode:
        if not cur:
            return None
        
        if key > cur.key:
            cur.right = self.removeHelper(cur.right, key)
        elif key < cur.key:
            cur.left = self.removeHelper(cur.left, key)
        else:
            if not cur.left:
                return cur.right
            elif not cur.right:
                return cur.left
            else:
                minNode = self.findMin(cur.right)
                cur.key = minNode.key
                cur.value = minNode.val
                cur.right = self.removeHelper(self.root.right, minNode.key)
        return cur

    def getInorderKeys(self) -> List[int]:
        result = []
        self.inorderTraversal(self.root, result)
        return result

    def inorderTraversal(self, root: TreeNode, result: List[int]) -> None:
        if root != None:
            self.inorderTraversal(root.left, result)
            result.append(root.key)
            self.inorderTraversal(root.right, result)

