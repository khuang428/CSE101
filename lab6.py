# Karen Huang
# KARHUANG
# 111644515
# CSE 101
# Lab #6


# Part I
def kmac_salting(text, salt):
    if len(text) == 0:
        return text
    else:
        return text[0] + salt + kmac_salting(text[1:],salt)


# Part II
def sum_pairs(list1, list2):
    y = []
    if len(list1) == 0 and len(list2) == 0:
        return []
    elif len(list1) == 0:
        return list2
    elif len(list2) == 0:
        return list1
    else:
        y.append(list1[0] + list2[0])
    return y + sum_pairs(list1[1:], list2[1:])


# Part III
def gpa_calculator(grades):
    if credit_sum_helper(grades) == None or grade_points_helper(grades) == None:
        return None
    if len(grades) == 0:
        return 0.0
    else:
        #print(credit_sum_helper(grades))
        #print(grade_points_helper(grades))
        return grade_points_helper(grades) / credit_sum_helper(grades)

# Part III Helper Function #1
def credit_sum_helper(grades):
    if len(grades) == 0:
        return 0.0
    elif grades[0] not in 'AaBbCcDdFf' or grades[1] <= 0:
        return None
    if credit_sum_helper(grades[2:]) == None:
        return None
    else:
        return grades[1] + credit_sum_helper(grades[2:])
# Part III Helper Function #2
def grade_points_helper(grades):
    if len(grades) == 0:
        return 0.0
    elif grades[0] not in 'AaBbCcDdFf' or grades[1] <= 0:
        return None
    if grade_points_helper(grades[2:]) == None:
        return None
    else:
        if grades[0].lower() == 'a':
            return 4*grades[1] + grade_points_helper(grades[2:])
        elif grades[0].lower() == 'b':
            return 3*grades[1] + grade_points_helper(grades[2:])
        elif grades[0].lower() == 'c':
            return 2*grades[1] + grade_points_helper(grades[2:])
        elif grades[0].lower() == 'd':
            return 1*grades[1] + grade_points_helper(grades[2:])
        elif grades[0].lower() == 'f':
            return grade_points_helper(grades[2:])

if __name__ == '__main__':
    # Part I
    print('Testing Part I')
    print('Testing kmac_salting() for text = "ILOVECSE101", salt = "|": ' + str(kmac_salting("ILOVECSE101", "|")))
    print('Testing kmac_salting() for text = "Prof", salt = "kmAc": ' + str(kmac_salting("Prof", "KmAc")))
    print('Testing kmac_salting() for text = "", salt = "TEST": ' + str(kmac_salting("", "TEST")))
    print('Testing kmac_salting() for text = "A", salt = "xyz": ' + str(kmac_salting("A", "xyz")))
    print()

    # Part II
    print('Testing Part II')
    print('Testing sum_pairs() for list1 = [0, 1, 7], list2 = [2, 3]: ' + str(
        sum_pairs([0, 1, 7], [2, 3])))
    print('Testing sum_pairs() for list1 = [], list2 = [1, 2, 3, 4, 5]: ' + str(
        sum_pairs([], [1, 2, 3, 4, 5])))
    print('Testing sum_pairs() for list1 = [6, 7, 8], list2 = [15, 14, 13]: ' + str(
        sum_pairs([6, 7, 8], [15, 14, 13])))

    # Part III
    print('Testing Part III')
    print("Testing gpa_calculator() for grades = ['A', 4, 'B', 4, 'A', 4]: " + str(
        gpa_calculator(['A', 4, 'B', 4, 'A', 4])))
    print("Testing gpa_calculator() for grades = ['A', 4, 'B', 3, 'C', 1, 'F', 2]: " + str(
        gpa_calculator(['A', 4, 'Q', 3, 'C', 1, 'F', 2])))
    print("Testing gpa_calculator() for grades = []: " + str(
        gpa_calculator([])))
    print()

