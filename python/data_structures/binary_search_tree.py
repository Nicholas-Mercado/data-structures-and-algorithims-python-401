from data_structures.binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):
    """
    Put docstring here
    """

    def add(self, value):

        def climb(root, new_node):

            if not root:
                return

            if new_node.value < root.value:
                if root.left:
                    climb(root.left, new_node)
                else:
                    root.left = new_node

            if new_node.value > root.value:
                if root.right:
                    climb(root.right, new_node)
                else:
                    root.right = new_node

        node = Node(value)

        if not self.root:
            self.root = node
            return

        climb(self.root, node)

    def contains(self, target_value):

        def climb(root, target_value):

            if self.root.value == None:
                return False

            if self.root.value == target_value:
                return True

            elif self.root.value < target_value :
                    climb(root.left, target_value)

            else:
                    climb(root.right, target_value)

        return climb(self.root, target_value)

