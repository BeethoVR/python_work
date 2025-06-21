quiz_questions = [ ("What is the capital of France?", ["Berlin", "Paris", "Madrid", "Rome"], 2), 
                   ("Which planet is known as the Red Planet?", ["Earth", "Venus", "Mars", "Jupiter"], 3),
                   ("What is the chemical symbol for water?", ["H2O", "O2", "CO2", "H2"], 1), ]
                
resp = 0
ej = input('algo?')
print(ej)

for q in quiz_questions:
    print(q[0])

    Ind = 1
    for opc in q[1]:
        print(f'%d ) %s' % ( Ind, opc))
        Ind += 1

    r = int(input('respuesta: '))
    #print(f'respuesta correcta: %d, repondio %d' % ( q[2], r))
    if (r == q[2]):
        print('Correcto')
        resp += 1
    else:
        print('Incorrecto')

print("Calificación: {} de 3".format(resp))