class Node:
    def __init__(self, value, next_node=None, prev_node=None):
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node

    def set_next_node(self, next_node):
        self.next_node = next_node

    def get_next_node(self):
        return self.next_node

    def set_prev_node(self, prev_node):
        self.prev_node = prev_node

    def get_prev_node(self):
        return self.prev_node

    def get_value(self):
        return self.value

    # def stringify_list(self):
    #     string_list = ""
    #     current_node = self.get_head_node()
    #     while current_node:
    #         if current_node.get_value() != "None":
    #             string_list += str(current_node.get_value()) + "\n"
    #         current_node = current_node.get_next()
    #     return string_list


class DoublyLinkedList:
    def __init__(self):
        self.head_node = None
        self.tail_node = None
