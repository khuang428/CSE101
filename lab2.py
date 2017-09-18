# Karen Huang
# KARHUANG
# 111644515
# CSE 101
# Lab #2

# In this part of the file it is very important that you write code inside
# the functions only. If you write code in between the functions, then the
# grading system will not be able to read your code or grade your work!


# Part I
def student_status(num_credits):
    if num_credits > 11:
        return 'full-time'
    elif num_credits >= 1:
        return 'part-time'
    else:
        return 'unknown'


# Part II
def school_dilemma(age):
    if age < 6:
        return 'Too young for school'
    elif age < 11:
        return 'Elementary School'
    elif age < 14:
        return 'Middle School'
    elif age < 18:
        return 'High School'
    else:
        return 'College'


# Part III
def repair_shop(brand, damage_type, wind_shield, engine, tires):
    retStr = brand;
    if damage_type == 'Front':
        retStr += '@Repair front'
    elif damage_type == 'Rear':
        retStr += '@Repair rear'
    elif damage_type == 'Side':
        retStr += '@Repair side'
    if wind_shield:
        retStr += '@Wind shield'
    if engine:
        retStr += '@Engine'
    if tires:
        retStr += '@Tires'
    return retStr

# Part IV
def company_policy(name, experience, base_pay, age):
    result = name
    if 0 <= experience < 5:
        if 21 <= age < 25:
            if base_pay > 1000:
                result += '1'
            if base_pay > 5000:
                result += '2'  # Label 0
        elif 25 <= age < 40:
            if base_pay > 9000:
                result += '2'
        if experience > 3:
            result += '3'  # Label 1
    elif 5 <= experience <= 10:
        if 25 <= age < 40:
            if base_pay <= 10000:
                result += '4'  # Label 2
            if base_pay > 25000:
                result += '5'
            if base_pay > 50000:
                result += '2'  # Label 3
        if experience > 10:  # Intentionally Broken
            result += '6'  # Label 4
        elif experience > 7:
            result += '6'  # Label 5
    elif experience > 10:
        if age > 30:
            if base_pay < 30000:
                result += '4'  # Label 6
                result += '7'  # Label 7
            if experience > 15:
                if base_pay > 50000:
                    result += '5'  # Label 8
                    result += '8'  # Label 9
                else:
                    result += '8'  # Label 10
            else:
                result += '1'  # Label 11
                result += '7'  # Label 12
        else:
            result += '4'  # Label 13
            result += '6'  # Label 14
    return result


# Below you will see an if-statement and a few tests. It is REALLY important
# that you not delete this if-statement or the tests inside. You may, however,
# add more tests to the code below. You can format them however you like.
# Upload your lab2.py file to CodeLoad to see how it matches up against other
# test cases!
if __name__ == '__main__':
    # Testing Part I
    print('Testing student_status() for credits = 7: ' + str(student_status(7)))
    print('Testing student_status() for credits = 14: ' + str(student_status(14)))
    print('Testing student_status() for credits = -1: ' + str(student_status(-1)))
    print()

    # Testing Part II
    print('Testing school_dilemma() for age = 6: ' + str(school_dilemma(6)))
    print('Testing school_dilemma() for age = 1: ' + str(school_dilemma(1)))
    print('Testing school_dilemma() for age = 18: ' + str(school_dilemma(18)))
    print()

    # Testing Part III
    print(
        'Testing repair_shop() for brand = "Ford", damage = "Side", wind_shield = True, engine = False, tires = True: ' +
        str(repair_shop('Ford', 'Side', True, False, True)))
    print(
        'Testing repair_shop() for brand = "Mercedes", damage = "Rear", wind_shield = False, engine = True, tires = True: ' +
        str(repair_shop('Mercedes', 'Rear', False, True, True)))
    print(
        'Testing repair_shop() for brand = "Lexus", damage = "Front", wind_shield = True, engine = True, tires = False: ' +
        str(repair_shop('Lexus', 'Front', True, True, False)))
    print()

    # Testing Part IV
    name_test = 'kmac'
    experience_test = 0
    base_pay_test = 100000
    age_test = 100

    print('Testing company_policy() for name = ' + name_test + ' experience = ' + str(experience_test) +
          ' base_pay = ' + str(base_pay_test) + ' age = ' + str(age_test) + ': '+
          str(company_policy(name_test, experience_test, base_pay_test, age_test)))

