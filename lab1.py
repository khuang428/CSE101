# Karen Huang
# KARHUANG
# 111644515
# CSE 101
# Lab 1


# Computes the quantity x^2 + 3y + 4
def compute(x, y):
    return x**2 + 3*y + 4


if __name__ == '__main__':
    print('Testing compute(): with x = 7, y = 2: ' + str(compute(7, 2)))
    print('Testing compute(): with x = 2, y = 7: ' + str(compute(2, 7)))
    print('Testing compute(): with x = 14, y = 3: ' + str(compute(14, 3)))
