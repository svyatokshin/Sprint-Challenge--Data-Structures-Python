class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        if node is None:        # if no node return None
            return None
        if node.next_node is not None:   # if there is a node after the node we are looking at
            new_node = node.next_node     # set new_node as the next_node after the node
            # set the prev node as the next_node (reversing)
            node.next_node = prev
            # recurrsion on this new_node, with the prev node being the one we just ran
            self.reverse_list(new_node, node)
        else:
            # else would mean we have we have no next_node for node we are looking at
            self.head = node
            node.next_node = prev
            # so make head the node as it was just tail, and prev node is now next_node


# For example,

# 1->2->3->None
# would become...

# 3->2->1->None
