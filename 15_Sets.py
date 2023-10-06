#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<SETS>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
'''
<--------------------------------Sets------------------------------------>
Sets:==> Container for storing multiple values in a variable 
 names = {"Jhon", "Marry", "Pal"}

 What to remember 
 
 Unordered => if we are printing something from sets so it may be in unordered
 Immutable => we can not update existing values but we can remove or add elements
 Unindexed 
 Duplicates not allowed 
 Any datatype
 Mix different data types

'''

#Creating a Set =======================================>

names = {'Sia', "Mia", "Kia", "chia"}
#print set
print(names)

#length of set
print(len(names))

#check data type of set

print(type(names))

#accessing items of set

for x in names:
    print(x)

#Check if an item exists in a set

if "Sia" in names:
    print("Sia is in the set")

#Add elements in sets
names.add("Ria")
names.add("Sia") # sia is already present so it will not duplicate it
print(names)

#add another sequence in a set
names_list = ["Lia", "Pia"]
names.update(names_list)
print(names)


#For removing elements from a set
names.remove("Sia")
print(names)

#You are removing a name which is not present in out set so use discartd() if you use remove() it will throw err

names.discard("bakk")
print(names)

# join two sets

s1 = {"a", "b", "c"}
s2 = {"d", "e", "a"}

# s3=s1.union(s2)
# print(s1,s2,s3)

# s1.update(s2)
# print(s1)

#Keep only duplicates while joining

# s1.intersection_update(s2)
# print(s1)

#Keep all value except duplicates

s1.symmetric_difference_update(s2)
print(s1) #except a all value will print

#Ques: Given three arrays, we have to find common elements in three sorted lists using sets.
l1 = [1,5,5]
l2 = [3,4,5,5,10]
l3 = [5,5,10,20]

# type casting into sets
s1 = set(l1)
s2 = set(l2)
s3 = set(l3)

#join using intersection

s1s2 = s1.intersection(s2)
final_set = s1s2.intersection(s3)


final_list = list(final_set)

print(final_list)