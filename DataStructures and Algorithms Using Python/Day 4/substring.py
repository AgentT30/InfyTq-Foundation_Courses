def pattern_search(text, pattern):
    res = []
    for i in range(len(text)):
        if text.startswith(pattern, i):
            res.append(i)
    return len(res)


# Use different values for text and pattern and test your program
text = "MESMERIZING MESSAGE"
pattern = "MES"
result = pattern_search(text, pattern)
print("The given text:", text)
print("Pattern:", pattern)
print("No. of occurrences of the pattern :", result)
