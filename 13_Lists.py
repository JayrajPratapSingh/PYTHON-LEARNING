#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<LIST>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
'''
<----------------------------------List-------------------------------------->
LIST::
These allows us to store multiple items in a single variable.

fruit = ["apple", "bananas", "cherry"]
list = [1,2,3,4,5]
list1 = [True, False]
list2 = [True, 1, "apple"]

List Items:

Indexed
Ordered
Mutable
Duplicates allowed
any datatype
Mix of different data types

Acessing the list item 

fruit[2]

'''


fruit = ["apple", "Banana", "Mango", "Cherry"]

#Printing List
print(fruit)  #Prints all item in fruit list
#Printing Type of List
print(type(fruit)) # List

#Print Length of List

print(len(fruit))  #3

# Checking if an item is present in the list

if "Banana" in fruit:
    print("Banana is part of the list")
else:
    print("Banana is not present in the list");

#Accessing items of a list

listNum = [10, 30, 40, 50, 60]

print(listNum[3])
print(listNum[-3])

#Accessing item in range

print(listNum[1:3])  #starting means 1 is inclusive and last means 3 will be exclusive
print(listNum[-3:-1])

#Adding element to a list
#Append()  ===> adds items to the list in the end
#insert()  ===> adds items to a particuler index
#extend()  ===> adds list2 items in list one

#adding elements to a list in last


listNum.append(50)
print(listNum)

#adding elements to a list in given index or a specific index

listNum.insert(2, "mango")
print(listNum)

#adding two array items

listNum.extend(fruit)

print(listNum)


#Removing Element
#remove() ====> it removes item by given name of item or number
#pop()  ==> it removes item by given idex item else last item




listNum.remove(30)
print(listNum)

listNum.pop()
listNum.pop(1)
print(listNum)



#Changing item in List
#At an index
#in a range


listNum[1] = 60

listNum[5:7] = [40, 50]
listNum[5:7] = "papaya"  #it will convert into list 
print(listNum)


# SORTING A LIST
#Ascending Order
#Descending Order
#Bydefault Ascending 

list = [40, 50, 30, 56, 10, 58]
fruits = ["apple", "Mango", "papaya", "Orange", "Guavava"]
alphabate = ['n', 'c','b','a']
list.sort()

print(list)
list.sort(reverse=True) #Ascending Order
print(list)
alphabate.sort()


print(alphabate)
alphabate.sort(reverse=True) #descending Order
print(alphabate)

fruits.reverse()
print(fruits)


#List Comprehension==========================================>
#When we want to make a new list from items of an existing list
#Let say we want to spred some item in new list so we can use loop and if else so it gives easy way to do it

newList = [list for list in list if list > 30]
newFruits = [fruit for fruit in fruits if "M" in fruit]
print(newFruits)
newFruits = fruit + fruits
print(newFruits)
print(newList)


#Nested List====================================>
OhList = ["Oh", "are", "bakk", ["luck", "takatak"]]

print(OhList[3][1])


#Ques swap the index 
indexList1 = [23, 65, 19, 90]
i = indexList1[0]
indexList1[0] = indexList1[2]
indexList1[2] = i
print(indexList1)
indexList2 = [1,2,3,4,5]
i = indexList2[1]
indexList2[1] = indexList2[4]
indexList2[4] = i
print(indexList2)