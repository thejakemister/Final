# Course: CS 30
# Period: 4
# Date created: 2020/01/23
# Date last modified: 2020/01/23
# Name: Jacob Leippi
# Description: Final porject, Problem 2

class_ave = []
# list of grades
class_size = 0
# amount of students
average = 0
# average grade

def Student_average():
    try:
        # tries to run the following code
        class_size = int(input("how many student are in the class? "))
        for class_size in range (1, class_size + 1):
            class_ave.append(int(input("enter the grade for student " +
            str(class_size) + ":")))
        print("thank you for using The Class Average Calculator")
    except:
        # runs if an error occurs of any kind
        print('invalid input')

Student_average()
# calls the function
