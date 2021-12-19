n = float(input('enter the number:'))
m = input('enter the action:')
import math
if m == 'radical':
    for i in range(1,n+1):
        if n//i == i:
           print(i)
if m == 'sin' :
    a = math.sin(n)
    print(a)
if m == 'cot' :
    a = 1 / (math.tan(n))
    print(a)
if m == 'cos' :
    a = math.cos(n)
    print(a)
if m == 'cot' :
    a = 1 / (math.tan(n))    
    print(a)
if m == 'tan' :
    a = math.tan(n)
    print(a)
if m == 'factorial':
    a = math.factorial(n)
    print(a)