def sort_by(dict):
    return dict["num"]


def get_book(path):
    with open(path) as f:
        content = f.read()
        return content

def count_words(content):
    words = content.split()
    return len(words)

def count_letters(content):
    dict = {}
    for char in content:
        char = char.lower()
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    return dict

def list_dicts(dict):
    l = []
    for key in dict:
        if key.isalpha():
            l.append({"letter": key, "num": dict[key]})
    
    l.sort(reverse=True, key=sort_by)
    return l


def main(path):
    book = get_book(path)
    word_count = count_words(book)
    letter_count = count_letters(book)

    list = list_dicts(letter_count)

    for dict in list:
        print(f"The letter {dict['letter']} was found {dict['num']} times")


main("books/frankenstein.txt")

# with open("books/frankenstein.txt") as f:
#     content = f.read()
#     words = content.split()

#     all_chars = {}

#     for word in words:
#         for char in word:
#             char = char.lower()
#             if char in all_chars:
#                 all_chars[char]+=1
#             else:
#                 all_chars[char] = 1
    
#     list_of_dicts = []

#     for char in all_chars:
#         # print(f"{char} appears {all_chars[char]} times")
#         if char.isalpha():
#             dict = {"letter": char, "num": all_chars[char]}
#             list_of_dicts.append(dict)

#     list_of_dicts.sort(reverse=True, key=sort_by)

#     for dict in list_of_dicts:
#         print(f"The letter {dict['letter']} was found {dict['num']} times")

