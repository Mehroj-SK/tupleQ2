# tuple1 = ("Mehroj")
# print(tuple1) 

# tuple1 = ("apple", "Orange", "pineapple")
# list1 = list(tuple1)
# list1.pop(2)
# tuple1 = tuple(list1)
# print(tuple1) 

# tuple1 = ("apple", "Orange", "pineapple")
# del tuple1
# print(tuple1)
#if we want ti delete the tuple and print it , it shows error as the tuple is not defined becuase it is deleted


# tuple1 = (1,2,3,[6,7],4,5)
# print(tuple1[3][0], tuple1[4])

# tuple1 = (1,2,3,[6,7],4,5)
# tuple1[3][0]=8
# print(tuple1) 



tuple1 = (10,20)
tuple2 = (30,40)
temp = tuple1
tuple1 = tuple2 
tuple2 = temp 
print(tuple1,tuple2) 