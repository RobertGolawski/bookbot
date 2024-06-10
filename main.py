def sort_by(dict):
    return dict["num"]






with open("books/frankenstein.txt") as f:
    content = f.read()
    words = content.split()

    all_chars = {}

    for word in words:
        for char in word:
            char = char.lower()
            if char in all_chars:
                all_chars[char]+=1
            else:
                all_chars[char] = 1
    
    list_of_dicts = []

    for char in all_chars:
        # print(f"{char} appears {all_chars[char]} times")
        if char.isalpha():
            dict = {"letter": char, "num": all_chars[char]}
            list_of_dicts.append(dict)

    list_of_dicts.sort(reverse=True, key=sort_by)

    for dict in list_of_dicts:
        print(f"The letter {dict['letter']} was found {dict['num']} times")

