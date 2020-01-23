# Course: CS 30
# Period: 4
# Date created: 2020/01/23
# Date last modified: 2020/01/23
# Name: Jacob Leippi
# Description: Final porject, Problem 2

class_ave = []
class_size = 0
average = 0

class_size = int(input("how many student are in the class? "))
for class_size in range(1, class_size + 1):
    class_ave.append(int(input("enter the grade for student " +
    str(class_size) + ":")))
    average = int(class_ave) + int(class_ave)


print(average)
print(class_ave)
print(class_size)
