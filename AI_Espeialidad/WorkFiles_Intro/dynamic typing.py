Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> number = 10
>>> number
10
>>> type(number)
<class 'int'>
>>> number = 10.35
>>> number
10.35
>>> type(number)
<class 'float'>
>>> number = "10"
>>> number
'10'
>>> type(number)
<class 'str'>
>>> print(number + 50)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print(number + 50)
TypeError: can only concatenate str (not "int") to str
