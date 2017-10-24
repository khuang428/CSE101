# Karen Huang
# KARHUANG
# 111644515
# CSE 101
# Lab #5

# In this part of the file it is very important that you write code inside
# the functions only. If you write code in between the functions, then the
# grading system will not be able to read your code or grade your work!


# Part I
def sequence(n):
    retStr = ''
    while n != 1:
        if n % 2 == 0:
            retStr += 'A'
        if n % 3 == 0:
            retStr += 'B'
        if n % 5 == 0:
            retStr += 'C'
        if n % 7 == 0:
            retStr += 'D'
        if n % 2 == 0:
            n //= 2
        else:
            n = 3*n + 1
    return retStr


# Part II
def session_simulator(clients, regular):
    timeUsed = 0
    for time in clients:
        if regular == 0:
            timeUsed += time // 2
        elif time > regular:
            timeUsed += regular + (time - regular) // 2
            regular = 0
        else:
            timeUsed += time
            regular -= time
    return timeUsed


# Part III
def cafe_day(orders):
    revenue = 0.0
    if len(orders) == 0:
        return revenue
    for order in orders:
        if len(order) == 4 and order[1] >= 0 and order[2] >= 0 and order[3] >= 0:
            if order[0] == 'P':
                if order[1] >= 3 or order[2] >= 4:
                    order[3] -= 3
                    if order[3] < 0:
                        order[3] = 0
                revenue += order[1] * 3.5 + order[2] * 2.5 + order[3] * 1.25
            elif order[0] == 'G':
                if (order[1] + order[2] + order[3]) >= 10:
                    revenue += .8 * (order[1] * 3.5 + order[2] * 2.5 + order[3] * 1.25)
                else:
                    revenue += order[1] * 3.5 + order[2] * 2.5 + order[3] * 1.25
            elif order[0] == 'S':
                revenue += .98 * (order[1] * 3.5 + order[2] * 2.5 + order[3] * 1.25)
    return revenue


# Below you will see an if-statement and a few tests. It is REALLY important
# that you not delete this if-statement or the tests inside. You may, however,
# add more tests to the code below. You can format them however you like.
# Upload your homework3.py file to CodeLoad to see how it matches up against other
# test cases!
if __name__ == '__main__':
    # Part I
    print("Testing Part I")
    print("Testing sequence() with n = 4: " + str(sequence(4)))
    print("Testing sequence() with n = 12: " + str(sequence(12)))
    print("Testing sequence() with n = 24: " + str(sequence(24)))
    print()

    # Part II
    print("Testing Part II")
    print("Testing session_simulator() with clients = [5, 5], regular = 10: " + str(session_simulator([5, 5], 10)))
    print("Testing session_simulator() with clients = [1, 5, 4, 11], regular = 10: " + str(
        session_simulator([1, 5, 4, 11], 10)))
    print("Testing session_simulator() with clients = [5, 7, 5, 6], regular = 20: " + str(
        session_simulator([5, 7, 5, 6], 20)))
    print("Testing with clients = [10, 2, 14, 15, 13, 6, 3, 7, 12, 8], regular = 9: " + str(
        session_simulator([10, 2, 14, 15, 13, 6, 3, 7, 12, 8], 9)))
    print()

    # Part III
    orders1 = [['P', 5, 0, 4]]
    orders2 = [['B', 1, 2, 3], ['P', 5, 0, 4], ['G', 4, 4, 2]]
    orders3 = [['G', 4, 3, 2], ['S', 0, 0, 10], ['P', 1, 4, 3]]
    print("Testing Part III")
    print("Testing cafe_day() with orders = orders1: " + str(cafe_day(orders1)))
    print("Testing cafe_day() with orders = orders2: " + str(cafe_day(orders2)))
    print("Testing cafe_day() with orders = orders3: " + str(cafe_day(orders3)))
    print()
