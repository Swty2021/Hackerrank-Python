#Finding the percentage
n = int(input("Enter no. of elements:"))
student_marks = {}
print (student_marks)
for i in range(1,n+1):
    name_key = input("Enter name:")
    name_val = list(range(n))
    student_marks[name_key] = name_val
    print (student_marks)
query_name = input("Enter student name:")
output = list(student_marks[query_name])
average = sum(output)/len(output)
format_average = "{:.2f}".format(average)
print(format_average)

