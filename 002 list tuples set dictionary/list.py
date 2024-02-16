my_list=[1,2,3,4]
print(type(my_list))
# it can have multiple data types
my_list=[1,2,3,"Hello"]
# list are mutable
my_list.append("Bye")
print(my_list)
print(my_list[:4])
print(my_list[:5:2]) #step length 2
# List allow duplicate values
my_list.append(2)
print(my_list)

# len function
print(len(my_list))

# Empty list
list2=[]
print(list2)

# Delete an elemnt from a list
del my_list[2]
print(my_list)

# Join two list
list3=["Join",1,2]
print(my_list)
print(list3)
print((my_list+list3))