# def fact(n):
#     if n == 0:
#         return 1
#     elif n >= 1:
#         return n * fact(n - 1)


# print(fact(4))


# def sum_digits(n):
#     if type(n) is int:
#         list_numbers = [int(x) for x in str(n)]
#     else:
#         list_numbers = n
#     list_len = len(list_numbers)
#     if list_len == 1:
#         return list_numbers[0]
#     return list_numbers[-1] + sum_digits(list_numbers[:-1])


# test cases
# print(sum_digits(12) == 3)
# print(sum_digits(552) == 12)
# print(sum_digits(123456789) == 45)


# def find_min(n, min=None):
#     if len(n) == 0:
#         return min

#     if min is None or n[0] < min:
#         min = n[0]

#     return find_min(n[1:], min)


# print(find_min([42, 17, 2, -1, 67]) == -1)
# print(find_min([]) == None)
# print(find_min([13, 72, 19, 5, 86]) == 5)


# def is_palindrome(my_string):
#     while len(my_string) > 1:
#         if my_string[0] != my_string[-1]:
#             return False
#         my_string = my_string[1:-1]
#     return True


# def is_palindrome(string, match=True):
#     if len(string) < 2:
#         return match

#     if string[0] != string[-1]:
#         match = False
#     else:
#         match = True

#     return is_palindrome(string[1:-1], match)


# print(is_palindrome("abba") == True)
# print(is_palindrome("abcba") == True)
# print(is_palindrome("") == True)
# print(is_palindrome("abcd") == False)


#################################################################


# def multiplication(num_1, num_2):
#     result = 0
#     for count in range(0, num_2):
#         result += num_1
#     return result


# def multiplication(num_1, num_2):
#     if num_2 == 1:
#         return num_1
#     return num_1 + multiplication(num_1, num_2 - 1)


# print(multiplication(3, 7))
# print(multiplication(5, 5))
# print(multiplication(0, 4))
# print(multiplication(2, 9))
# print(multiplication(7, 8))

#################################################################
# def depth(tree):
#     result = 0
#     # our "queue" will store nodes at each level
#     queue = [tree]
#     # loop as long as there are nodes to explore
#     while queue:
#         # count the number of child nodes
#         level_count = len(queue)
#         for child_count in range(0, level_count):
#             # loop through each child
#             child = queue.pop(0)
#             # add its children if they exist
#             if child["left_child"]:
#                 queue.append(child["left_child"])
#             if child["right_child"]:
#                 queue.append(child["right_child"])
#         # count the level
#         result += 1
#     return result


# def depth(tree, depth_level=0):
#     depth_level += 1
#     if not tree["left_child"] or not tree["right_child"]:
#         return depth_level

#     if tree["left_child"]:
#         return depth(tree["left_child"], depth_level)


# # HELPER FUNCTION TO BUILD TREES
# def build_bst(my_list):
#     if len(my_list) == 0:
#         return None

#     mid_idx = len(my_list) // 2
#     mid_val = my_list[mid_idx]

#     tree_node = {"data": mid_val}
#     tree_node["left_child"] = build_bst(my_list[:mid_idx])
#     tree_node["right_child"] = build_bst(my_list[mid_idx + 1 :])

#     return tree_node


# # HELPER VARIABLES
# tree_level_1 = build_bst([1])
# tree_level_2 = build_bst([1, 2, 3])
# tree_level_4 = build_bst([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])

# # print(tree_level_1)
# # print("-------------")
# # print(tree_level_2)
# # print("-------------")
# # print(tree_level_4)
# # print("-------------")
# # test cases
# print(depth(tree_level_1) == 1)
# print(depth(tree_level_2) == 2)
# print(depth(tree_level_4) == 4)

#################################################################


# def move_to_end(my_list, str):

#     result = []

#     if len(my_list) == 0:
#         return []

#     if my_list[0] == str:
#         result += move_to_end(my_list[1:], str)
#         result.append(my_list[0])

#     else:
#         result.append(my_list[0])
#         result += move_to_end(my_list[1:], str)

#     return result


# print(move_to_end(["Amber", "Sapphire", "Amber", "Jade"], "Amber"))

#################################################################


# define wrap_string() here
def wrap_string(str, n, openSymbol="<", closeSymbol=">"):
    result = ""

    if n <= 0:
        return str

    result += openSymbol
    result += wrap_string(str, n - 1, openSymbol, closeSymbol)
    result += closeSymbol

    return result


# Test code - do not edit
wrapped = wrap_string("Mohammad", 5, "!", "!")
print(wrapped)
