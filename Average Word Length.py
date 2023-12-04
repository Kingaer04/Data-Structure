def Average_Word_Length(words):
    number_of_word = 0
    count = 0
    for i in words:
        if i == " ":
            number_of_word = number_of_word
        else:
            number_of_word += 1
    for word in words.split(" "):
        count += 1
    print(number_of_word / count)


word = input()
Average_Word_Length(word)
