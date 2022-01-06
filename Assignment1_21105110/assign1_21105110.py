#Assignment 1
#Q1
n1 = int(input("Enter 1st Number:"))
n2 = int(input("Enter 2nd Number:"))
n3 = int(input("Enter 3rd Number:"))
avg = (n1 + n2 + n3) / 3
print("The average of three numbers: " , avg)

#Q2
ginc= float(input("Enter Gross Income:"))
nd= float(input("Enter number of dependents:"))
tinc= ginc-10000-(3000*nd)
tax= (tinc*20)/100
print("Tax:", tax)

#Q3
student=[21105110,'Shubhendu Roy','M','ECE', 8.5]         
print("Student:",student)


#Q4
print("Marks of five student")
Marks= [96,56,75,48,83]
print("Marks in unsorted manner",Marks)          
Marks.sort()
print("Marks in sorted manner",Marks)

#Q5a.
color= ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color.pop(3)
print(color)
          
#Q5b.
colors= ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
colors[3:5]=["Purple"]
print(colors)          
