#<--------------------------------LOOPS------------------------------------------>
'''
We use loops for repeted task
There are two types of loop in pyhon 
A. For
b. while

<-----------------------For----------------->

for i in range( startpoint,stoppoint,steps)  //if termination conditon meet hoga to loop chalna band ho jayega nahi to task chlta rahega
#code


# <-----------------------------------WHILE LOOP------------------------------------>
i=0
while i<10
#code
i+=1
'''


#<------------------------------------For Loop------------------------------------->

for i in range(1,11):
    print(i,"Hello World")

for i in range(11, 0, -1):
    print(i, "Ohh!")

for i in range(1,11,2):
    print(i,"OMG")

#no matter where you start but print 10 times
for _ in range(10):
    print("Bhakk Budbak")


#<------------------------Print element of a list using for loop---------------------->


list = [10,20,38,4,5,6,7,8,9,0]
fruits = ["Mango", "Guavava","Apple","Lemon"]

for i in list:
    print(i)

for i in fruits:
    print(i)




# <-----------------------------------WHILE LOOP------------------------------------>
# for loop me hame number of ittretion ka idea hona chahiye but While loop me jroori nahi hai we use condition to execute the code
# 1
i=2

while i<=100:
 print(i)
 i+=2

#2
j=0

while j <= 10:
 print(j)
 j +=1

#3

x=4 
y=0
while x>=0:
   x-=1
   y+=1

   if x==y:
      continue
   #continue means from here ecape the other part but again next process will start
   else:
      print(x,y)


#<--------------------------FOR PATTERN QUESTIONS SOLUTION------------------------------------>

'''
Find 3 things for patterns ques
rows
colums
what to print
-------------------> row
^
|
|
|
|
column


'''

#Ques Row fixd n=5 print if 1 then one time 2 then 2 time three then 3 time like this


n = int(input("Enter the number:"))

for _ in range (n):
   print("*" * 7)




#Ques Row  n print if 1 then one time 2 12 then 2 time three then 3 time 123 like this

n2 = int(input("Enter the number:"))

for j in range (n2):
   for i in range(1,n2+1):
      print(i,end="")
   print()


   #Ques Row  n print if 1 then one time 2 1 then 12 2time three then 3 time 1 then 12 then 123 like this


n3 = int(input("Enter the number:"))

for j in range (1,n3+1):
   for i in range(1,j+1):
      print(i,end="")
   print()


#Ques: Print

#    1
#   123
#  12345
# 1234567
n4 = int(input("Enter the number:"))

for i in range (1, n4+1): #Loop for rows
   #print spaces
   print(" "* (n4-i), end="")
   #print digits
   for j in range(1, 2 * i):
      print(j, end="")
   print()

   

