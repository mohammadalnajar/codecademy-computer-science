print('Start ============================')

# def large_power(bass,exponent):
#     result = bass**exponent
    
#     if result > 5000:
#         return True
#     else:
#         return False
    
# Uncomment these function calls to test your large_power function:
# print(large_power(2, 13))
# print(2**13)
# should print True
# print(large_power(2, 12))
# print(2**12)
# should print False

# ==================================

# def over_budget(budget,food_bill,electricity_bill,internet_bill,rent):
#     if budget < food_bill+electricity_bill+internet_bill+rent:
#         return True
#     else:
#         return False
    
# # Uncomment these function calls to test your over_budget function:
# print(over_budget(100, 20, 30, 10, 40))
# # should print False
# print(over_budget(80, 20, 30, 10, 30))
# # should print True

# ===================

# def twice_as_large(num1,num2):
#     if num1 > num2*2:
#         return True
#     else: 
#         return False

        
        
# ==================



# def divisible_by_ten(num):
#     if num % 10 == 0:
#         return True
#     else:
#         return False


# ===========

# def in_range(num,ren1,ren2):
#     if num > ren1 and num <ren2:
#         return True
#     else:
#         return False
    
    
# def max_num(num1,num2,num3):
#     arr = [num1,num2,num3]
#     sorted_arr = sorted(arr)
#     if sorted_arr[-1] == sorted_arr[-2]:
#         return "It's a tie!"
#     else:
#         return sorted_arr[-1]


# ================
#Write your function here
# def append_sum(lst):
#   i = 0
#   for num in lst:
#     if i < 3:
#       lst.append(lst[-1] + lst[-2])
#       i=i+1
#     else:
#       break
#   return lst

# def append_sum(lst):    
#     # print(type(range(len(lst))))
#     for x in range(3):
#         if x < 3:
#             lst.append(lst[-1]+lst[-2])
#     return lst
# #Uncomment the line below when your function is done
# print(append_sum([1, 1, 2]))
# print(append_sum([3, 8]))
# # [1, 1, 2, 3, 5, 8]
# # [3, 8, 11, 19, 30]

# =======================

#Write your function here
# def more_than_n(lst,item,n):
#     repeated = 0
#     for x in range(len(lst)):
#         if lst[x] == item:
#             repeated +=1
    
#     if repeated > n:
#         return True
#     else:
#         return False

#Uncomment the line below when your function is done
# print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))


# # ===================

# def every_three_nums(start):
#     lst = []
#     if start > 100:
#         return lst
    
#     lst = range(start,101,3)
#     return list(lst)  

# print(every_three_nums(91))  
    
# # ===================

# def remove_middle(lst,start,end):
#     first_lst = lst[:start]
#     second_lst = lst[end+1:]
#     new_lst = first_lst+second_lst
  
            
#     return new_lst

# print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))


# =========

# def more_frequent_item(lst,item1,item2):
#     item1_freq = lst.count(item1)
#     item2_freq = lst.count(item2)
#     if item2_freq > item1_freq:
#         return item2
#     else:
#         return item1
# print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))

# =======

# def double_index(lst,idx):
#     if not idx > len(lst)-1:
#         lst.insert(idx,lst[idx]*2)
#         lst.pop(idx+1)
#         return lst
    
# print(double_index([3, 8, -10, 12], 2))

# =======

# def middle_element(lst):
#     if len(lst) % 2 == 0:
#         md_idx1 =(round(len(lst)/2))
#         md_idx2 =md_idx1 -1
#         return (lst[md_idx1]+lst[md_idx2])/2
#     else:
#         md_idx = (round(len(lst)/2))
#         return lst[md_idx]
# print(middle_element([5, 2, -10, -4, 4, 5]))

#  =================

# def divisible_by_ten(nums):
#     count = 0
#     divisible_nums= []
#     for num in nums:
#         if num%10 == 0:
#             count+=1
#             divisible_nums.append(num)
    
