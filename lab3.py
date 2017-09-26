# your name
# your NetID
# your SBU ID number
# CSE 101
# Lab #3

# In this part of the file it is very important that you write code inside
# the functions only. If you write code in between the functions, then the
# grading system will not be able to read your code or grade your work!


# Part I - Interleave: Fix Error(s)
def interleave(nums):
    new_nums = []
    if len(nums) == 0:
        return new_nums
    for i in range(len(nums[0])):
        for j in range(len(nums)):
            new_nums.append(nums[j][i])
    return new_nums


# Part II - Weighted GPA Calculator
def gpa_calculator(grades, credit_worth):
    total_grade = 0
    total_credits = 0
    if len(grades) == 0:
        return None
    for i in range(len(grades)):
        if grades[i].lower() == 'a':
            total_grade += 4 * credit_worth[i]
        elif grades[i].lower() == 'b':
            total_grade += 3 * credit_worth[i]
        elif grades[i].lower() == 'c':
            total_grade += 2 * credit_worth[i]
        elif grades[i].lower() == 'd':
            total_grade += 1 * credit_worth[i]
        elif grades[i].lower() != 'f':
            return None
    for credit in credit_worth:
        total_credits += credit
    return total_grade / total_credits


# Part III - Tuition Calculator
def tuition_calculator(student_type, num_credits):
    creditPrice = 0
    if student_type == 'In State':
        creditPrice = 300.0
    elif student_type == 'Out Of State':
        creditPrice = 600.0
    elif student_type == 'International':
        creditPrice = 900.0
    else:
        return None
    if 1 <= num_credits <= 11:
        return num_credits * creditPrice
    elif 12 <= num_credits <= 21:
        return 12 * creditPrice
    elif num_credits >= 22:
        return 12 * creditPrice + (num_credits - 21) * 1.1 * creditPrice
    return None


# Below you will see an if-statement and a few tests. It is REALLY important
# that you not delete this if-statement or the tests inside. You may, however,
# add more tests to the code below. You can format them however you like.
# Upload your lab2.py file to CodeLoad to see how it matches up against other
# test cases!
if __name__ == '__main__':
    # Part I
    print("Testing Part I:")
    print("Testing interleave() for nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]: " + str(
        interleave([[1, 2, 3], [4, 5, 6], [7, 8, 9]])))  # 3 lists with 3 elements each
    print("Testing interleave() for nums = [[0, 1, 0], [1, 0, 0], [0, 0, 1]]: " + str(
        interleave([[0, 1, 0], [1, 0, 0], [0, 0, 1]])))  # 3 lists with 3 elements each
    print("Testing interleave() for nums = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 0]]: " + str(
        interleave([[1, 2], [3, 4], [5, 6], [7, 8], [9, 0]])))  # 5 lists with 2 elements each
    print()

    # Part II
    print("Testing Part II:")
    print("Testing gpa_calculator() with grades = ['A', 'A', 'A', 'A'], credit_worth = [4, 3, 2, 3]: " + str(
        gpa_calculator(['A', 'A', 'A', 'A'], [4, 3, 2, 3])))  # Straight A's
    print("Testing gpa_calculator() with grades = ['F', 'F', 'F', 'F'], credit_worth = [2, 4, 3, 5]: " + str(
        gpa_calculator(['F', 'F', 'F', 'F'], [2, 4, 3, 5])))  # Straight F's
    print("Testing gpa_calculator() with grades = ['F','A','B','A','A'], credit_worth = [2,5,5,3,1]: " + str(
        gpa_calculator(['F', 'A', 'B', 'A', 'A'], [2, 5, 5, 3, 1])))  # Simple case
    print()

    # Part III
    print("Testing Part III:")
    print("Testing tuition_calculator() with student_type = 'In State', num_credits = 5: " + str(
        tuition_calculator('In State', 5)))  # In state part-time
    print("Testing tuition_calculator() with student_type = 'Out Of State', num_credits = 13: " + str(
        tuition_calculator('Out Of State', 12)))  # Out of state full-time
    print("Testing tuition_calculator() with student_type = 'International', num_credits = 22: " + str(
        tuition_calculator('International', 22)))  # International overload
