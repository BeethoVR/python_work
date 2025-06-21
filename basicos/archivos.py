f = open('./basicos/fruits.txt', 'r') # o f = open('fruits.txt') el default es 'r' de solo lectura
print(f.read())
print("\n")
f.seek(0)
for l in f:
    print(l)

f.close()    

with open('./basicos/fruits.txt') as f:
    print(f.read())
print('''Listo, no hay necesidad de cerrar el archivo, 
         se cierra en automático''')    

with open('./basicos/vegetales.txt', 'w') as f:
    f.write('tomate\n')
    f.write('cebolla\n')
    f.writelines(['ajo\n', 'perejil\n'])

with open('./basicos/vegetales.txt', 'a+') as f: # o 'a+' para append y read
    f.write('apio\n')

