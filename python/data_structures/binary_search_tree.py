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

        node = Node(value)

        if not self.root:
            self.root = node
            return


        climb(self.root, node)





