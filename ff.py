if __name__ == "__main__":
    import sys
    from json import loads , dumps

    def load_from_json_file(filename):
        with open(filename,"r+") as file :
            c = file.read()
            return loads(c)
        
    def write_file(filename,text):
        if isinstance(filename,str) and isinstance(text,str):
            with open(filename,"w+",encoding="utf-8") as file :
                return file.write(text)
        else: 
            print("provide a valid filename/text")
        
    def save_to_json_file(my_obj,filename):
        write_file(filename,dumps(my_obj))

    try :
        file = open("amine.json")
        fileName = file.name
        items = load_from_json_file(fileName)
        items = items +  sys.argv[1:]
        save_to_json_file(items,fileName)
    except FileNotFoundError :
        print("file does not exists !")
