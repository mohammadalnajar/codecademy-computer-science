# 1. Count Letters
print("1. Count Letters =====================================================")
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# Write your unique_english_letters function here:
def unique_english_letters(word):
    unique_letters = []
    for letter in word:
        if letter in letters:
            if letter not in unique_letters:
                unique_letters.append(letter)

    return len(unique_letters)


# Uncomment these function calls to test your function:
print(unique_english_letters("mississippi"))
# should print 4
print(unique_english_letters("Apple"))
# should print 4

# #########################################
# 2. Count X
print("2. Count X =====================================================")
# Write your count_char_x function here:
def count_char_x(word, x):
    letters = {}

    for letter in word:
        if letter not in letters.keys():
            letters[letter] = 1
        else:
            letters[letter] += 1
    return letters[x]


# Uncomment these function calls to test your tip function:
print(count_char_x("mississippi", "s"))
# should print 4
print(count_char_x("mississippi", "m"))
# should print 1

# 3. Count Multi X
print("3. Count Multi X =====================================================")


# Write your count_multi_char_x function here:
def count_multi_char_x(word, sub_word):
    word = word.split(sub_word)
    return len(word) - 1


# Uncomment these function calls to test your function:
print(count_multi_char_x("mississippi", "iss"))
# should print 2
print(count_multi_char_x("apple", "pp"))
# should print 1

# 4. Substring Between
print("4. Substring Between =====================================================")
# Write your substring_between_letters function here:
def substring_between_letters(word, letter_1, letter_2):
    idx_1 = word.find(letter_1)
    idx_2 = word.find(letter_2)
    if not idx_1 == -1 and not idx_2 == -1:
        return word[idx_1:idx_2]
    elif idx_1 == -1 and not idx_2 == -1:
        return word[:idx_2]
    elif not idx_1 == -1 and idx_2 == -1:
        return word[idx_1:]
    else:
        return ""


# Uncomment these function calls to test your function:
print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "c", "c"))

# should print "apple"
