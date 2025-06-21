Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
shirt_numbers = [7, 8, 10, 20, 30]
shirt_numbers
[7, 8, 10, 20, 30]
shirt_numbers = ["7", "8", "10", "20", "30"]
shirt_numbers
['7', '8', '10', '20', '30']
animals = ["Lion", "Cat", "Dog"]
animals
['Lion', 'Cat', 'Dog']
new_animals = [animals, "Horse", "Goat", "Tiger"]
new_animals
[['Lion', 'Cat', 'Dog'], 'Horse', 'Goat', 'Tiger']
new_animals[0]
['Lion', 'Cat', 'Dog']
>>> new_animals[1]
'Horse'
>>> animals[0]
'Lion'
>>> animals[1]
'Cat'
>>> animals[-1]
'Dog'
>>> animals[-2]
'Cat'
>>> new_animals.pop()
'Tiger'
>>> new_animals
[['Lion', 'Cat', 'Dog'], 'Horse', 'Goat']
>>> new_animals.append("Elephant")
>>> new_animals
[['Lion', 'Cat', 'Dog'], 'Horse', 'Goat', 'Elephant']
>>> new_animals.remove("Goat")
>>> new_animals
[['Lion', 'Cat', 'Dog'], 'Horse', 'Elephant']
>>> new_animals[0] = "Cow"
>>> new_animals
['Cow', 'Horse', 'Elephant']
>>> len(new_animals)
3
>>> new_animals.reverse()
>>> new_animals
['Elephant', 'Horse', 'Cow']
