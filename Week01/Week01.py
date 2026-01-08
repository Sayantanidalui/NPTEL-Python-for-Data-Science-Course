# -*- coding: utf-8 -*-
"""
Created on Wed Jan  7 17:36:13 2026

@author: User
"""

#simple example
a=14
c=a*10
print(a,c)

#access basic libraries-sublibraries
import numpy
content=dir(numpy)
print(content)

#variables
Emp_name="Sayu"
age=20
height=150.6

#find data type
type(Emp_name)
type(age)
type(height)

#verify datatype
type(height) is int
type(Emp_name) is str

#convert data type
ht=int(height)
type(ht)
emp=float(Emp_name)
type(emp)

#Arithmetic operators
a=10
b=5 
print(a+b,a-b,a*b,a/b,a%b,a**b)

#Assignment operators
a=10
b=5 
a+=b
print(a)
a-=b
print(a)
a*=b
print(a)
a/=b
print(a)

#Relational operators
x=5 
y=7
print(x<y,x<=y,x>y,x>=y,x==y,x!=y)

#Logical operators
print((x>y) or (x<y))
print((x>y) and (x<y))
print(not(x==y))

#bitwise operators
x|y
x&y

#practice assignment Q5
x=300
y=17
x%=y
print(x)