#Q1
s=input("Enter a sentence:").lower()
n={}
words=s.split()
for word in words:
    if word in n:
        n[word]=n[word]+1
    else:
        n[word]=1
print("Frequency of words:",n)

#Q2
y = int(input("Enter a year: "))
if (y % 4 == 0):
    ly = True
else:
    ly = False

m = int(input("Enter a month [1-12] "))
if m in (1, 3, 5, 7, 8, 10, 12):
    mlen = 31
elif m == 2:
    if ly:
        mlen = 29
    else:
        mlen = 28
else:
    mlen = 30

d = int(input("Enter a day: "))
if d < mlen:
    d=d+1
else:
    d = 1
    if m == 12:
        m = 1
        y=y+1
    else:
        m=m+ 1
print("Next date is %d/%d/%d." % (d, m, y))
      
#Q3
list=[3,9,10]
result=[(x,x**2) for x in list]
print(result)

#Q4
gp= int(input("Enter Grade Points: "))
g = ""
s = ""
if gp == 10:
	g = "A+"
	s="Outstanding"
elif gp == 9:
	g = "A"
	s="Excellent"
elif gp == 8:
	g = "B+"
	s="Very Good"
elif gp == 7:
	g = "B"
	s="Good"
elif gp == 6:
	g = "C+"
	s="Average"
elif gp == 5:
	g = "C"
	s="Below Average"
elif gp == 4:
	g = "D"
	s="Poor"
else:
	g ="Error"
print("Your Grade is %s and %s" % (g, s))

#Q5
for i in range(6):
    for j in range(i):
        print(' ', end='')
    for j in range(2*(6-i)-1):
        print(chr(65 + j), end='')
    print()

#Q6
d=dict()
while True:
        n=input("Enter the Name of the student:")
        sid=int(input("Enter the SID:"))
        d[sid]=n
        c=input("To stop adding enter 'N' and to add more enter just press press enter:")
        if c=='N':
                break
print("Entered data: ", d)

svalues=sorted(d.values())
skeys=sorted(d.keys())
d1 = {}
for i in svalues:
    for j in d.keys():
        if d[j] == i:
            d1[j] = d[j]
            break

print("Sorting using names:",d1)

d2 = {}
for k in skeys:
    for m in d.values():
        if m == d[k]:
            d2[k]=d[k]
            break

print("Sorting using SID:",d2)

search=int(input("Enter the SID to search the detaill of the Student:"))
name=d[search]
print("SID: %d Name: %s" %(search, name))

#Q7
n=int(input("Enter the range:"))
s=2
a=1
b=1
if n==1:
        print('a')
elif n==2:
        print('a','b')
else:
        print("Fibonacci series: ", end=' ')
        print(a,b,end=' ')
        for i in range(n-2):
            c = a + b
            b=a
            a=c
            print(c,end=' ')
            s=s+c
        print()
print("Average of fibonacci series:",s/n)                      

#Q8
set1={1,2,3,4,5}
set2={2,4,6,8}
set3={1,5,9,13,17}

u1=set1.union(set2)
u2=u1.union(set3)


i12=set1.intersection(set2)
i23=set2.intersection(set3)
i13=set1.intersection(set3)
i123=i12.intersection(set3)

#a
set_a=set1.symmetric_difference(set2)
print("A new set of all elements that are in Set1 and Set2 but not both:")
print(set_a)

#b
set_b=u2-i12-i23-i13
print("A new set of all elements that are in only one of the three sets Set1, Set2 and Set3:")
print(set_b)

#c
c1=i12.union(i23)
c2=c1.union(i13)
set_c=c2-i123
print("A new set of elements that are exactly two of the sets Set1, Set2 and Set3:")
print(set_c)

#d
n={1,2,3,4,5,6,7,8,9,10}
set_d=n-set1
print("A new set of all integers in the range 1 to 10 that are not in Set1:")
print(set_d)

#e
set_e=n-u2
print("A new set of all integers in the range 1 to 10 that are not in Set1, Set2 and Set3:")
print(set_e)
     