# Karen Huang
# KARHUANG
# 111644515
# CSE 101
# Homework #4

# In this part of the file it is very important that you write code inside
# the functions only. If you write code in between the functions, then the
# grading system will not be able to read your code or grade your work!


def pretty_print(keys_per_line, object, return_type=None):
    string = ''

    assert keys_per_line > 0, 'Invalid keys_per_line. Please provide a value > 0.'

    if type(object) == dict:
        value = list(object.values())
        key = list(object.keys())
        for i in range(len(object)):
            if i < len(object) - 1:
                if (i % keys_per_line != 0) or i == 0:
                    string += str(key[i]) + ' -> ' + str(value[i]) + ' \t'
                else:
                    string += '\n' + str(key[i]) + ' -> ' + str(value[i]) + ' \t'
            else:
                if i % keys_per_line != 0:
                    string += str(key[i]) + ' -> ' + str(value[i]) + '\n'
                else:
                    string += '\n' + str(key[i]) + ' -> ' + str(value[i]) + '\n'
    if return_type is None:
        print(string)
    else:
        return string


# Part I
def updown_encrypt(plaintext, num_rows):
    if num_rows < 0:
        return plaintext
    if len(plaintext) == 0:
        return '%' * num_rows
    if len(plaintext) % num_rows == 0:
        num_col = len(plaintext) // num_rows
    else:
        num_col = (len(plaintext) // num_rows) + 1
    grid = [[] for i in range(num_rows)]
    for c in range(num_col):
        if c % 2 == 0:
            for n in range(num_rows):
                if len(plaintext) == 0:
                    grid[n].insert(c,'%')
                else:
                    grid[n].insert(c,plaintext[0])
                    plaintext = plaintext[1:]
        else:
            for n in range(num_rows):
                if len(plaintext) == 0:
                    grid[num_rows - 1 - n].insert(c,'%')
                else:
                    #rows = num_rows - n
                    grid[num_rows - 1 - n].insert(c,plaintext[0])
                    plaintext = plaintext[1:]
    retW = ''
    for i in range(num_rows):
        for j in range(num_col):
            retW += grid[i][j]
    return retW


# Part II
def updown_decrypt(encrypted, num_rows):
    if num_rows < 0:
        return encrypted
    if len(encrypted) == 0:
        return None
    num_col = len(encrypted) // num_rows
    grid = [[] for i in range(num_rows)]
    for r in range(num_rows):
        for c in range(num_col):
            grid[r].insert(c,encrypted[0])
            encrypted = encrypted[1:]
    retW = ''
    for c in range(num_col):
        for r in range(num_rows):
            if c % 2 == 0:
                if grid[r][c] != '%':
                    retW += grid[r][c]
            else:
                if grid[num_rows - 1 - r][c] != '%':
                    retW += grid[num_rows - 1 - r][c]
    return retW




# Part III
def map_char_to_coords(filename):
    dict = {}
    num_line = 1
    for line in open(filename):
        arr = line.split()
        for n in range(len(arr)):
            dict[arr[n]] = (num_line,n+1)
        num_line += 1
    return dict

# Part IV
def map_coords_to_char(filename):
    dict = {}
    refDict = map_char_to_coords(filename)
    for key in refDict:
        dict[refDict[key]] = key
    return dict


# Part V
def dc_encrypt(plaintext, filename):
    charToCoords = map_char_to_coords(filename)
    rowNums = []
    colNums = []
    for letter in plaintext:
        row, col = charToCoords[letter]
        rowNums.append(row)
        colNums.append(col)
    enList = rowNums + colNums
    coordsToChar = map_coords_to_char(filename)
    retStr =''
    while len(enList) != 0:
        retStr += coordsToChar[(enList[0],enList[1])]
        enList = enList[2:]
    return retStr


# Part VI
def dc_decrypt(encrypted, filename):
    charToCoords = map_char_to_coords(filename)
    enList = []
    for letter in encrypted:
        enList.append(charToCoords[letter][0])
        enList.append(charToCoords[letter][1])
    mid = len(enList) // 2
    rowNums = enList[:mid]
    colNums = enList[mid:]
    coordsToChar = map_coords_to_char(filename)
    retStr = ''
    for n in range(mid):
        retStr += coordsToChar[(rowNums[n],colNums[n])]
    return retStr


# Below you will see an if-statement and a few tests. It is REALLY important
# that you not delete this if-statement or the tests inside. You may, however,
# add more tests to the code below. You can format them however you like.
# Upload your homework3.py file to CodeLoad to see how it matches up against other
# test cases!
if __name__ == '__main__':
    # Testing Part I
    print("##### Part I ##### ")
    print("Testing snake_encrypt() with plaintext = 'AMERICA', num_cols = 7: "
          + str(updown_encrypt('AMERICA', 7)))
    print("Testing snake_encrypt() with plaintext = 'STONYBROOKUNIV', num_cols = 4: "
          + str(updown_encrypt('STONYBROOKUNIV', 4)))
    print("Testing snake_encrypt() with plaintext = 'CHICKENWINGS', num_cols = -2: "
          + str(updown_encrypt('CHICKENWINGS', -2)))
    print("Testing snake_encrypt() with plaintext = '', num_cols = 5: "
          + str(updown_encrypt('', 5)))
    print()

    # Testing Part II
    print("##### Part II ##### ")
    print("Testing snake_decrypt() with encrypted = 'AMERICA', num_cols = 7: "  # Simple case
          + str(updown_decrypt('AMERICA', 7)))
    print("Testing snake_decrypt() with encrypted = 'SOO%TRK%OBUVNYNI', num_cols = 4: "  # Multi Lines case
          + str(updown_decrypt('SOO%TRK%OBUVNYNI', 4)))
    print("Testing snake_decrypt() with encrypted = 'CHICKENWINGS', num_cols = -2: "  # Invalid step case
          + str(updown_decrypt('CHICKENWINGS', -2)))
    print()

    # Testing Part III
    print("##### Part III ##### ")
    print("Testing map_char_to_coords with filename = 'key1.txt': ")
    pretty_print(4, map_char_to_coords('key1.txt'), None)
    print("Testing map_char_to_coords with filename = 'key2.txt': ")
    pretty_print(4, map_char_to_coords('key2.txt'), None)
    print("Testing map_char_to_coords with filename = 'key3.txt': ")
    pretty_print(4, map_char_to_coords('key3.txt'), None)

    # Testing Part IV
    print("##### Part IV ##### ")
    print("Testing map_coords_to_char with filename = 'key1.txt': ")
    pretty_print(4, map_coords_to_char('key1.txt'), None)
    print("Testing map_coords_to_char with filename = 'key2.txt': ")
    pretty_print(4, map_coords_to_char('key2.txt'), None)
    print("Testing map_coords_to_char with filename = 'key3.txt': ")
    pretty_print(4, map_coords_to_char('key3.txt'), None)

    # Testing Part V
    print("##### Part V ##### ")
    print("Testing dc_encrypt with plaintext = 'STONYBROOK', filename = 'key1.txt': "
          + str(dc_encrypt('STONYBROOK', 'key1.txt')))
    print("Testing dc_encrypt with plaintext = 'SUFFOLKCOUNTY', filename = 'key1.txt': "
          + str(dc_encrypt('SUFFOLKCOUNTY', 'key1.txt')))
    print("Testing dc_encrypt with plaintext = 'CSE101ISEASY', filename = 'key2.txt': "
          + str(dc_encrypt('CSE101ISEASY', 'key2.txt')))
    print("Testing dc_encrypt with plaintext = 'PASSWORD89ASHD891NE21D', filename = 'key3.txt': "
          + str(dc_encrypt('PASSWORD89ASHD891NE21D', 'key3.txt')))

    # Testing Part VI
    print("\n##### Part VI #####")
    print("Testing dc_decrypt with encrypted = 'J418FR9939', filename = 'key1.txt': "
          + str(dc_decrypt('J418FR9939', 'key1.txt')))
    print("Testing dc_decrypt with encrypted = 'GFOOKXEFOBTK3', filename = 'key1.txt': "
          + str(dc_decrypt('GFOOKXEFOBTK3', 'key1.txt')))
    print("Testing dc_decrypt with encrypted = 'J6GI6SJR0SEY', filename = 'key2.txt': "
          + str(dc_decrypt('J6GI6SJR0SEY', 'key2.txt')))
    print("Testing dc_decrypt with encrypted = 'PBW98AY8E77AROT9SN93J3', filename = 'key3.txt': "
          + str(dc_decrypt('PBW98AY8E77AROT9SN93J3', 'key3.txt')))
