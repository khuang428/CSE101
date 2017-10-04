# Karen Huang
# KARHUANG
# 111644515
# CSE 101
# Lab #4


def another_one(integer, divisor):
    times = 0
    if divisor == 0:
        return 0
    while integer // divisor != 0:
        times += 1
        integer //= divisor
    return times+1


def premium_airlines(membership, price, points):
    if membership == 'Regular':
        if price >= 5000:
            points += 5
    elif membership == 'Platinum':
        if price >= 5000:
            points += 35
        elif price >= 2000:
            points += 20
    elif membership == 'Diamond':
        if price >= 5000:
            points += 35
        elif price >= 2000 and points > 300:
            points += 30
        elif price >= 500 and points >= 100:
            points += 10
        elif points >= 25:
            points += 2
    return points


def unfair_hiring_system(applications, mood):
    hireList = []
    index = 0
    curMood = mood
    while curMood > 0 and index < len(applications):
        if applications[index] == 'Strong':
            hireList.append(index)
            curMood += 2
        elif applications[index] == 'Fair':
            if curMood >= mood // 2:
                hireList.append(index)
                curMood += 1
            else:
                curMood -= 2
        elif applications[index] == 'Poor':
            if curMood >= (3 * mood) // 4:
                hireList.append(index)
                curMood -= 1
            else:
                curMood -= 5
        elif applications[index] == 'Disaster':
            curMood -= 10
        index += 1
        curMood -= 1
    return hireList


if __name__ == '__main__':
    # Part I
    print('Testing another_one() for integer = 123, divisor = 2: ' + str(another_one(123, 2)))
    print('Testing another_one() for integer = 512, divisor = 3: ' + str(another_one(512, 3)))
    print('Testing another_one() for integer = 132, divisor = 5: ' + str(another_one(132, 5)))
    print()

    # Part II
    print('Testing premium_airlines() for membership = "Diamond", price = 4999, points = 700: ' + str(
        premium_airlines("Diamond", 4999, 700)))
    print('Testing premium_airlines() for membership = "Regular", price = 5000, points = 300: ' + str(
        premium_airlines("Regular", 5000, 300)))
    print('Testing premium_airlines() for membership = "Platinum", price = 500. points = 1000: ' + str(
        premium_airlines("Platinum", 500, 1000)))
    print()

    # Part III
    applications1 = ['Strong', 'Fair', 'Disaster']
    applications2 = []
    applications3 = ['Disaster', 'Poor', 'Disaster', 'Disaster', 'Disaster', 'Poor', 'Disaster', 'Poor']
    applications4 = ['Strong', 'Poor', 'Disaster', 'Fair', 'Fair', 'Strong', 'Poor', 'Poor', 'Fair', 'Fair', 'Fair',
                    'Disaster', 'Fair', 'Fair', 'Poor', 'Fair', 'Disaster', 'Disaster']
    print('Testing unfair_hiring_system() for applications = applications1, mood = 100: ' + str(
        unfair_hiring_system(applications1, 100)))
    print('Testing unfair_hiring_system() for applications = applications2, mood = 50: ' + str(
        unfair_hiring_system(applications2, 50)))
    print('Testing unfair_hiring_system() for applications = applications3, mood = 200: ' + str(
        unfair_hiring_system(applications3, 200)))
    print('Testing unfair_hiring_system() for applications = applications4, mood = 42: ' + str(
        unfair_hiring_system(applications4, 42)))
