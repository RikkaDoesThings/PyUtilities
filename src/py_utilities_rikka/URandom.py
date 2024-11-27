import random

def letters(how_many, caps):
    """Creates random letters.\nhow_many is how many letters will be returned.\ncaps makes the letters capitalized, (1) lowercase, (2) and mixed. (3)"""
    letterset = "abcdefghijklmnopqrstuvwxyz"
    finished_product = ""
    if caps == 1:
        while True:
            if how_many == 0:
                return finished_product
            else:
                rannum = random.randint(0,25)
                how_many -= 1
                finished_product = finished_product+(letterset[rannum])
    else:
        if caps == 2:
            while True:
                if how_many == 0:
                    return finished_product
                else:
                    rannum = random.randint(0,25)
                    how_many -= 1
                    finished_product = finished_product+(str.upper(letterset[rannum]))
        else:
            if caps == 3:
                while True:
                    if how_many == 0:
                        return finished_product
                    else:
                        rannum = random.randint(0,25)
                        rannum2 = random.randint(1,2)
                        if rannum2 == 1:
                            finished_product = finished_product+(letterset[rannum])
                        else:
                            if rannum2 == 2:
                                finished_product = finished_product+(str.upper(letterset[rannum]))

def numbers(how_many):
    """Return random numbers.\nhow_many is how many numbers will be returned."""
    finished_product = ""
    while True:
        if how_many == 0:
            return finished_product
        else:
            rannum = random.randint(0,9)
            how_many -= 1
            finished_product = finished_product+(str(rannum))

def symbols(how_many):
    """Return random symbols.\nhow_many is how many symbols will be returned."""
    symbolset = "`~!@#$%^&*()-_=+[]}{|;:',.<>/?"
    symbolset = symbolset + '"'
    finished_product = ""
    while True:
        if how_many == 0:
            return finished_product
        else:
            rannum = random.randint(0,30)
            how_many -= 1
            finished_product = finished_product+(symbolset[rannum])

def password(how_many):
    """Creates a random string of characters that include (capitalized and lowercase) letters, numbers, and symbols."""
    finished_product = ""
    while True:
        if how_many == 0:
            return finished_product
        else:
            rannum = random.randint(1,3)
            how_many -= 1
            if rannum == 1:
                finished_product = finished_product+(letters(1,3))
            elif rannum == 2:
                finished_product = finished_product+(numbers(1))
            elif rannum == 3:
                finished_product = finished_product+(symbols(1))

def uuid_gen(how_long):
    """Returns a randomly generated unique identifier."""
    with open("UUID.txt","r+") as f:
        list_text = f.readlines()
        uuid = (str(numbers(how_long)))
        whileloop = True
        while whileloop == True:
            trigger = False
            for v in list_text:
                if uuid == v:
                    trigger = True
            if trigger == True:
                uuid = (str(numbers(how_long)))
            else:
                whileloop == True
                break
        uuid2 = uuid+"\n"
        f.writelines(uuid2)
        return uuid

def rgb():
    """Generates 3 rgb values in order like this: 163, 81, 255."""
    return (random.randint(0,255)),(random.randint(0,255)),(random.randint(0,255))