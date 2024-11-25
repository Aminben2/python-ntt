class Rectangle:
    number_of_instances = 0
    print_symbol = "#"
    def __init__(self,width= 0,height = 0):
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

    def getHeight(self):
        return self.__height
    def setHeight(self,p):
        if not isinstance(p.str) :
            raise TypeError("height must be an integer")
        if p < 0 :
            raise ValueError("height must be >= 0")
        self.__height=p

    def getWidth(self):
        return self.__width
    def setWidth(self,p):
        if not isinstance(p.str) :
            raise TypeError("width must be an integer")
        if p < 0 :
            raise ValueError("width must be >= 0")
        self.__width=p

    def area(self):
        return self.__height * self.__width
    
    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2*(self.__height + self.__width)
    
    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        s = ""
        for i in range(self.__height):
            for j in range(self.__width):
                s = s + str(Rectangle.print_symbol)
            s = s + "\n"
        return s
    
    def __repr__(self):
        return "Rectangle(width = 0, height = 0)"
    
    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
    
    @staticmethod
    def square(w):
        return Rectangle(w,w)

    @staticmethod
    def bigger_or_equal(obj1, obj2):
        if isinstance(obj1,Rectangle) and isinstance(obj2,Rectangle):
            return obj1 if obj1.area() > obj2.area() else obj2
        raise TypeError("Provide two Rectangle")



class MyClass:
    pass

def lookup(obj):
    return dir(obj)

class MyList(list):
    def print_sorted(self):
        new = self[:]
        new_sorted = sorted(new)
        for i in new_sorted:
            print(i,end=" ")
        
# my_list = MyList([3, 1, 4, 2])
# my_list.print_sorted()  # Output: [1, 2, 3, 4]
# print(my_list)  # Output: [3, 1, 4, 2]


def is_kind_of_class(obj,cl):
    check = False
    for i in cl.__subclasses__():
        if isinstance(obj,i): check = True ; break
    if isinstance(obj,cl) or check : return True
    return False

# class BaseClass:
#     pass

# class SubClass(BaseClass):
#     pass

# obj1 = BaseClass()
# obj2 = SubClass()

# print(is_kind_of_class(obj1, BaseClass))  # Output: True
# print(is_kind_of_class(obj2, BaseClass))  # Output: True
# print(is_kind_of_class(obj1, SubClass))   # Output: False

def inherits_from(obj , cl):
    sbs = cl.__subclasses__()
    for i in sbs :
        if isinstance(obj,i) and i != cl: return True
    return False

# class BaseClass:
#     pass

# class SubClass(BaseClass):
#     pass

# obj1 = BaseClass()
# obj2 = SubClass()

# print(inherits_from(obj2, BaseClass))  # Output: True
# print(inherits_from(obj1, BaseClass))  # Output: False


class BaseGeometry:
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value,int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0 : 
            raise ValueError(f"{name} must be greater than 0")
    
class Rectangle(BaseGeometry):
    def __init__(self,width,height):
        self.integer_validator("height",height)
        self.integer_validator("width",width)
        self.__height = height
        self.__width = width

    def area(self):
        return self.__height * self.__width
    
    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle) :
    def __init__(self,size):
        self.integer_validator("size",size)
        super().__init__(size,size)
        self._size = size
    

class MyInt(int):
    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)



def add_attribute(obj ,n,v):
    if not hasattr(obj,"__dict__"): raise TypeError("can't add new attribute")
    setattr(obj,n,v)
    
