class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def find_child(self, value):
        for child in self.children:
            if child.value == value:
                return child
        return None

    def print_tree(self, level=0):
        if level == 0:
            print(self.value)
            print("here")
        else:
            print("  " * (level - 1) + "|__" + str(self.value))

        for child in self.children:
            child.print_tree(level + 1)

    def is_leaf(self):
        return len(self.children) == 0


