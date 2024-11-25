def count_words(s):
    words_count = {}
    all_words = s.split(" ")
    for i in all_words :
        if i in words_count :
            words_count[i] = words_count[i] + 1
        else :
            words_count[i] = 1
    return words_count

# print(count_words("amine ben omar omar ben"))

def count_pair(l):
    pair_count = {}
    for i in l :
        if i % 2 == 0:
            if i in pair_count :
                pair_count[i] = pair_count[i] + 1
            else :
                pair_count[i] = 1
    return pair_count

# print(count_pair([5,2,2,2,4,5,4,2,1,7,5,6]))
        

def count_chars_infile(filePath):
    chars_count = {}
    with open(filePath,"r+") as file :
        lines = file.readlines()
        for line in lines :
            for char in line :
                if char in chars_count :
                    chars_count[char] = chars_count[char] + 1
                else :
                    chars_count[char] = 1
    return chars_count


# print(count_chars_infile("f.txt"))

def get_student_notes(filePath):
    notes = {}
    with open(filePath,"r+") as file :
        lines = file.readlines()
        for line in lines:
            p = line.split(";")
            notes[p[0]] = p[1]
    return notes

# print(get_student_notes("st.txt"))

def str_to_int_date(l):
    new = []
    for i in l :
        date = i.split("/")
        new.append((int(date[0]),int(date[1]),int(date[2])))
    return new

# print(str_to_int_date( ["12/05/2022", "25/09/2023", "08/11/2021"]))


def extact_from_email(l):
    users = {}
    for i in l :
        y = i.split("@")
        users[y[0]] = y[1]
    return users

# print(extact_from_email( ["john.doe@example.com", 
# "alice.smith@gmail.com", "bob.jones@yahoo.com"]))

def stef_files(l):
    files = {}
    for i in l :
        file = i.split(".")
        if file[1] in files :
            files[file[1]].append(i)
        else :
            files[file[1]] = [i]
    return files

# print(stef_files(["document1.txt", "image.png", "script.js", "document2.txt"],))


# def lengthOfLastWord(s: str) -> int:
#     if len(s) == 1 and s[0] != " ":
#         return 1
#     i = len(s) - 1
#     print(i)
#     l = 0
#     while i >= 0:
#         while s[i] and s[i] == " ":
#             i -= 1
#         while s[i] and  s[i] != " ":
#             i -= 1
#             l += 1
#         i -= 1
#         break
#     return l

# print(lengthOfLastWord("day"))


# def plusOne( digits):
#     num = 0
#     for i in digits :
#         num = num * 10 + i
    
#     new = num + 1
#     num_str = str(new)
#     digits_str = list(num_str)
#     digits_return = []
#     for i in range(len(digits_str)):
#         digits_return.append(int(digits_str[i]))
#     return digits_return 

# print(plusOne([1,5,4,5]))

# def isPalindrome(s):
#     """
#     :type s: str
#     :rtype: bool
#     """
#     new = ""
#     for i in s :
#         if i.isalnum() :
#             new += i
#     new = new.lower()
#     index = 0
#     for j in range(len(new) - 1,-1,-1):
#         if new[index] != new[j]:
#             return False
#         index += 1
#     return True


# print(isPalindrome("A man, a plan, a canal: Panama"))



