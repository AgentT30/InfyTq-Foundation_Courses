def encode(message):
    final_ans = ""
    while len(message) > 0:
        letter_count = 0
        char = message[0]
        while len(message) > 0:
            if char == message[0]:
                letter_count += 1
                message = message[1:]
            else:
                break
        final_ans += str(letter_count) + char
    return final_ans


# Provide different values for message and test your program
encoded_message = encode("AABCCA")
print(encoded_message)
