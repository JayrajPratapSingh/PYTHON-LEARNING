''' 
variables and their declarations

variables in programming like containers that is used to stores some data 
container means some memory space in my computer

so for storing data we use variables

so in memomry at any particuler address this will create a space to store data like we have to store 10

x=10

x is variable and 10 is data 

now if i will change 

x=5 
then it will update 5 at same space instead of 10

now 

y= 10 

 it will create any other space in our computer's memory 

 


'''


# DATA TYPES

'''

Data can be different types like integer, number, string, boolian

z="Jhon"  // this is string

a=5.3  // float data type

b= false/true  // boolian

c = None  // null value


Interesting fact is that in python variable do not need to declare with any type int, float, bool, str e.t.c 


This is dinamacally typed

make sure to give a proper name to a variable
'''


#Variable Declaration

'''
A variable name must start with letter underscore character

A variable name cannot start with a number

A variable name can only contain alphanumetic charectors and underscore (A-z, 0-9, and_)

Variable name case senstive (count, Count and COUNT are three different variables)

Avariable name can not be any of the Pyhon keyword.

the keywords in python we do not use to write variabes name which is given below

False, 
True,
None,
and
as 
assert
break
calss 
continue
def
del 
elif 
else
except
finally
for
from 
global
if
import
in
is
lambda
nonlocal
not
or
pass
raise
return
try
while
with
yield

'''

#String

name = "Jayraj"

#integer

rollNumber = 23

# float
percentage = 95.0

#bollean

isPass = True

print(name, rollNumber, percentage, isPass)

# Print with string remember + only concatinate trings so we have to convert in string like given below

print("My name is = " + name + ",\nMy Roll Number is = " + str(rollNumber) + ",\nMy Percentage is = " + str(percentage) + ",\nAm i Passed the exam = " + str(isPass))

#OR

print("My name is = ", name, ",\nMy Roll Number is = ", rollNumber, ",\nMy Percentage is = ", percentage, ",\nAm i Passed the exam = ",  isPass)


# How to Know Type of varible data

print(type(name))
print(type(rollNumber))
print(type(percentage))
print(type(isPass))


#EXPRESSIONS


print("My Percentage has changed to = ", percentage-1)

#Print with seperator

print(name, rollNumber, percentage, isPass, sep="_")

x=1
y=1
z=3
print(x,y,z,sep="->")



