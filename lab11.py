# Karen Huang
# KARHUANG
# 111644515
# CSE 101
# Lab #11

# In this part of the file it is very important that you write code inside
# the functions only. If you write code in between the functions, then the
# grading system will not be able to read your code or grade your work!

import re


# Part I
def mac_checker(macs):
    retL = []
    pattern = r'^([\dA-F][\dA-F]:){5}[\dA-F][\dA-F]$'
    for mac in macs:
        if re.search(pattern, mac):
            retL.append(macs.index(mac))
    return retL


# Part II
def math_expr(expressions):
    retL = []
    pattern = r'^[+-]\d+\.\d+\s+[+\-*/^]\s+[+-]\d+\.\d+$'
    for exp in expressions:
        if re.search(pattern, exp):
            retL.append(expressions.index(exp))
    return retL


# Part III
def time_convert(original):
    retStr = 'invalid format'
    pattern = r'(([01]\d)|(2[0-3])):?[0-5][0-9]'
    if re.search(pattern, original):
        if int(original[0:2]) > 12:
            retStr = str(int(original[0:2]) - 12)
            if len(retStr) == 1:
                retStr = '0' + retStr
        elif int(original[0:2]) == 0:
            retStr = '12'
        else:
            retStr = original[0:2]
        retStr += ':' + original [-2:]
        if int(original[0:2]) >= 12:
            retStr += ' PM'
        else:
            retStr += ' AM'
    return retStr


# Part IV
def emergency(call):
    retStr = 'invalid format'
    pattern = r'Hello, my name is [A-Z]\w+ [A-Z]\w+\. I need to report (\w+ ?)+\. Please come to \d+ (\w+ ?)+\.'
    if re.search(pattern, call):
        retStr = ''
        callL = call.split()

        name = callL[4] + ' ' + callL[5][:-1]

        event = ''
        eventN = callL.index('Please')
        for n in range (10, eventN - 1):
            event += callL[n] + ' '
        event += callL[eventN - 1][:-1]

        place = ''
        placeN = callL.index('come') + 2
        for n in range(placeN, len(callL) - 1):
            place += callL[n] + ' '
        place += callL[-1][:-1]

        retStr += event + ' at ' + place + ' reported by ' + name
    return retStr


# Below you will see an if-statement and a few tests. It is REALLY important
# that you not delete this if-statement or the tests inside. You may, however,
# add more tests to the code below. You can format them however you like.
# Upload your homework3.py file to CodeLoad to see how it matches up against other
# test cases!
if __name__ == '__main__':
    # Part I
    print("### Testing Part I ###")
    macs1 = ['CE:9B:F1:02:94:49', '30:CF:39:7E:E6:9C', '3D:49:C7:23:B9:E8']
    macs2 = ['5E:1E:23:44:9F:17', '1P:CC:DD:EE:FF:11', '1D:D3,C1:1C:32:65']
    macs3 = ['91:13:6B:5C:3E:FF', 'DD:D1:5a:4F:2F:D4', 'A1:FC:54:AB!92:55']
    print("Testing mac_checker() with macs = macs1: " + str(mac_checker(macs1)))
    print("Testing mac_checker() with macs = macs2: " + str(mac_checker(macs2)))
    print("Testing mac_checker() with macs = macs3: " + str(mac_checker(macs3)))
    print()

    # Part II
    print("### Testing Part II ###")
    expressions1 = ['+1.1   * -1.1', '+3213.321 /  -121.1', '-131.5 - -11.5']
    expressions2 = ['31.11  ^ 2', '+123.321 ^   +321.123', '+1.23 +  -123.0']
    expressions3 = ['one.two   + thirty.two', '', '+s *  -3', '+3.3 -+5.5']
    print("Testing math_expr() with macs = expressions1: " + str(math_expr(expressions1)))
    print("Testing math_expr() with macs = expressions2: " + str(math_expr(expressions2)))
    print("Testing math_expr() with macs = expressions3: " + str(math_expr(expressions3)))
    print()

    # Part III
    print("### Testing Part III ###")
    print("Testing time_convert() for original = '23:59': " + str(time_convert('23:59')))
    print("Testing time_convert() for original = '0000': " + str(time_convert('0000')))
    print("Testing time_convert() for original = '12:59': " + str(time_convert('12:59')))
    print("Testing time_convert() for original = '01:10': " + str(time_convert('01:10')))
    print("Testing time_convert() for original = '1733': " + str(time_convert('1733')))
    print("Testing time_convert() for original = '24:00': " + str(time_convert('24:00')))
    print("Testing time_convert() for original = '13:13': " + str(time_convert('13:13')))
    print("Testing time_convert() for original = '8:55': " + str(time_convert('8:55')))
    print()

    # Part IV
    print("### Testing Part IV ###")
    call1 = 'Hello, my name is Yupeng Yin. I need to report a fire. Please come to 100 Circle Road.'
    call2 = 'Hello, my name is Wiktor Laima. I need to report a car accident. Please come to 2635 Simons Hollow Road.'
    call3 = 'Hello, my name is Joe M Bell. I need to report a robbery. Please come to 3595 Oakwood Avenue.'
    call4 = 'Hello, I need to report an assault. Please come to 3761 Hoffman Avenue.'
    print("Testing emergency() for call = call1: " + str(emergency(call1)))
    print("Testing emergency() for call = call2: " + str(emergency(call2)))
    print("Testing emergency() for call = call3: " + str(emergency(call3)))
    print("Testing emergency() for call = call4: " + str(emergency(call4)))
    print()