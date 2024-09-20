def mySort(list):
    if len(list) <= 1:
        return list
    
    mid = len(list) // 2
    left = mySort(list[:mid])
    right = mySort(list[mid:])

    def merge(left, right):
        result = []
        i, j = 0, 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])

        result.extend(right[j:])
        
        return result
    
    return merge(left, right)

# print(mySort([17, 0, -3, 2, 1, 0.5]))

def isPrime(num):
    if num == 1:
        return False
    else:
        mid = num // 2 + 1
        for i in range(2, mid + 1):
            if num % i == 0:
                return False
        return True

# print(isPrime(1))
# print(isPrime(5))
# print(isPrime(91))
# print(isPrime(1000000))

def palindrome(string):
    mid = len(string) // 2
    for i in range(0, mid):
        if string[i] != string[-(i + 1)]:
            return False
    return True

# print(palindrome("bearaeb")) # true
# print(palindrome("Whatever revetahW")) # true
# print(palindrome("Aloha, how are you today?")) # false
    
def pyramid(num):
    for i in range(1, num + 1):
        print(" " * (num - i) + "*" * (2 * i - 1))


# pyramid(1);
# # *
# pyramid(2);
# #  *
# # ***
# pyramid(4);
# #    *
# #   ***
# #  *****
# # *******

def inversePyramid(num):
    for i in range(num, 0, -1):
        print(" " * (num - i) + "*" * (2 * i - 1))
    
# inversePyramid(4);

def has_33(list):
    for i in range(0, len(list)):
        if list[i] == 3:
            if list[i + 1] == 3:
                return True
    return False
            
# print(has_33([1, 5, 7, 3, 3])) # True
# print(has_33([])) # False
# print(has_33([4, 3, 2, 1, 0])) # False

def spyGame(list):
    spy = []
    step = 0
    for i in list:
        step += 1
        if i == 0 or i == 7:
            spy.append(i)
            if (len(spy) >= 3) and (spy.count(0) >= 2) and (0 in spy and 7 in spy):
                return True
    return False
    
# print(spyGame([1, 2, 4, 0, 3, 0, 7])) # True
# print(spyGame([1, 2, 5, 0, 3, 1, 7])) # False