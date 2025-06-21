
#%%
import numpy as np

a1 = np.random.rand(4)
a2 = np.random.rand(4, 1)
a3 = np.array([[1, 2, 3, 4]])
a4 = np.arange(1, 4, 1)
a5 = np.linspace(1 ,4, 4)

print(a4.ndim)
print(a1)
print(a2)
print(a3)
print(a4)
print(a5)
# %%
import numpy as np

old = np.array([[1, 1, 1], [1, 1, 1]])
new = old
new[0, :2] = 0

print(old)
# %%
import re 
s = 'ACBCAC'
#Para la cadena dada, 
# ¿cuál de las siguientes expresiones 
# regulares puede utilizarse para comprobar si la cadena empieza por "AC"?

print('1')
re.findall('[^A]C', s)
print('2')
re.findall('^AC', s)
print('3')
re.findall('AC', s)
print('4')
re.findall('^[AC]', s)
# %%
import re
s = 'ACAABAACAAAB'
result = re.findall('A{1,2}', s)
L = len(result)
print(L)
# %%
import re 

t = """
Office of Research Administration: (734) 647-6333 | 4325 North Quad
Office of Budget and Financial Administration: (734) 647-8044 | 309 Maynard, Suite 205
Health Informatics Program: (734) 763-2285 | 333 Maynard, Suite 500
Office of the Dean: (734) 647-3576 | 4322 North Quad
UMSI Engagement Center: (734) 763-1251 | 777 North University
Faculty Adminstrative Support Staff: (734) 764-9376 | 4322 North Quad
"""

r1 = re.findall('\d{3}[-]\d{4}', t)
print(r1)
r2 = re.findall('\d{3}[-]\d{3}[-]\d{4}', t)
print(r2)
r3 = re.findall('[(]\d{3}[)]\s\d{3}[-]\d{4}', t)
print(r3)
r4 = re.findall('[(]\d{3}[)]\d{3}[-]\d{4})', t)
print(r4)

# %%
import re

t = 'I refer to https://google.com and I never refer http://www.baidu.com if I have to search anything'

r1 = re.findall('(?<=https://)([.]*)', t)
print(r1)

r2 = re.findall('(?<=https://)([A-Za-z0-9]*)', t)
print(r2)

r3 = re.findall('(?<=[https]://)([A-Za-z0-9.]*)', t)
print(r3)

r4 = re.findall('(?<=https://)([A-Za-z0-9.]*)', t)
print(r4)

# %%
import re

text=r'''Everyone has the following fundamental freedoms:
    (a) freedom of conscience and religion;
    (b) freedom of thought, belief, opinion and expression, including freedom of the press and other media of communication;
    (c) freedom of peaceful assembly; and
    (d) freedom of association.'''

import re
#pattern = '\(.\) '
pattern = 'freedom'
print(len(re.findall(pattern,text)))
# %%
