def printMany():
    for i in range(1, 101):
        print(i)

def printEvery3():
    for i in range(1, 89, 3):
        print(i)

def position(string):
    result = -1;
    for i in string:
        if i == i.upper():
            result = i, string.index(i)
            break
    print(result)

# position("abcd")  # returns -1
# position("AbcD")  # returns ('A', 0)
# position("abCD")  # returns ('C', 2)

def findSmallCount(number_list, base):
    counter = 0
    for i in number_list:
        if i < base:
            counter += 1
    return counter

# print(findSmallCount([1, 2, 3], 2)) # returns 1
# print(findSmallCount([1, 2, 3, 4, 5], 0)) # returns 0

def findSmallerTotal(number_list, base):
    result = 0
    for i in number_list:
        if i < base:
            result += i
    return result

# print(findSmallerTotal([1, 2, 3], 3)) # returns 3
# print(findSmallerTotal([1, 2, 3], 1)) # returns 0
# print(findSmallerTotal([3, 2, 5, 8, 7], 999)) # returns 25
# print(findSmallerTotal([3, 2, 5, 8, 7], 0)) # returns 0

def findAllSmall(number_list, base):
    result = []
    for i in number_list:
        if i < base:
            result.append(i)
    return result

# print(findAllSmall([1, 2, 3], 10)) # returns [1, 2, 3]
# print(findAllSmall([1, 2, 3], 2)) # returns [1]
# print(findAllSmall([1, 3, 5, 4, 2], 4)) #  returns [1, 3, 2]

def summ(number_list):
    result = 0
    for i in number_list:
        result += i
    return result

# print(summ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])); # returns 55
# print(summ([])); # return 0
# print(summ([-10, -20, -30])); # return -60