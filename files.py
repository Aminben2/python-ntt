def read_file_and_print_it(filename=""):
    if isinstance(filename,str):
        with open(filename,"r+",encoding="utf-8") as file :
            lines = file.readlines()
            for i in lines:
                print(i,end="")
    else: 
        print("provide a valid filename")

# read_file_and_print_it("amine.txt")


def write_file(filename,text):
    if isinstance(filename,str) and isinstance(text,str):
        with open(filename,"w+",encoding="utf-8") as file :
            return file.write(text)
    else: 
        print("provide a valid filename/text")


# print(write_file("amine.txt","amine"))

import json
def to_json_string(my_obj):
    return json.dumps(my_obj)


s =to_json_string({"amine":2,"ben":6})
# print(type(s))


def from_json_string(s):
    return json.loads(s)

o = from_json_string('{"amine":25, "ben": 4146}')
# print(o)
# print(type(o))

def save_to_json_file(my_obj,filename):
    write_file(filename,json.dumps(my_obj))

# save_to_json_file({1:"amine",2:"ben"},"amine.json")


def load_from_json_file(filename):
    with open(filename,"r+") as file :
        c = file.read()
        return json.loads(c)
    
ob = load_from_json_file("amine.json")
# print(ob)
# print(type(ob))


def class_to_json(o):
    return o.__dict__

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def to_json(self):
        return self.__dict__
    

student = Student("Alice", 25)
print(student.to_json())

