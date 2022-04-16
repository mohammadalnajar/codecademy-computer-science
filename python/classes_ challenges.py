# 1. Count Letters
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
