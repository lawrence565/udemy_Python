class TypedList(list):
    def __init__(self, example_element, initial_list):
        self.type = type(example_element)
        if not isinstance(initial_list, list):
            raise TypeError("Second argument of Typelist must be a list.")
        for element in initial_list:
            self.__check(element)
        # self.elements = initial_list[:] # Copy by value to create another list, 自製版本
        super.__init__(initial_list)
    
    def __check(self, element):
        if type(element) != self.type:
            raise TypeError("Attempt to add an element of incorrect type to a TypedList.")
    
    def __setitem__(self, i, element):
        self.__check(element)
        # self.elements[i] = element
        return super().__setitem__(i, element)
    
    def __getitem__(self, i):
        # return self.elements[i]
        return super().__getitem__(i)
    
    # def __str__(self):
    #     return str(self.elements) 使用 super() 不需實作

a = TypedList("Hello", [" "] * 7)
b = TypedList("Hello", [" "] * 10)

print(a)
print(b)