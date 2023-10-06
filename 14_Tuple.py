#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<TUPLE>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
'''
Used to store multiple items in avariable

Tuple can be 
tuple= (1,2,3)  #one type of data
tuple= (False, True)
tuple = ("Kay", "Shay", "Riya", "Manoj")
tuple = (False, "Shay", 1, )  #Multiple data type
'''

#creating a tuple====================================>

colours = ("red", "yellow", "green", "blue")

#creating a tuple with 1 item -- always give comma for one item

# fruit = ("apple",)
# Or===========================================>
# fruit = tuple("apple")

# Check type of tuple
print(type(colours))

#Check the Length of tuple=============================================>

# print(len(colours));


#Accessing items in tuple==========================================>

# print(colours[1])  #Positive indexing

# print(colours[-1])  #Negative indexing

# print(colours[1:3]) # range indexing

# print(colours[-3:]) # range negative indexing


#Check if an item exist in tuple===================================>

# if "green" in colours:
#     print("Green is part of tuple")
# if "orange" not in colours:
#     print("Orange is not part of tuple")


#Travers the tuple =======================================>

# for i in colours:
#     print(i)


#Concatenate 2 tuples=====================================>

# more_colours = ("blue","orange")
# colours = colours + more_colours
# print(colours)


#Unpacking a Tuple=========================================>

colour1, colour2, colour3,colour4 = colours  # always use variables equlas to items in a tuple
print(colour1,colour2,colour3,colour4)


#Tuple VS List============================================================>

#Iterating through a "tuple" is faster than in a "list"
#"List" are mutable whereas "tuples" are immutable.
#Tuples that contain immutable elements can be used as a key for a dictionary.

#Reverse a Tupel ===========================================================>

tuple1 = ("z", "a", "d","f", "g", "e", "e", "k")
list = []
for x in reversed(tuple1):
    list.append(x)
output_tuple = tuple(list) #type cast in
print(output_tuple)