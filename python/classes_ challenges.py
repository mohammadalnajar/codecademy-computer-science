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
