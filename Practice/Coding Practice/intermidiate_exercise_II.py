import math

def factorPrime(num):
    primes = []
    factor_primes = []
    result = ""

    if num < 4:
        result += num
    else:
        for i in range(2, int(math.sqrt(num)) + 1):
            if i < 4:
                primes.append(i)
            else:
                for j in range(2, int(math.sqrt(i)) + 1):
                    if i % j == 0 and i != j:
                        break
                    elif j == int(math.sqrt(i)):
                        primes.append(i)

    while num != 1:
        for prime in primes:
            while num % prime == 0:
                factor_primes.append(prime)
                num //= prime
                print(num)

    for i in range(0, len(factor_primes)):
        if i != len(factor_primes) - 1:
            result += (str(factor_primes[i]) + " x ")
        else:
            result += str(factor_primes[i])

    print(result)

# factorPrime(120)

def intersection(list1, list2):
    intersection = []
    if len(list1) < len(list2):
        major_list = list1
        minor_list = list2
    else:
        major_list = list2
        minor_list = list1
    
    for item in major_list:
        if item in minor_list:
            intersection.append(item)

    return intersection

# print(intersection([1, 3, 4, 6, 10], [5, 11, 4, 3, 100, 144, 0]))

# def flatten(higher_list):
#     result = []

#     def check_list(lst):
#         new_list = []
#         for i in range(0, len(lst)):
#             if isinstance(lst[i], list):
#                 check_list(lst[i])
#             else:
#                 new_list.append(lst[i])
#         return(new_list)
    
#     for item in check_list(higher_list):
#         result.append(item)
    
#     return result

def flatten(higher_list):
    result = []

    def check_list(lst):
        for i in lst:
            if isinstance(i, list):
                check_list(i)  # 遞迴處理內層列表
            else:
                result.append(i)  # 將非列表元素直接添加到 result

    check_list(higher_list)  # 開始展開傳入的列表
    return result

# print(flatten([1, [[], 2, [0, [1]], [3]], [1, 3, [3], [4, [1]], [2]]]))
            