#     print(divisible_nums)
#     return count
# print(divisible_by_ten([20, 25, 30, 35, 40]))


#  =================

# def add_greetings(names):
#     lst = []
#     for name in names:
#         lst.append('Hello, '+name)
    
#     return lst
# print(add_greetings(["Owen", "Max", "Sophie"]))


#  =================

# def delete_starting_evens(lst):
#     for idx in range(len(lst)):
#         if lst[idx] % 2 != 0:
#             return lst[idx:]

#     return []
            
    
    
# print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
# print(delete_starting_evens([4, 8, 10]))

# ================

# def odd_indices(lst):
#     new_lst= []
#     for idx in range(len(lst)):
#         if idx % 2 != 0:
#             new_lst.append(lst[idx])
#     return new_lst


# print(odd_indices([4, 3, 7, 10, 11, -2]))


# ================

# def exponents(lst1,lst2):
#     lst = []
#     for num1 in lst1:
#         for num2 in lst2:
#             lst.append(num1**num2)            
    
#     return lst
    
# print(exponents([2, 3, 4], [1, 2, 3]))

# ================

# def larger_sum(lst1,lst2):
#     sum1 = 0
#     sum2 = 0
    
#     for num1 in lst1:
#         sum1 +=num1
#     for num2 in lst2:
#         sum2 +=num2
       
#     if sum1 < sum2:
#         return lst2
#     else:
#         return lst1
# print(larger_sum([1, 9, 5], [2, 3, 7]))


# ================

# def over_nine_thousand(lst):
#     sum = 0 
#     idx = 0
#     while sum < 9000 and idx < len(lst):
#         sum += lst[idx]
#         idx += 1   
        
#     return sum      
    
# print(over_nine_thousand([8000, 900, 120, 5000]))

# ===================

# def max_num(nums):
#     max_num = 0 
#     prev_num = 0
#     for num in nums:
#         if num > prev_num:
#             max_num = num
        
#         prev_num = num
    
#     return max_num

# print(max_num([50, -10, 100, 75, 20]))


# =======

# def sum_list(nums):
#     sum = 0 
#     for num in nums: 
#         sum +=num
#     return sum
    
# print(sum_list([1,2,3,4]))


# ==============

# def same_values(lst1,lst2):
#     same_values_indices = []
    
#     for idx1 in range(len(lst1)):
#         for idx2 in range(len(lst2)):
#             if lst1[idx1] == lst2[idx2] and idx1 == idx2:
#                 same_values_indices.append(idx1)
#     return same_values_indices

# def same_values(lst1,lst2):
#     same_values_indices = []
    
#     for idx in range(len(lst1)):
#         if lst1[idx] == lst2[idx]:
#             same_values_indices.append(idx)
#     return same_values_indices

# print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))
# [0, 2, 3]

# ==============

# def reversed_list(lst1,lst2):
#     reversed = True
    
#     for idx1 in range(len(lst1)):
#         print(lst1[idx1],'lst1')
#         print(lst2[-idx1-1],'lst2')
#         if lst1[idx1] != lst2[-idx1-1]:
#             reversed = False
#     return reversed


# print(reversed_list([1, 2, 3], [3, 2, 1]))
# print(reversed_list([1, 5, 3], [3, 2, 1]))


# =================



# def tenth_power(num):
#     return num**10

# print(tenth_power(1))
# # 1 to the 10th power is 1
# print(tenth_power(0))
# # 0 to the 10th power is 0
# print(tenth_power(2))
# # 2 to the 10th power is 1024

# ==============

# def square_root(num):
#     return num**1/2

#====================

# def win_percentage(wins,loses):
#     total = wins + loses
#     return wins/total*100

# ==============

# def average(num1,num2):
#     return num1+num2/2

# ===========

# def first_three_multiples(num):
#     print(1*num)
#     print(2*num)
#     print(3*num)
#     return 3*num

# ============

# def tip(total,percentage):
#     return total*percentage/100

# def dog_years(name,age):
#     return name+', you are'+age*7+' years old in dog years'