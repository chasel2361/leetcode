class Solution:
    def postorderTraversal(self, root):
        traversal = []
        stack = [(root, False)]  #[1]
        
        while stack:
            node, visited = stack.pop()
            if node:  #[2]
                if visited: 
                    traversal.append(node.val)  #[3]
                else:
                    stack.extend([(node, True), 
                                  (node.right, False), 
                                  (node.left, False)])  #[4]
        return traversal