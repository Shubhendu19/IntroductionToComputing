#Q1
def TowerOfHanoi(n , origin, end, extra):
    if n == 0:
        return
    TowerOfHanoi(n-1, origin, end, extra)
    print("Move disk",n,"from",origin,"to",end)
    TowerOfHanoi(n-1, extra, end, origin)
         

n = 3
TowerOfHanoi(n, 'Origin', 'End', 'Extra')

#Q2
def factorial(n): 
    if (n==1 or n==0):          
        return 1     
    else:          
        return (n * factorial(n - 1))

n = int(input("Enter the number of rows:"))
for i in range(n):
    for j in range(n-i+1):
        print(end=" ") 
    for j in range(i+1): 
        print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
    print()

#Q3
def main(a,b):
    q0=(a//b)
    r0=(a%b)
    return q0,r0
x=int(input("Enter a number:"))
y=int(input("Enter a number:"))
l=list(main(x,y))
q=l[0]
r=l[1]
print("Quotient:",q)
print("Remainder:",r)

#a
if callable(main)==True:
    print("Function is callable")
else:
    print("Function is not callable")
if callable(x)==True:
    print("%d is callable" %(x))
else:
    print("%d is not callable" %(x))
if callable(y)==True:
    print("%d is callable" %(y))
else:
    print("%d is not callable" %(y))
    
#b
if all( v == 0 for v in l ) :
    print("They are all not non-zeros")
else:
    print("They are all non-zeros")

#c
ln=[q,r,4,5,6]
lr=[]
for i in ln:
    if i>4:
        lr.append(i)
print("Elements greater than 4: ",lr)

#d
s=set(lr)
print("Above solution in set data form:",s)

#e
frozenset(s)
print("Immutable set:",s)

#f
print("Max value from set:",max(s))
print(f"Hash value of {max(s)}:", hash(max(s)))

#Q4
class Student:
    def __init__(self,n,rn):
        self.n=n
        self.rn=rn
    def function(self):
        print("Name: ",self.n)
        print("Roll No.: ",self.rn)
    def __del__(self):
        print("Destructor Called")
name=Student("Shubhendu Roy", 21105110)
name.function()
del name

#Q5
class Employees:
    def __init__(self,n,s):
        self.n=n
        self.s=s
    def function(self):
        print(f"Employee name: {self.n} Salary: {self.s}")

n1=Employees("Mehak",40000)
n2=Employees("Ashok",50000)
n3=Employees("Viren",60000)

n1.function()
n2.function()
n3.function()

#a
print("Updating Mehak's salary to 70000")
n1.s=70000
n1.function()

#b
print("Viren's record deleted")
del n3

#Q6
def main(w1,w2):
    l1=[]
    l2=[]
    
    for i in w1:
        l1.append(i)
    for j in w2:
        l2.append(j)
    if (l1.sort()==l2.sort()):
        return True
    else:
        return False

word1=input("Barbie enter a word:").lower()
word2=input("George enter a word:").lower()

x=main(word1,word2)
if x==True:
    print("Real Friendship")
else:
    print("Fake Friendship")
    
