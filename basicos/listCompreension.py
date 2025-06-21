Temps = [123, 234, 345, 456, -999]

# Ejemplo 1
lC = [(t / 10) for t in Temps]
print(lC)

# Ejemplo 2
lC = [(t / 10) for t in Temps if (t > 0) ]
print(lC)

# Ejemplo 3
def getNumbers(listValues):
    return([v if (type(v) == int) else 0 for v in listValues])
    
data =    [99, 'no data', 95, 94, 'no data']

print(data)
print(getNumbers(data))

#Ejemplo 4
def sumNumbers(listNumbers):
    #listNumbers = [float(n) for n in listNumbers]  
    #return (sum(listNumbers))
    return(sum([float(n) for n in listNumbers]))

data = ['1.2', '2.6', '3.3']

print(sumNumbers(data))

# Ejemplo 5
#dictTemps = {'lun': 123, 'mar': 234, 'mier': 345}
#dictDiario = { key:value for key:value in dictTemps}