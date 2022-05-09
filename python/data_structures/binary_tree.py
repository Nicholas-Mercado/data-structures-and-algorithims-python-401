class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    """
    Put docstring here
    """

    def __init__(self):
        self.root = None
        self.ordered_values = []
        self.max = 0

    def pre_order(self):

        def climb(root, values):

            if not root:
                return

            values.append(root.value)

            climb(root.left, values)

            climb(root.right, values)

        climb(self.root, self.ordered_values)

        return self.ordered_values


    def in_order(self):

        def climb(root, values):

            if not root:
                return

            climb(root.left, values)

            values.append(root.value)

            climb(root.right, values)

        climb(self.root, self.ordered_values)

        return self.ordered_values


    def post_order(self):

        def climb(root, values):

            if not root:
                return

            climb(root.left, values)

            climb(root.right, values)

            values.append(root.value)

        climb(self.root, self.ordered_values)

        return self.ordered_values


    def find_maximum_value(self):

        def climb(root, values):

            if not root:
                return

            if root.value > self.max:
                self.max = root.value

            climb(root.left, values)

            climb(root.right, values)

        climb(self.root, self.ordered_values)

        return self.max
