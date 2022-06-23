class Tree:
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None

root = Tree()
root.data = 1
root.left = Tree()
root.left.data = 2
root.right = Tree()
root.right.data = 2

class Solution:
    def isSymmetric(self, root) -> bool:
        l,r = root.left, root.right
        print(root)
        deq = deque([l,r])
        
        while deque:
            res = deq.popleft()
            if(res.left.val != res.right.val):
                return False
            
            deq.append([res.left, res.right])
        
        return True
        