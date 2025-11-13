#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      adsmith
#
# Created:     20/09/2024
# Copyright:   (c) adsmith 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

numList = []

def menu():
    user = 0
    while user != 8:
        printMenu()
        user = int(input("type in the number of your choice: "))
        if user == 1:
            menuItemOne()
        if user == 2:
            menuItemTwo()
        if user == 3:
            menuItemThree()
        if user == 4:
            menuItemFour()
        if user == 5:
            menuItemFive()
        if user == 6:
            menuItemSix()
        if user == 7:
            menuItemSeven()
        if user == 8:
            menuItemEight()
        if user == 9:
            menuItemNine()
        if user == 0:
            print("thank you for using the menu")


def printMenu():
    print("1. Item one")
    print("2. Item two")
    print("3. Item three")
    print("4. Item four")
    print("5. Item five")
    print("6. Item six")
    print("7. Item seven")
    print("8. Item eight")
    print("9. Item nine")
    print("0. exit")


def menuItemOne():
    global numList
    try:
        numList.append(int(input("What would you like  to  add to the list?: ")))
    except (ValueError, KeyboardInterrupt, SystemExit):
        print("Invalid input. Please enter a valid integer.")
    print(numList)


def menuItemTwo():
    global numList
    numList = input("What is your list of numbers?: ")
    try:
        # Split the input by spaces and map the values to integers
        numList = list(map(int, numList.split()))
        print(numList)
    except (ValueError, KeyboardInterrupt, SystemExit):
        print("Invalid input. Please enter a valid list.")
    try:
        numList.remove(int(input("What number would you like removed from the list?: ")))
        print(numList)
    except (ValueError, KeyboardInterrupt, SystemExit):
        print("Invalid input. Please enter a valid number.")


def menuItemThree():
    global numList
    numList = input("What is your list of numbers?: ")
    try:
        # Split the input by spaces and map the values to integers
        numList = list(map(int, numList.split()))
        print(numList)
    except (ValueError, KeyboardInterrupt, SystemExit):
        print("Invalid input. Please enter a valid list.")
    try:
        numList.pop(int(input("What number position would you like removed from the list?: ")))
        print(numList)
    except (ValueError, KeyboardInterrupt, SystemExit):
        print("Invalid input. Please enter a valid number.")


def menuItemFour():
    global numList
    numList = input("What is your list of numbers?: ")
    try:
        # Split the input by spaces and map the values to integers
        numList = list(map(int, numList.split()))
        print(numList)
    except (ValueError, KeyboardInterrupt, SystemExit):
        print("Invalid input. Please enter a valid list.")


def menuItemFive():
    global numList
    numList = input("What is your list of numbers?: ")
    try:
        # Split the input by spaces and map the values to integers
        numList = list(map(int, numList.split()))
        meanNums = sum(numList) / len(numList)
        print(meanNums)
    except (ValueError, KeyboardInterrupt, SystemExit):
        print("Invalid input. Please enter a valid list.")


def menuItemSix():
    global numList
    numList = input("What is your list of numbers?: ")
    try:
        # Split the input by spaces and map the values to integers
        numList = list(map(int, numList.split()))
        sorted_list = sorted(numList)
        n = len(sorted_list)
        if n % 2 == 1:
            median = sorted_list[n // 2]
        else:
            mid1 = sorted_list[n // 2 - 1]
            mid2 = sorted_list[n // 2]
            median = (mid1 + mid2) / 2
        print(median)
    except (ValueError, KeyboardInterrupt, SystemExit):
        print("Invalid input. Please enter a valid list.")


def menuItemSeven():
    global numList
    numList = input("What is your list of numbers?: ")
    try:
        # Split the input by spaces and map the values to integers
        numList = list(map(int, numList.split()))
        if len(numList) == 0:
            print("The list is empty.")
        elif len(numList) % 2 != 0:
            mid_index = len(numList) // 2
            print(numList[mid_index])
        else:
            mid_index = len(numList) // 2
            print(numList[mid_index - 1])
    except (ValueError, KeyboardInterrupt, SystemExit):
        print("Invalid input. Please enter a valid list.")


def menuItemEight():
    global numList
    numList = input("What is your list of numbers?: ")
    try:
        # Split the input by spaces and map the values to integers
        numList = list(map(int, numList.split()))
        counts = {}
        for item in numList:
            counts[item] = counts.get(item, 0) + 1
        max_freq = 0
        for i in counts.values():
            if i > max_freq:
                max_freq = i
        modes = [item for item, i in counts.items() if i == max_freq]
        print(modes)
    except (ValueError, KeyboardInterrupt, SystemExit):
        print("Invalid input. Please enter a valid list.")


def menuItemNine():
    global numList
    numList = input("What is your list of numbers?: ")
    try:
        # Split the input by spaces and map the values to integers
        numList = list(map(int, numList.split()))
        varience = 0
        standardDiff = 0
        squaredDiff = []
        mean = sum(numList) / len(numList)
        for i in numList:
            squaredDiff.append((i - mean) ** 2)
        varience = sum(squaredDiff) / (len(numList) - 1)
        standardDiff = varience ** 0.5
        print(standardDiff)
    except (ValueError, KeyboardInterrupt, SystemExit):
        print("Invalid input. Please enter a valid list.")


def main():
    menu()


if __name__ == '__main__':
    main()
