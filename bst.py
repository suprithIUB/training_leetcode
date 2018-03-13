class BST:
    def __init__(self):
        self.root = None

    def add(self, item):
        new_node = BSTNode(item)
        if not self.root:
            self.root = new_node
        else:
            current_node = self.root
            parent = current_node
            while current_node:
                parent = current_node
                if item < current_node.data:
                    current_node = current_node.left
                else:
                    current_node = current_node.right
            if item < parent.data:
                parent.left = new_node
            else:
                parent.right = new_node

    def find_min_right_subtree(self, node):
        if not node:
            return
        min_node = node
        while min_node.left:
            min_node = node.left
        return min_node

    def delete(self, item, root):
        if not root:
            return
        if item < root.data:
            print("going left")
            root.left = self.delete(item, root.left)
        elif item > root.data:
            print("going right")
            root.right = self.delete(item, root.right)
        else:
            # found the match
            if not root.left and not root.right:
                print("no children")
                root = None
            elif root.left and root.right:
                min_node = self.find_min_right_subtree(root.right)
                root.data = min_node.data
                root.right = self.delete(min_node.data, root.right)
            else:
                if root.left:
                    temp = root
                    root = root.left
                    temp = None
                elif root.right:
                    temp = root
                    root = root.right
                    temp = None
        return root
    
    def search(self, item):
        if not self.root:
            return None
        current_node = self.root
        while current_node:
            if current_node.data == item:
                break
            elif item < current_node.data:
                current_node = current_node.left
            else: 
                current_node = current_node.right
        return current_node


    def inorder_iterative(self):
        if not self.root:
            return
        node = self.root
        stack = []
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                print(stack[-1].data)
                node = stack[-1].right
                stack.pop()

class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


if __name__ == "__main__":
    bst = BST()
    bst.add(12)
    bst.add(5)
    bst.add(17)
    bst.add(3)
    bst.add(7)
    bst.add(1)
    bst.add(9)
    bst.add(8)
    bst.add(11)
    bst.add(13)
    bst.add(17)
    bst.add(14)
    bst.add(20)
    bst.add(18)
    bst.inorder_iterative()
    print("set up done")
    #print(bst.search(28).data)
    bst.delete(1, bst.root)
    print("deleted 1")
    bst.inorder_iterative()
    bst.delete(13, bst.root)
    print("deleted 13")
    bst.inorder_iterative()
    bst.delete(17, bst.root)
    bst.inorder_iterative()
    print("deleted 17")
