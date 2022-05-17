class Node:
    index = 0

    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node
        self.index = Node.index
        Node.index += 1

    def get_value(self):
        return str(self.value)

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

    def get_index(self):
        return self.index


class Linked_list:
    def __init__(self, value=None):
        self.head_node = Node(value)

    def get_head_node(self):
        return self.head_node

    def insert_beginning(self, new_value):

        new_node = Node(new_value)
        # print(new_node.get_value(), "new_node")
        new_node.set_next(self.head_node)
        self.head_node = new_node

    def stringify_list(self):
        string_list = ""
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_value() != "None":
                string_list += str(current_node.get_value()) + "\n"
            current_node = current_node.get_next()
        return string_list

    def reverse_list(self):

        current_node = self.get_head_node()
        previous_node = None

        while current_node is not None:
            if current_node.get_next() is None:
                self.head_node = current_node

            next_node = current_node.get_next()
            current_node.set_next(previous_node)
            previous_node = current_node
            current_node = next_node

    def get_list_length(self):
        current_node = self.get_head_node()
        length = 1
        while current_node.get_next() is not None:
            current_node = current_node.get_next()
            length += 1

        return length

    def find_node(self, index):
        global found_node
        found_node = None

        current_node = self.get_head_node()

        while current_node is not None:
            if current_node.get_index() == index:
                found_node = current_node
                break

            current_node = current_node.get_next()

        return found_node

    def generate_test_linked_list():
        linked_list = Linked_list()
        for i in range(1, 51):
            linked_list.insert_beginning(i)
        return linked_list


def nth_last_node(linked_list, n):
    return linked_list.find_node(linked_list.get_list_length() - n)


# list = Linked_list(1)

# list.insert_beginning(2)
# list.insert_beginning(3)
# list.insert_beginning(4)
# list.insert_beginning(5)

# print(list.stringify_list())
# list.reverse_list()
# print(list.stringify_list())

# print(list.get_list_length())

# print(list.find_node(list.get_list_length() - 2).get_value())


# Complete this function:


test_list = Linked_list.generate_test_linked_list()

print(test_list.stringify_list())


# test_list.reverse_list()
# print(test_list.stringify_list())

print("===========")

print(test_list.find_node(48).get_value())

print("==========")
print("==========")
print("==========")

print(test_list.get_list_length())
print("==========")
nth_last = nth_last_node(test_list, 2)
print(nth_last.value)
print("==========")
