# favorite_fruit = "blueberry"

# print(favorite_fruit[1:3])

# first_name = "Rodrigo"

# last_name = "Villanueva"

# print(last_name[0:5])


# def account_generator(f_name, l_name):
#     return f_name[0:3] + l_name[0:3]


# print(account_generator(first_name, last_name))


# def password_generator(f_name, l_name):
#     return f_name[len(f_name) - 3 :] + l_name[len(l_name) - 3 :]


# print("=========")
# print(password_generator(first_name, last_name))


# company_motto = "Copeland's Corporate Company helps you capably cope with the constant cacophony of daily life"

# print(company_motto[-len(company_motto) + 1 :])


# def letter_check(word, letter):
#     if letter in word:
#         return True
#     return False


# print(letter_check("letter", "l"))


def username_generator(first_name, last_name):
    first_name = first_name.replace(" ", "")
    last_name = last_name.replace(" ", "")
    username = first_name[:3] + last_name[:4]
    return username


print(username_generator("Mohammad", "Al najar"))


def password_generator(username):
    last_letter = username[-1]
    password = last_letter
    password = last_letter + username[:-1]

    for letter in username:
        password = password + letter

    return password


print(password_generator(username_generator("Mohammad", "Al najar")))
