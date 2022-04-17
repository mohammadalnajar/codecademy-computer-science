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

print("==============================ADVANCED==============================")

# 1. Word Length Dict
print("1. Word Length Dict =====================================================")

# Write your word_length_dictionary function here:
def word_length_dictionary(list_of_words):
    dict = {}
    for word in list_of_words:
        dict[word] = len(word)

    return dict


# Uncomment these function calls to test your  function:
print(word_length_dictionary(["apple", "dog", "cat"]))
# should print {"apple":5, "dog": 3, "cat":3}
print(word_length_dictionary(["a", ""]))
# should print {"a": 1, "": 0}

# 2. Frequency Count
print("2. Frequency Count =====================================================")

# Write your frequency_dictionary function here:
def frequency_dictionary(list_of_values):
    dict = {}
    for val in list_of_values:
        dict[val] = list_of_values.count(val)

    return dict


# Uncomment these function calls to test your  function:
print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}
print(frequency_dictionary([0, 0, 0, 0, 0]))
# should print {0:5}

# 3. Unique Values
print("3. Unique Values =====================================================")

# Write your unique_values function here:


def unique_values(dict):
    values = []
    for val in dict.values():
        values.append(val)
    print(values, "values")
    for val in dict.values():
        print(values.count(val), "val")
        if values.count(val) > 1:
            values.remove(val)

    # for key in dict:
    #     if

    print(values)


# Uncomment these function calls to test your  function:
print(unique_values({0: 3, 1: 1, 4: 1, 5: 3}))
# should print 2
print(unique_values({0: 3, 1: 3, 4: 3, 5: 3}))
# should print 1

# 4. Count First Letter
print("4. Count First Letter =====================================================")

# Write your count_first_letter function here:
def count_first_letter(dict):

    dict_to_return = {}
    for key in dict:
        if not key[0] in dict_to_return:
            dict_to_return[key[0]] = len(dict[key])
        else:
            dict_to_return[key[0]] += len(dict[key])
    return dict_to_return


# Uncomment these function calls to test your  function:
print(
    count_first_letter(
        {
            "Stark": ["Ned", "Robb", "Sansa"],
            "Snow": ["Jon"],
            "Lannister": ["Jaime", "Cersei", "Tywin"],
        }
    )
)
# should print {"S": 4, "L": 3}
print(
    count_first_letter(
        {
            "Stark": ["Ned", "Robb", "Sansa"],
            "Snow": ["Jon"],
            "Sannister": ["Jaime", "Cersei", "Tywin"],
        }
    )
)
# should print {"S": 7}
