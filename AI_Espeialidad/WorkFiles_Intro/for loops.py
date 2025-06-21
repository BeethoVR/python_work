Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
for i in range(9):
    print(i)

    
0
1
2
3
4
5
6
7
8
for i in range(0, 9):
    print(i)

    
0
1
2
3
4
5
6
7
8
for i in range(0, 9, 3):
    print(i)

    
0
3
6
animals = ["Lion", "Elephant", "Cat", "Dog"]
for animal in animals:
    print(animal)

    
Lion
Elephant
Cat
Dog
for i in "Elephant":
    print(i)

    
E
l
e
p
h
a
n
t
>>> animals = ("Lion", "Elephant", "Cat", "Dog")
>>> for animal in animals:
...     print(animal)
...     if animal == "Cat":
...         break
... 
...     
Lion
Elephant
Cat
>>> animals = ("Lion", "Elephant", "Cat", "Dog")
>>> for animal in animals:
...     if animal == "Cat":
...         continue
...     print(animal)
... 
...     
Lion
Elephant
Dog
