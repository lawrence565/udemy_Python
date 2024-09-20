def star(layer):
    for i in range(1, layer + 1):
        print('*' * i)

# star(1)
# star(4)

def stars2(layer):
    for i in range(1, layer):
        print('*' * i)
    for i in range(layer, 0, -1):
        print('*' * i)

# stars2(1)
# stars2(2)
# stars2(3)
# stars2(4)

def table(num):
    for i in range(1, 10):
        print(f"{num} x {i} = {num * i}")

# table(3)

def table9to9():
    for i in range(1, 10):
        for j in range(1, 10):
            print(f"{i} x {j} = {i * j}")

# table9to9()

def swap(string):
    result = ""
    for i in string:
        if i == i.upper():
            result += i.lower()
        else: 
            result += i.upper()
        
    return result

# print(swap("Aloha")) # returns "aLOHA"
# print(swap("Love you.")) # returns "lOVE YOU."

def findMin(list):
    if len(list) > 0:
        minimum = list[0]
    else:
        return
    
    for i in list:
        if i < minimum:
            minimum = i
    return minimum

# print(findMin([1, 2, 5, 6, 99, 4, 5])) # returns 1
# print(findMin([])) # returns undefined
# print(findMin([1, 6, 0, 33, 44, 88, -10])) # returns -10