def sms_encoding(data):
    # start writing your code here
    encoded_word = ''
    vowels = 'aeiouAEIOU'
    vowels_tuple = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')

    words_in_sentence = data.split()
    for i in words_in_sentence:
        count = 0
        word_length = len(i)
        for j in range(len(i)):
            if i[j] in vowels:
                count += 1
        if count == word_length:
            encoded_word += i
        else:
            for x in i:
                if x in vowels_tuple:
                    i = i.replace(x, "")
            encoded_word += i
        encoded_word += " "
    encoded_word.pop(len(encoded_word))
    return encoded_word


data = "I love Python"
print(sms_encoding(data))
