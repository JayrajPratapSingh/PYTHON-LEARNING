#  <<<<<<<<<<<<<<<<<<<<<<<Conditionals And Loops>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#<----------------------------Control System-------------------------->
'''
They Allow us to control the flow of our programm

'''

#<--------------------------Conditional Statement------------------------>

'''
if, if-else
nested
Else ifladder
Ternary
switch

#<------------------------------IF ELSE---------------------------------->
if condition;
   Statement1!
else
   Statement2!


 <---------elif----------->


if condition;
   Statement1!
elif
   Statement2!
else
   Statement3!


  





'''

#<------------------------------IF ELSE---------------------------------->
#Ques1: Take integer input and tell if it is positive or negative

'''
number = int(input("Enter a number:"))
if number >=0:
    print("The number is Positive")
else:
    print("The number is negative")
7
'''


#Ques2: Take a integer input an tell if it is even or odd
# so we have taken input already

'''

if number%2 ==1:
    print("Number is odd")
else:
    print("Number is even")

'''


#Ques3: Teke cost price and selling price of an item and determine how much profit or loss incurred

'''

costPrice = float(input("Enter the cost Price:"))
sellingPrice = float(input("Enter the Selling Price:"))

PL = sellingPrice - costPrice

if PL==0:
    print("No profit No Loss")
elif PL > 0:
    print("Your Profit is:", PL)
else:
    print("Your Loss is:", PL)

'''


#Ques4 input percentage of a student and print the Grade according to marks:81-100=VeryGood, 61-80=Good,41-60= Average <=40 Fail

'''

PercentageOfStudent = float(input("Enter the percentage of the student:"))

if PercentageOfStudent >=80:
    print("Your Grade is: Very Good")
elif PercentageOfStudent >=60:
    print("Your Grade is: Good" )
elif PercentageOfStudent >=41:
    print("Your Grade is: Average" )
else:
    print("Your are Fail" )

'''

#<----------------------------MULTIPLE CONDITION USING "and" and "or"------------------------------>
#Ques5:  



# engMarks = int(input("Enter marks in english: "))
# mathMarks = int(input("Enter marks in Math: "))

# if engMarks>80 and mathMarks>80:
#     print("Your Grade is: A ")
# elif engMarks>80 or mathMarks >80:
#     print("Your Grade is: B")
# else:
#     print("Your Grade is: C")





#<----------------------------NESTED IF-ELSE------------------------------>

#Ques 6:  find greatst of three numbers using nested if else




# n1 = int(input("Enter the first Number:"))
# n2 = int(input("Enter the second Number:"))
# n3 = int(input("Enter the Third Number:"))

# if n1>n2:
#     if n1>n3:
#        print(n1, "is the greatest Number")
#     else:
#         print(n3, "is the greatest Number")
# else:
#     if(n2>n3):
#         print(n2, "is the greatest Number")
#     else:
#         print(n3, "is the greatest element")



    
#<----------------------------MATCH CASE (Python 3.10)------------------------------>
#Calculator using Match Statement


# num1 = int(input("Enter Number1:"))
# num2 = int(input("Enter Number2:"))

# operator = input("Enter Operator:")

# match operator:
#     case "+":
#         print("Sum is:", num1 + num2)
#     case "-":
#         print("Difference is:", num1-num2)
#     case "*":
#         print("Product is:", num1*num2)
#     case "/":
#         print("Division is:", num1/num2)
#     case "//":
#         print("Divison Roundoff is:", num1//num2)
#     case "%":
#         print("Remiender is:", num1%num2)
#     case "**":
#         print("num1 to the power num2 is:", num1**num2)
#     case _ :
#         print("Enter a valid operator")




#<----------------------------TERNARY OPERATOR------------------------------>

#Ques 7: Write a program to check if number is odd or even using ternary operator

num = int (input("Enter a number:"))

output = "Even" if num%2 ==0 else "Odd"

#we can use direct in print
print("Output is", output )


