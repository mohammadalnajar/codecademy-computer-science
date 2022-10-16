# def pattern_search(text, pattern):
#     pass


# text = "HAYHAYNEEDLEHAYHAYHAYNEEDLEHAYHAYHAYHAYNEEDLE"
# pattern = "NEEDLE"


# print(pattern_search(text, pattern))


def pattern_search(text, pattern, replacement, case_sensitive=True):
    # indices = []
    # list_letters = list(text)

    fixed_text = ""
    num_skips = 0
    for index in range(len(text)):
        match_count = 0
        for char in range(len(pattern)):
            if case_sensitive and pattern[char] == text[index + char]:
                match_count += 1
            elif (
                not case_sensitive
                and pattern[char].lower() == text[index + char].lower()
            ):
                match_count += 1
            else:
                break

        if match_count == len(pattern):
            # indices.append(index)
            fixed_text += replacement
            num_skips = len(pattern) - 1
            print(pattern, "found at index", index)
        else:

            if num_skips > 0:
                num_skips -= 1
                continue
            else:
                fixed_text += text[index]

    # for i in indices:
    #     print(i, "i")
    #     print(len(pattern), "pattern")

    #     diff_num = 0
    #     if len(pattern) > len(replacement):
    #         diff_num += len(pattern) - len(replacement)

    #     print(diff_num, "diff")
    #     for x in range(len(replacement)):
    #         if x < len(pattern):
    #             list_letters[i + x] = replacement[x]
    #         else:
    #             list_letters.insert(i + x, "")
    #             list_letters[i + x] = replacement[x]

    # for y in range(diff_num):
    #     list_letters.pop(i + y - 1)

    # print(list_letters, "list_letters", i)

    # print(indices, "indices")
    # print("".join(list_letters), "list_letters")
    print("=============================")
    print(fixed_text, "fixed_text")
    return fixed_text


friends_intro = "Pylhon is a wonderful Language that zzz is beloved for its ease zzz of use and simple syntacs. While zzz at some times the performance can be less than iDil, by properly zzz utilizing built-in libraries and other languuUuage features, pylhon's performance zzz can approach that of C."
pattern_search(friends_intro, "Language", "language")
pattern_search(friends_intro, "pylhon", "Python", False)
pattern_search(friends_intro, "idil", "ideal", False)
pattern_search(friends_intro, "zzz ", "")
pattern_search(friends_intro, "syntacs", "syntax")
pattern_search(friends_intro, "languuUuage", "language")
