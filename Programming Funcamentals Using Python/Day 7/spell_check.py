def find_correct(word_dict):
    # start writing your code here
    correct = 0
    almost_correct = 0
    wrong = 0
    for i in word_dict:
        if i == word_dict.get(i):
            correct += 1
        else:
            letters_correct = 0
            letters_wrong = 0
            for j in range(len(i)):
                if i[j] == word_dict.get(i)[j]:
                    letters_correct += 1
                else:
                    letters_wrong += 1
            if letters_wrong > 2:
                wrong += 1
            else:
                almost_correct += 1

    return [correct, almost_correct, wrong]


word_dict = {"THEIR": "THEIR", "BUSINESS": "BISINESS",
             "WINDOWS": "WINDMILL", "WERE": "WEAR", "SAMPLE": "SAMPLE"}
print(find_correct(word_dict))
