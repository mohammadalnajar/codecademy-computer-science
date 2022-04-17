# 1. Sum Values
print("1. Sum Values =====================================================")


def sum_values(my_dict):
    result = 0
    for x in my_dict:
        if type(my_dict[x]) == int:
            result += my_dict[x]
    return result


# Uncomment these function calls to test your sum_values function:
print(sum_values({"milk": 5, "eggs": 2, "flour": 3}))
# should print 10
print(sum_values({10: 1, 100: 2, 1000: 3}))
# should print 6

# 2. Even Keys
print("2. Even Keys =====================================================")

# Write your sum_even_keys function here:
def sum_even_keys(dict):
    sum = 0  # Initialize sum
    for x in dict.keys():
        if x % 2 == 0:
            sum += dict[x]
    return sum


# Uncomment these function calls to test your  function:
print(sum_even_keys({1: 5, 2: 2, 3: 3}))
# should print 2
print(sum_even_keys({10: 1, 100: 2, 1000: 3}))
# should print 6


# 3. Add Ten
print("3. Add Ten =====================================================")

# Write your add_ten function here:
def add_ten(dict):
    for x in dict:
        dict[x] = dict[x] + 10
    return dict


# Uncomment these function calls to test your  function:
print(add_ten({1: 5, 2: 2, 3: 3}))
# should print {1:15, 2:12, 3:13}
print(add_ten({10: 1, 100: 2, 1000: 3}))
# should print {10:11, 100:12, 1000:13}

# 4. Values That Are Keys
print("4. Values That Are Keys =====================================================")

# Write your values_that_are_keys function here:
def values_that_are_keys(dict):
    keys = dict.keys()
    values = dict.values()
    result = []
    for key in keys:
        if key in values:
            result.append(key)

    return result


# Uncomment these function calls to test your  function:
print(values_that_are_keys({1: 100, 2: 1, 3: 4, 4: 10}))
# should print [1, 4]
print(values_that_are_keys({"a": "apple", "b": "a", "c": 100}))
# should print ["a"]

# 5. Largest Value
print("5. Largest Value =====================================================")

# Write your max_key function here:
def max_key(dict):
    max_val = max(dict.values())

    for key in dict:
        if dict[key] == max_val:
            return key


# Uncomment these function calls to test your  function:
print(max_key({1: 100, 2: 1, 3: 4, 4: 10}))
# should print 1
print(max_key({"a": 100, "b": 10, "c": 1000}))
# should print "c"
