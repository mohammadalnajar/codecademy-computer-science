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

# 5. X Length
print("5. X Length =====================================================")

# Write your x_length_words function here:
def x_length_words(sentence, num):
    words = sentence.split()
    print(words)
    bool = True
    for word in words:
        if len(word) < num:
            bool = False
    return bool


# Uncomment these function calls to test your tip function:
print(x_length_words("i like apples", 2))
# should print False
print(x_length_words("he likes apples", 2))
# should print True


print(
    "=====================================ADVANCED====================================="
)

# 1. Check Name
print("1. Check Name =====================================================")


def check_for_name(sentence, name):
    return name.lower() in sentence.lower()


# Uncomment these function calls to test your  function:
print(check_for_name("My name is Jamie", "Jamie"))
# should print True
print(check_for_name("My name is jamie", "Jamie"))
# should print True
print(check_for_name("My name is Samantha", "Jamie"))
# should print False

# 2. Every Other Letter
print("2. Every Other Letter =====================================================")


# Write your every_other_letter function here:
def every_other_letter(word):
    new_word = ""
    for idx in range(len(word)):
        if idx % 2 == 0:
            new_word += word[idx]
    return new_word


# Uncomment these function calls to test your function:
print(every_other_letter("Codecademy"))
# should print Cdcdm
print(every_other_letter("Hello world!"))
# should print Hlowrd
print(every_other_letter(""))
# should print


# 3. Reverse
print("3. Reverse =====================================================")

# Write your reverse_string function here:
def reverse_string(word):
    return word[::-1]


# Uncomment these function calls to test your  function:
print(reverse_string("Codecademy"))
# should print ymedacedoC
print(reverse_string("Hello world!"))
# should print !dlrow olleH
print(reverse_string(""))
# should print


# 4. Make Spoonerism
print("4. Make Spoonerism =====================================================")

# Write your make_spoonerism function here:
def make_spoonerism(word_1, word_2):
    return word_2[0] + word_1[1:] + " " + word_1[0] + word_2[1:]


# Uncomment these function calls to test your function:
print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
print(make_spoonerism("a", "b"))
# should print b a


# 5. Add Exclamation
print("5. Add Exclamation =====================================================")

# Write your add_exclamation function here:
def add_exclamation(sentence):
    if len(sentence) <= 20:
        rest = 20 - len(sentence)
        for idx in range(rest):
            sentence += " "
        sentence = sentence.replace(" ", "!")
        return sentence
    return sentence


# Uncomment these function calls to test your function:
print(add_exclamation("Codecademy"))
# print(add_exclamation("Co dec ademy"))
# should print Codecademy!!!!!!!!!!
print(add_exclamation("Codecademy is the best place to learn"))
# should print Codecademy is the best place to learn
