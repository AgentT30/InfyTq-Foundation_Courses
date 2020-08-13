def max_frequency_word_counter(data):
    word = ""
    frequency = 0
    count = {}
    # start writing your code here
    # Populate the variables: word and frequency
    word_list = data.lower().split(" ")

    for i in word_list:
        count.setdefault(i, 0)
        count[i] = count[i]+1

    word_count = []
    for i in count:
        # print(i, count.get(i))
        if count.get(i) > frequency:
            if frequency == count.get(i):
                if len(word) > len(i.rstrip()):
                    word = word
                else:
                    word = i.rstrip()
            else:
                frequency = count.get(i)
                word = i.rstrip()
    print(word, frequency)


# Provide different values for data and test your program.
# data = "Work like you do not need money, love like you have never been hurt, and dance like no one is watching"
data = 'Listen to the big clock Tick tock tick'
max_frequency_word_counter(data)
