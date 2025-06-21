from os import system

system('clear')
print("\n\n")

def fun(x):
    if x % 2 == 0:
        return 1
    else:
        return 0
 
 
print(fun(fun(2)) + 1)
#-------------------------- 
system('clear')
print("\n\n")

my_list = [x * x for x in range(5)]
 
def fun(lst):
    del lst[lst[2]]
    return lst

print(fun(my_list)) 
#-------------------------- 


my_list = [0,1,2,3,4,5,6,7,8,9,10]
print(my_list)

l1 = my_list[ -3 : -2 ]

print(l1)