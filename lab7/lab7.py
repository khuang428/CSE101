# Karen Huang
# KARHUANG
# 111644515
# CSE 101
# Lab #7

# In this part of the file it is very important that you write code inside
# the functions only. If you write code in between the functions, then the
# grading system will not be able to read your code or grade your work!


# Part I
def trip(max_distance, places):
    dist = 0
    dest = 'nowhere'
    if max_distance <= 0:
        return None
    for place in places:
        if places[place] > dist and places[place] < max_distance:
            dist = places[place]
            dest = place
    return dest

# Part II
def insert_tag(input_filename, output_filename, tag, target_word):
    output = open(output_filename, 'w')
    newWord = '<' + tag + '>' + target_word + '</' + tag + '>'
    for line in open(input_filename):
        newLine = line.replace(target_word, newWord)
        output.write(newLine)
    output.close()
    return None


# Part III
def shop(filename, shopping_list):
    price = 0.0
    shop_list = shopping_list.split(',')
    if len(shop_list) == 0:
        return price
    products = {}
    for line in open(filename):
        product = line.split(',')
        products[product[0]] = float(product[1])
    for n in range(0,len(shop_list),2):
        if shop_list[n] in products:
            price += float(shop_list[n+1]) * products[shop_list[n]]
    return price




# Part IV
def robot_competition(robot1, robot2):
    index1 = 0
    index2 = 0
    position1 = 0
    position2 = 0
    for i in range(max(len(robot1), len(robot2))):
        if len(robot1) > index1:
            if robot1[index1] == 'F':
                position1 += 1
            elif robot1[index1] == 'B':
                if position1 > 0:
                    position1 -= 1
            elif robot1[index1] == 'R':
                position1 = 0
        if len(robot2) > index2:
            if robot2[index2] == 'F':
                position2 += 1
            elif robot2[index2] == 'B':
                if position2 > 0:
                    position2 -= 1
            elif robot2[index2] == 'R':
                position2 = 0

        index1 += 1
        index2 += 1

    if position1 > position2:
        return 1
    elif position2 > position1:
        return 2
    else:
        return 0


# Below you will see an if-statement and a few tests. It is REALLY important
# that you not delete this if-statement or the tests inside. You may, however,
# add more tests to the code below. You can format them however you like.
# Upload your homework3.py file to CodeLoad to see how it matches up against other
# test cases!
if __name__ == '__main__':
    # Part I
    locations = {'Beijing': 6836, 'Los Angeles': 2448, 'New York': 50, 'San Francisco': 2569,
                 'Washington D.C.': 204, 'Pittsburgh': 315, 'Columbus': 477, 'Tokyo': 6749,
                 'Moscow': 4672, 'Paris': 3649, 'Las Vegas': 2230, 'Kansas City': 1095,
                 'Iowa City': 913, 'Orlando': 940, 'Island of Hawaii': 4927, 'City B': 1399}
    print("Testing Part I")
    print("Testing trip() for max_distance = 1000, places = locations: "
          + str(trip(1000, locations)))
    print("Testing trip() for max_distance = 0, places = locations: "
          + str(trip(0, locations)))
    print("Testing trip() for max_distance = 3848, places = locations: "
          + str(trip(3848, locations)))
    print("Testing trip() for max_distance = 10, places = locations: "
          + str(trip(10, locations)))
    print()

    # Part II
    print("Testing Part II")
    print("Reminder: please compare your output file with the 'expectedX.html' files provided for you.")
    print("Testing insert_tag() with input_filename = 'sample1.html', output_filename = 'modified1.html', "
          + "tag = 'i', target_word = 'Python'")
    insert_tag('sample1.html', 'modified1.html', 'i', 'Python')

    print("Testing insert_tag() with input_filename = 'sample2.html', output_filename = 'modified2.html', "
          + "tag = 'b', target_word = 'buffalo'")
    insert_tag('sample2.html', 'modified2.html', 'b', 'buffalo')

    print("Testing insert_tag() with input_filename = 'sample3.html', output_filename = 'modified3.html', "
          + "tag = 'u', target_word = 'Stony'")
    insert_tag('sample3.html', 'modified3.html', 'u', 'Stony')
    print()

    # Part III
    list1 = ''
    list2 = 'Ketchup,4,Mustard,10,tooth paste,1,Avocados,1'
    list3 = 'Tuna,1,Honey,1,Free Rice,79,Ginger Bread,4'
    print("Testing Part III")
    print("Testing shop() with filename = 'prices1.txt', shopping_list = ls1: "
          + str(shop('prices1.txt', list1)))
    print("Testing shop() with filename = 'prices2.txt', shopping_list = ls2: "
          + str(shop('prices2.txt', list2)))
    print("Testing shop() with filename = 'prices3.txt', shopping_list = ls3: "
          + str(shop('prices3.txt', list3)))
    print()

    # Part IV
    print("Testing Part IV")
    print(
        "Testing robot_competition() for robot1 = ['F','B','B','A','R','F','F'], robot2 = ['B','C','D','R','F','F']: " +
        str(robot_competition(['F', 'B', 'B', 'A', 'R', 'F', 'F'], ['B', 'C', 'D', 'R', 'F', 'F'])))
    print("Testing robot_competition() for robot1 = ['F','B','B','A','R','F','F'], robot2 = ['R','F','F','F']: " +
          str(robot_competition(['F', 'B', 'B', 'A', 'R', 'F', 'F'], ['R', 'F', 'F', 'F'])))
    print("Testing robot_competition() for robot1 = [], robot2 = []: " +
          str(robot_competition([], [])))
