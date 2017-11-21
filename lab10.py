# Karen Huang
# KARHUANG
# 111644515
# CSE 101
# Lab #10

# In this part of the file it is very important that you write code inside
# the functions only. If you write code in between the functions, then the
# grading system will not be able to read your code or grade your work!


# Part I
def decimal_to_fixed_point(value):
    retStr = ''
    if value[0] == '-':
        retStr += '-'
        value = value[1:]
    val = value.split('.')
    retStr += bin(int(val[0]))[2:] + '.'
    dec = float('.' + val[1])
    for n in range(23):
        dec *= 2
        if dec < 1:
            retStr += '0'
        else:
            retStr += '1'
            dec %= 1
    return retStr


# Part II
def fixed_point_to_floating_point(value):
    retStr = ''
    expStr = ''
    mantissa = ''
    if value[0] == '-':
        retStr += '1'
        value = value[1:]
    else:
        retStr += '0'

    if float(value) > 1.0:
        exp = value.index('.') - 1
    elif '1' in value:
        exp = value.index('.') - value.index('1')
    else:
        exp = -127
    if exp < 1:
        expStr += '0'
    expStr += bin(127 + exp)[2:]
    while len(expStr) < 8:
        expStr += '0'
    retStr += expStr

    value = value.replace('.', '')
    if '1' in value:
        while value[0] != '1':
            value = value[1:]
        value = value[1:]
    mantissa = value
    while len(mantissa) > 23:
        mantissa = mantissa[:-1]
    while len(mantissa) < 23:
        mantissa += '0'
    retStr += mantissa

    return retStr

if __name__ == '__main__':
    # Testing Part I
    value = '-12.125'
    print('Testing decimal_to_fixed_point() for value = ' + value + ': ' + str(decimal_to_fixed_point(value)))
    value = '7.4'
    print('Testing decimal_to_fixed_point() for value = ' + value + ': ' + str(decimal_to_fixed_point(value)))
    value = '-0.00625'
    print('Testing decimal_to_fixed_point() for value = ' + value + ': ' + str(decimal_to_fixed_point(value)))
    value = '-0.0'
    print('Testing decimal_to_fixed_point() for value = ' + value + ': ' + str(decimal_to_fixed_point(value)))

    print()

    # Testing Part II
    value = '-1100.00100000000000000000000'
    print('Testing fixed_point_to_floating_point() for value = ' + value + ': ' + str(
        fixed_point_to_floating_point(value)))

    value = '-0.00011100001010001111010'
    print('Testing fixed_point_to_floating_point() for value = ' + value + ': ' + str(
        fixed_point_to_floating_point(value)))

    value = '-0.00000000000000000000000'
    print('Testing fixed_point_to_floating_point() for value = ' + value + ': ' + str(
        fixed_point_to_floating_point(value)))

    value = '1111011.01110100111010100100101'
    print('Testing fixed_point_to_floating_point() for value = ' + value + ': ' + str(
        fixed_point_to_floating_point(value)))

    value = '111001111.00100101011110001100010'
    print('Testing fixed_point_to_floating_point() for value = ' + value + ': ' + str(
        fixed_point_to_floating_point(value)))
