class BSTnode:
    def __init__(self, data: int=None):
        self.data = data
        self.left = None
        self.Right = None
class BST:
    def __init__(self):
        self.root = None

    def insert(self , data :int):
       if not self.root:
            self.root = BSTnode(data)
       else:
            self.insertpulus(self.root, data)
    def insertpulus(self , node ,data):
        if data < node.data:
            if not node.left:
                node.left = BSTnode(data)
            else:
                self.insertpulus(node.left , data)
        else:
            if not node.Right:
                node.Right = BSTnode(data)
            else:
                self.insertpulus(node.Right , data)
    def is_empty(self):
        if not self.root:
            return True
    def traverse(self):
        if not self.root:
            print('This is an empty binary search tree.')
            return
        print("Preorder:" , end='')
        self.preorder(self.root)
        print()
        print("Inorder:" , end='')
        self.inorder(self.root)
        print()
        print("Postorder:" , end='')
        self.Postorder(self.root)
        print()
    def preorder(self , node):
        if node != None:
            print(' ->' , node.data , end='')
            self.preorder(node.left)
            self.preorder(node.Right)
    def inorder(self , node):
        if node != None:
            self.inorder(node.left)
            print(' ->' , node.data , end='')
            self.inorder(node.Right)
    def Postorder(self , node):
        if node != None:
            self.Postorder(node.left)
            self.Postorder(node.Right)
            print(' ->' , node.data , end='')
    def find_max(self):
        pos = self.root
        while pos.Right != None:
            pos = pos.Right
        return pos.data
    def find_min(self):
        pos = self.root
        while pos.left != None:
            pos = pos.left
        return pos.data
    def delete(self, data):
        def _find_max(node):
            current = node
            while current.right is not None:
                current = current.right
            return current.data
        def _delete_recursive(node, data):
            if node is None:
                return None, None

            if data < node.data:
                node.left, deleted = _delete_recursive(node.left, data)
            elif data > node.data:
                node.right, deleted = _delete_recursive(node.right, data)
            else:
                if node.left is None:
                    return node.right, node.data
                elif node.right is None:
                    return node.left, node.data

                max_val = _find_max(node.left)
                node.data = max_val
                node.left, _ = _delete_recursive(node.left, max_val)
                return node, data

            return node, deleted

        self.root, deleted = _delete_recursive(self.root, data)
        if deleted is None:
            print("Delete Error, " + str(data) + " is not found in Binary Search Tree.")
            return deleted
    
def main():
    my_bst = BST()
    while 1:
        text = input()
        if text == "Done":
            break
    condition, data = text.split(": ")
    if condition == "I":
      my_bst.insert(int(data))
    elif condition == "D":
      my_bst.delete(int(data))
    else:
      print("Invalid Condition")
  my_bst.traverse()

main()