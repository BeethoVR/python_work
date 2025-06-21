print("Hello, World!")
print('data')

a = [1,2,34,5]
print(a)

b = int(input('Edad :'))
print(b)

c = b * 2
print(c)

d = "String %d - int , %3.4f - float , %s - string" % (9, 7.98235, 'cadena str')
#print(d)

d = "String {:d} - int , {:3.4f} - float , {:s} - string".format (9, 7.98235, 'cadena str')
#print(d)

myName = input("Please enter your name :\n")
myAge  = input("Hi {}, what about your age:\n".format(myName))

print(myAge)
