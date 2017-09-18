# Karen Huang
# KARHUANG
# 111644515
# CSE 101
# Homework #2

# In this part of the file it is very important that you write code inside
# the functions only. If you write code in between the functions, then the
# grading system will not be able to read your code or grade your work!


# Part I
def insurance(premium, age, gender):
    if age >= 60 or (18 <= age < 21 and gender == 'Male'):
        return premium
    elif 18 <= age < 21 and gender == 'Female':
        return premium * 0.9
    elif 21 <= age < 30:
        return premium * 0.75
    elif 30 <= age < 60 and gender == 'Female':
        return premium * 0.7
    elif 30 <= age < 60 and gender == 'Male':
        return premium * 0.6
    else:
        return -1


# Part II
def temperature_converter(value, scale_from, scale_to):
    if scale_from == scale_to:
        return value
    elif scale_from == 'C' and scale_to == 'K':
        return value + 273
    elif scale_from == 'K' and scale_to == 'C':
        return value - 273
    elif scale_from == 'C' and scale_to == 'F':
        return ((value * 9) / 5) + 32
    elif scale_from == 'F' and scale_to == 'C':
        return ((value - 32) * 5) / 9
    elif scale_from == 'K' and scale_to == 'F':
        return temperature_converter(temperature_converter(value,'K','C'),'C','F')
    elif scale_from == 'F' and scale_to == 'K':
        return temperature_converter(temperature_converter(value,'F','C'),'C','K')
    '''
    When you get too lazy to type out more math
    This looks disgusting though
    '''


# Part III
def row_boat(movements):
    meters = 0
    for move in movements:
        if move == 'F':
            meters += 1 #why no ++ :(
        if meters > 0 and move == 'B':
            meters -= 1
        if move == 'S':
            meters = 0;
    return meters


# Part IV
def untangle(numbers, len_of_sublist):
    return None


# Part V
def car_rental(rentals):
    car_type = [0, 0, 0, 0]  # Income generated Sedan, Coupe, SUV, Hybrid (in that order)

    return None


if __name__ == '__main__':
    # Testing Part I
    print("Part I: ")
    print("Testing insurance() with premium = 150, age = 20, gender = 'Female': " + str(insurance(150.0, 20, 'Female')))
    print("Testing insurance() with premium = 300, age = 25, gender = 'Male'  : " + str(insurance(300.0, 25, 'Male')))
    print("Testing insurance() with premium = 50,  age = 41, gender = 'Female': " + str(insurance(50.0, 41, 'Female')))
    print()

    # Testing Part II
    print("Part II: ")
    print("Testing temperature_converter() with value = 50, scale_from = 'K', scale_to = 'C': " + str(
        temperature_converter(50.0, 'K', 'C')))
    print("Testing temperature_converter() with value = 0,  scale_from = 'C', scale_to = 'F': " + str(
        temperature_converter(0.0, 'C', 'F')))
    print("Testing temperature_converter() with value = 32, scale_from = 'F', scale_to = 'C': " + str(
        temperature_converter(32.0, 'F', 'C')))
    print()

    # Testing Part III
    print("Part III: ")
    print("Testing row_boat() with movements = ['F', 'F', 'S', 'B', 'F']: " + str(
        row_boat(['F', 'F', 'S', 'B', 'F'])))
    print("Testing row_boat() with movements = ['S', 'S', 'S', 'B', 'S', 'B', 'B', 'B']: " + str(
        row_boat(['S', 'S', 'S', 'B', 'S', 'B', 'B', 'B'])))
    print("Testing row_boat() with movements = ['F', 'F', 'B', 'B', 'F', 'F', 'B', 'F', 'F']: " + str(
        row_boat(['F', 'F', 'B', 'B', 'F', 'F', 'B', 'F', 'F'])))
    print()

    # Testing Part IV
    print("Part IV: ")
    print("Testing untangle() with numbers = [1,2,3,4,5,6], len_of_sublist = 2: " + str(
        untangle([1, 2, 3, 4, 5, 6], 2)))
    print("Testing untangle() with numbers = [1,4,7,2,5,8,3,6,9], len_of_sublist = 3: " + str(
        untangle([1, 4, 7, 2, 5, 8, 3, 6, 9], 3)))
    print("Testing untangle() with numbers = [1,2,3], len_of_sublist = 1: " + str(untangle([1, 2, 3], 1)))
    print()

    # Testing Part V
    print("Part V: ")
    print("Testing car_rental() with rentals = [['Student','Coupe',4],['Faculty','Coupe',4],['Visitor','Coupe',4]]: " +
          str(car_rental([['Student', 'Coupe', 4], ['Faculty', 'Coupe', 4], ['Visitor', 'Coupe', 4]])))
    print("Testing car_rental() with rentals = [['Student','Coupe',4],['Faculty','SUV',4],['Visitor','Hybrid',4],['Visitor','Sedan',4]]: " +
          str(car_rental([['Student', 'Coupe', 4], ['Faculty', 'SUV', 4], ['Visitor', 'Hybrid', 4], ['Visitor', 'Sedan', 4]])))
    print("Testing car_rental() with rentals = [['Student','Coupe',3],['Faculty','SUV',2],['Visitor','Hybrid',1],['Visitor','Sedan',4]]: " +
          str(car_rental([['Student', 'Coupe', 3], ['Faculty', 'SUV', 2], ['Visitor', 'Hybrid', 1], ['Visitor', 'Sedan', 4]])))
    print()
