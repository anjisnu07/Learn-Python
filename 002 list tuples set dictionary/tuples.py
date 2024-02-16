tuple_1=(1,2,3,4)
print(tuple_1)
print(type(tuple))
# It can store data of multiple data types
tuple_2=(1,2,3,"Hello",True)
print(tuple_2)

# List to tuple convert
my_list=[1,2,3,4]
print(my_list)
my_tuple=tuple(my_list)
print(my_tuple)

# Indexing
print(my_tuple[1])

# tuples are immutable,i.e cant change using append or any func

print(len(my_tuple))