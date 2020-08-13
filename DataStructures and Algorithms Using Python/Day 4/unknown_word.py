def find_unknown_words(text, vocabulary):
    unknown_set = set()
    text_list = text.lower().split()
    for i in text_list:
        if i in vocabulary:
            continue
        else:
            unknown_set.add(i)
    count = 0
    for i in unknown_set:
        count += 1
    if count == 0:
        return -1
    return unknown_set


# Pass different values of text and vocabulary to the function and test your program
text = "The sun rises in the east"
vocabulary = ["sun", "in", "east", "doctor", "day"]
unknown_words = find_unknown_words(text, vocabulary)
print("The unknown words in the file are:", unknown_words)
