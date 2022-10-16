def sort_list(my_list):
    for x in range(len(my_list)):
        for idx in range(len(my_list)):
            if idx < len(my_list) - 1:
                num = my_list[idx]
                next_num = my_list[idx + 1]
                bigger = num > next_num
                if bigger:
                    my_list[idx] = next_num
                    my_list[idx + 1] = num
    return my_list


print(sort_list([3, 2, 1, 0, -1, -2, -3]))
print(sort_list([19, 8, 4, 2, 6, 5, 1, 9]))
