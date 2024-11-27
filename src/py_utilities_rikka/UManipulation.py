import string

def case_flip(string):
    try:
        return str.swapcase(string)
    except TypeError as err:
        print("Error: "+err)

def string_flip(string):
    try:
        finished_string = ""
        fin_num = 0
        for v in string:
            fin_num += 1
        fin_num2 = fin_num
        if fin_num != 0:
            fin_num -= 1
        while fin_num2 != 0:
            finished_string = finished_string + string[fin_num]
            fin_num -= 1
            fin_num2 -= 1
        return finished_string
    except TypeError as err:
        print("Error: "+err)

def word_count(string):
    """Counts words using whitespace. (Counts up by spaces.)"""
    try:
        wc_num = 1
        for v in string:
            if v == " ":
                wc_num += 1
        return wc_num
    except TypeError as err:
        print("Error: "+err)

def shift_character(c, shift):
    alphabet = string.ascii_lowercase
    if (str.lower(c)) not in alphabet:
        return c
    original_pos = alphabet.index(str.lower(c))
    new_pos = (original_pos + shift) % 26
    if str.isupper(c):
        return alphabet[new_pos].upper()
    else:
        return alphabet[new_pos]

def encode(string=" ",flip=True):
    """Returns an encoded version of the string. (Custom encoder!)"""
    result = []
    shifts = [-4,2]
    shift_index = 0
    for i,char in enumerate(string):
        shift = shifts[shift_index % 2]
        result.append(shift_character(char,shift))
        shift_index += 1
    result1 = "".join(result)
    if flip == False:
        return result1
    else:
        count = 0
        for v in result1:
            count += 1
        count2 = int(("-"+str(count)))
        count3 = 0
        result2 = ""
        while count3 != count2:
            count3 -= 1
            result2 = result2+(result1[count3])
        return result2

def decode(string,flip=True):
    """Returns an decoded version of the string. (Custom encoder!)"""
    result = []
    shifts = [4,-2]
    shift_index = 0
    for i,char in enumerate(string):
        shift = shifts[shift_index % 2]
        result.append(shift_character(char,shift))
        shift_index += 1
    result1 = "".join(result)
    if flip == False:
        return result1
    else:
        count = 0
        for v in result1:
            count += 1
        count2 = int(("-"+str(count)))
        count3 = 0
        result2 = ""
        while count3 != count2:
            count3 -= 1
            result2 = result2+(result1[count3])
        return result2