# -*- coding: utf-8 -*-
"""
Created on Wed Jan  7 18:04:55 2026

@author: User
"""

#Q1(which variable names are invalid in python )
#Answer - 1_variable, variable#

#Q2(which operator have lower precedence than "not" in python)
#Answer - and

#Q3
a=10
b=5
print(a**b % 3)
#Answer - 1

#Q4
greetings='Namaste'
greetings_1=float(greetings)
print(type(greetings_1))
#Answer - code will throw error

#Q5
j=6
g=3.3
normal_division=j/g
print(type(normal_division))
floor_division=j//g 
print(type(floor_division))
#Answer - float,float

#Q6
a="10"
b=float(a)+5
result=str(b)+"123"
print(type(result))
#Answer - <class 'str'>

#Q7
a=15
b=3
c=4
result=a+b*c//(c%b)-5
print(result)
#Answer - 22


#Q8
a=4
b=5
a*=b*2
print(a)
#Answer - 40

#Q9
a=3
b=5
c=(a==3) and (b==5) or (a!=3)
print(c)
#Answer - True

#Q10
a=5
b=3
print(a&b)
#Answer - 1