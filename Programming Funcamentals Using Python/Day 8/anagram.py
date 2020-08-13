
def check_anagram(data1, data2):
    if len(data1) == len(data2):
        data1_set = set(data1.upper())
        data2_set = set(data2.upper())
        if len(data1_set - data2_set) == 0:
            for i in range(len(data1)):
                if data1[i].upper() == data2[i].upper():
                    return False
                else:
                    continue
            return True
        else:
            return False
    else:
        return False


print(check_anagram("Reductions", "discounter"))
