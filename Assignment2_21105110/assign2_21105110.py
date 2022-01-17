#Q1
inputstr = input("Enter the string : ")
length= len(inputstr)
print("Length of the given string:", length)
rstr= inputstr[length: :-1]
print("Reverse string:", rstr)
nstr = inputstr[10:26]
print("New string :", nstr)
replacestr= inputstr.replace("a case sensitive","object oriented")
print("New replaced string :", replacestr)
index = inputstr.find("a")
print("Index of 'a':", index)
wstr = inputstr.replace(" ", "")
print("String without white spaces :", wstr)

#Q2
name= input("Enter your name :")
name1= "Hey, %s here!" %(name)
sid= int(input("Enter your SID :"))
sid1= "My SID is %d" %sid
dep = input("Enter your department :")
cgpa= float(input("Enter your CGPA :"))
dc = "I am from %s department and my CGPA is %f" %(dep,cgpa)
print(name1)
print(sid1)
print(dc)

#Q3
a=56
b=10
print("a&b :", (a&b))
print("a|b :", (a|b))
print("a^b :", (a^b))
print("Left shift both a and b with 2 bits : a = %d, b = %d" % (a << 2,b << 2))
print("Right shift a with 2 bits and b with 4 bits : a = %d, b = %d" % (a >> 2,b >> 4))

#Q4
num1 = 10
num2 = 14
num3 = 12

if (num1 >= num2) and (num1 >= num3):
   greatest = num1
elif (num2 >= num1) and (num2 >= num3):
   greatest = num2
else:
   greatest = num3

print("The greatest number is", greatest)

#Q5
s= input("Enter a string :")
s1= s.lower()
if "name" in s1:
    print("Yes")
else:
    print("No")

#Q6
s1=input("Enter number 1:")
s2=input("Enter number 2:")
s3=input("Enter number 3:")
x=int(s1)
y=int(s2)
z=int(s3)
if z > (x+y) or y > (x+z) or x > (y+z):
        print('No')
else:
        print('Yes')
