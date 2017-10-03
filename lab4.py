# your name
# your NetID
# your SBU ID number
# CSE 101
# Lab #4


def another_one(integer, divisor):
    return None


def premium_airlines(membership, price, points):
    return None


def unfair_hiring_system(applications, mood):
    return None


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
    print('Testing unfair_hiring_system() for applications = applications1, mood = 100: ' + str(
        unfair_hiring_system(applications1, 100)))
    print('Testing unfair_hiring_system() for applications = applications2, mood = 50: ' + str(
        unfair_hiring_system(applications2, 50)))
    print('Testing unfair_hiring_system() for applications = applications3, mood = 200: ' + str(
        unfair_hiring_system(applications3, 200)))
