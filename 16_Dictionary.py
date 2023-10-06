#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<DICTIONARY>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
'''
<-------------------------------------Dictionary-------------------------------------->

Dictionary stores key value pairs in a variable

What to remember

Ordered
Changeable
Unindexed
Duplicates not allowed
Any datatype

'''

#Creating a dictionary

numbers = {"Jayraj":8364503526, "Jaiom":9807642863, "Hariom":8318114175,"Ria":358094285}

#print dictionary

print(numbers)

#cheking type of dictionary

print(type(numbers))

#Length of dictionary

print(len(numbers))

#access items of items of dictionary

print(numbers["Jaiom"])
print(numbers.get("Jayraj"))

#print all of the keys of the dictionary 

print(numbers.keys())

#print all of the value of the dictionary

print(numbers.values())

#Update value in dictionary

numbers["Jayraj"] = 293842093

print(numbers)

#Add elements in dictionary

numbers["Kia"] = 249802734

print(numbers)

#Add another dictionary

more_numbers = {
    "Joy":987234987,
    "Luma":923475908

}

numbers.update(more_numbers)
print(numbers)


#Remove the elements from dictionary

numbers.pop("Jayraj")
print(numbers)

numbers.popitem()  # This will remove the last added item
print(numbers)

#Empty the dictionary=================================================>

# numbers.clear()
# print(numbers)


#Printing values and keys using loop

for x in numbers:
    print(x) # this will give all the keys 
    print(numbers[x]) # this will print all the values of the keys 

# Print both the item using loop 

for x in numbers.items():
    print(x)

#if we want to print both key and value saperated of a dictionary

for x,y in numbers.items():
    print(x,y)

#nested Dictionary

phones = {
    "Area1": {
        "x":0,
        "y":1,
        "z":2
    },
    "Area2": {
        "a":0,
        "b":1,
        "c":2
    }
}

print(phones["Area1"]["y"])


#Ques:==> Given a dictionary in python, write a python program to find the sum of all items in the dictionary
intput1= {
    "a":100,
    "b":200,
    "c":300
}

sum = 0

for x in intput1:
    sum = sum + intput1[x]
print(sum)


# OR
intput2= {
    "a":100,
    "b":200,
    "c":300,
}

# print("The sum of the dictionary values is :", sum(intput2.values()))

