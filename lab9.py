# your name
# your NetID
# your SBU ID number
# CSE 101
# Lab #9

# In this part of the file it is very important that you write code inside
# the functions only. If you write code in between the functions, then the
# grading system will not be able to read your code or grade your work!


# Part I
def arabic2wolfie(num):
    retStr = ''
    while num > 0:
        if num == 64:
            retStr += 'S'
            num -= 64
        elif num >= 56:
            retStr += 'ES'
            num -= 56
        elif num >= 32:
            retStr += 'T'
            num -= 32
        elif num >= 24:
            retStr += 'ET'
            num -= 24
        elif num >= 8:
            retStr += 'E'
            num -= 8
        elif num >= 7:
            retStr += 'IE'
            num -= 7
        elif num >= 4:
            retStr += 'F'
            num -= 4
        elif num >= 3:
            retStr += 'IF'
            num -= 3
        elif num >= 1:
            retStr += 'I'
            num -= 1
    return retStr

# Part II
def wolfie2arabic(numerals):
    nums = numerals + ' '
    i = 0
    retNum = 0
    while i < len(nums) - 1:
        if nums[i] == 'S':
            retNum += 64
            i += 1
        elif nums[i] == 'E':
            if nums[i+1] == 'S':
                retNum += 56
                i += 2
            elif nums[i+1] == 'T':
                retNum += 24
                i += 2
            else:
                retNum += 8
                i += 1
        elif nums[i] == 'T':
            retNum += 32
            i += 1
        elif nums[i] == 'I':
            if nums[i+1] == 'E':
                retNum += 7
                i += 2
            elif nums[i+1] == 'F':
                retNum += 3
                i += 2
            else:
                retNum += 1
                i += 1
        elif nums[i] == 'F':
            retNum += 4
            i += 1
    return retNum


# Below you will see an if-statement and a few tests. It is REALLY important
# that you not delete this if-statement or the tests inside. You may, however,
# add more tests to the code below. You can format them however you like.
# Upload your homework3.py file to CodeLoad to see how it matches up against other
# test cases!
if __name__ == '__main__':
    # Part I
    print("Testing Part I")
    print('Testing arabic2wolfie() with num = 10: ' + str(arabic2wolfie(10)))
    print('Testing arabic2wolfie() with num = 14: ' + str(arabic2wolfie(14)))
    print('Testing arabic2wolfie() with num = 22: ' + str(arabic2wolfie(22)))
    print('Testing arabic2wolfie() with num = 28: ' + str(arabic2wolfie(28)))
    print('Testing arabic2wolfie() with num = 30: ' + str(arabic2wolfie(30)))
    print('Testing arabic2wolfie() with num = 54: ' + str(arabic2wolfie(54)))
    print()

    # Part II
    print("Testing Part II")
    print("Testing wolfie2arabic() with wolfie = 'EII': " + str(wolfie2arabic('EII')))
    print("Testing wolfie2arabic() with wolfie = 'EFII': " + str(wolfie2arabic('EFII')))
    print("Testing wolfie2arabic() with wolfie = 'EEFII': " + str(wolfie2arabic('EEFII')))
    print("Testing wolfie2arabic() with wolfie = 'ETF': " + str(wolfie2arabic('ETF')))
    print("Testing wolfie2arabic() with wolfie = 'ETFII': " + str(wolfie2arabic('ETFII')))
    print("Testing wolfie2arabic() with wolfie = 'TEEFII': " + str(wolfie2arabic('TEEFII')))
