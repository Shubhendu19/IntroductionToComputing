#Q1
 
from tkinter import *
window = Tk() 
window.title("GST Rate Finder")  
window.geometry("300x300") 
def GST() :
    o= int(orignalField.get())
    n = int(netField.get())
    gr = ((n - o) * 100) / n;  
    grField.insert(10, str(gr) + " % ") 
    
def CA(): 
    orignalField.delete(0, END)    
    netField.delete(0, END)    
    grField.delete(0, END)
    
orignal = Label(window, text = "Original Price" )
orignal.grid(row = 1, column = 1,padx = 10,pady = 10)
orignalField = Entry(window)
orignalField.grid(row = 1, column = 2 ,padx = 10,pady = 10)

net = Label(window, text = "Net Price")
net.grid(row = 2, column = 1, padx = 10, pady = 10)
netField = Entry(window)
netField.grid(row = 2, column = 2, padx = 10,pady = 10)

result = Button(window, text = "Find", command = GST)
result.grid(row = 3, column = 2,padx = 10,pady = 10)

gr = Label(window, text = "Gst Rate")
gr.grid(row = 4, column = 1,padx = 10, pady = 10)
grField = Entry(window)
grField.grid(row = 4, column = 2, padx = 10,pady = 10)

clear = Button(window, text = "Clear", command = CA) 
clear.grid(row = 5, column = 2, padx = 10, pady = 10)

window.mainloop()

#Q2

from tkinter import *


import calendar
window = Tk()
window.geometry("250x140")
window.title("CALENDAR")

def Calender() :

	
	window1 = Tk()
	window1.title("CALENDAR")
	window1.geometry("550x600")
	y = int(yearField.get())
	c = calendar.calendar(y)
	yearLabel = Label(window1, text = c)
	yearLabel.grid(row = 5, column = 1, padx = 20)
	window1.mainloop()

	
year = Label(window, text = "Enter Year")
year.grid(row = 2, column = 1)
yearField = Entry(window)
yearField.grid(row = 3, column = 1)

Enter = Button(window, text = "Enter", command = Calender)
Enter.grid(row = 4, column = 1)

Exit = Button(window, text = "Exit", command = exit)
Exit.grid(row = 6, column = 1)

window.mainloop()
	
#Q3
from tkinter import *
window = Tk()
window.title("Calculator")
expression = ""
def Operation(num):
	global expression
	expression = expression + str(num)
	equation.set(expression)
	
def Equal():

	global expression
	total = str(eval(expression))
	equation.set(total)
	expression = ""
def CA():
	global expression
	expression = ""
	equation.set("")




equation = StringVar()

expressionField = Entry(window, textvariable=equation)

expressionField.grid(columnspan=4, ipadx=70)

button1 = Button(window, text=' 1 ',command=lambda: Operation(1), height=1, width=5)
button1.grid(row=2, column=0)

button2 = Button(window, text=' 2 ',command=lambda: Operation(2), height=1, width=5)
button2.grid(row=2, column=1)

button3 = Button(window, text=' 3 ',command=lambda: Operation(3), height=1, width=5)
button3.grid(row=2, column=2)

button4 = Button(window, text=' 4 ',command=lambda: Operation(4), height=1, width=5)
button4.grid(row=3, column=0)

button5 = Button(window, text=' 5 ',command=lambda: Operation(5), height=1, width=5)
button5.grid(row=3, column=1)

button6 = Button(window, text=' 6 ',command=lambda: Operation(6), height=1, width=5)
button6.grid(row=3, column=2)

button7 = Button(window, text=' 7 ',command=lambda: Operation(7), height=1, width=5)
button7.grid(row=4, column=0)

button8 = Button(window, text=' 8 ',command=lambda: Operation(8), height=1, width=5)
button8.grid(row=4, column=1)

button9 = Button(window, text=' 9 ',command=lambda: Operation(9), height=1, width=5)
button9.grid(row=4, column=2)

button0 = Button(window, text=' 0 ',command=lambda: Operation(0), height=1, width=5)
button0.grid(row=5, column=0)

plus = Button(window, text=' + ',command=lambda: Operation("+"), height=1, width=5)
plus.grid(row=2, column=3)

minus = Button(window, text=' - ',command=lambda: Operation("-"), height=1, width=5)
minus.grid(row=3, column=3)

multiply = Button(window, text=' * ',command=lambda: Operation("*"), height=1, width=5)
multiply.grid(row=4, column=3)

divide = Button(window, text=' / ', command=lambda: Operationpress("/"), height=1, width=5)
divide.grid(row=5, column=3)

equal = Button(window, text=' = ',command=Equal, height=1, width=5)
equal.grid(row=5, column=2)

clear = Button(window, text='Clear',command=CA, height=1, width=5)
clear.grid(row=5, column='1')

Decimal= Button(window, text='.',command=lambda: Operation('.'), height=1, width=5)
Decimal.grid(row=6, column=0)

window.mainloop()

#Q4
def mergeSort(List):
    if len(List) > 1:
        mid = len(List) // 2
        left = List[:mid]
        right = List[mid:]
        
        mergeSort(left)
        mergeSort(right)

        i = 0
        j = 0
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
              List[k] = left[i]
              i += 1
            else:
                List[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            List[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            List[k]=right[j]
            j += 1
            k += 1

List =[int(x) for x in input("Enter multiple value: ").split(",")]
print(List)
mergeSort(List)
print(List)

#Q5
def mergeSort(List):
    if len(List) > 1:
        mid = len(List) // 2
        left = List[:mid]
        right = List[mid:]
        
        mergeSort(left)
        mergeSort(right)

        i = 0
        j = 0
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
              List[k] = left[i]
              i += 1
            else:
                List[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            List[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            List[k]=right[j]
            j += 1
            k += 1



def binarySearch(List, x, low, high):
    while low <= high:

        mid = low + (high - low)//2

        if List[mid] == x:
            return mid

        elif List[mid] < x:
            low = mid + 1

        else:
            high = mid - 1

    return -1

def countOccurrences(List, n, x):
    res = 0
    for i in range(n):
        if x == List[i]:
            res += 1
    return res


#5a
List =[int(x) for x in input("Enter multiple value: ").split(",")]
print("List:",List)
mergeSort(List)
print("Sorted List:",List)

#5b
n=int(input("Enter the number to be searched:"))
result = binarySearch(List, n, 0, len(List)-1)
if result != 0:
    print("Element is present at index " + str(result))
else:
    print("Not found")

#5c
x=int(input("Enter the number whose occurence is needed:"))
print (f"Occurence of {x}:{countOccurrences(List, len(List), x)}")

  

