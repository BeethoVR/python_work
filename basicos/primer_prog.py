def creaFrase(Frase):
    interrogaciones = ('Qué','Porque','Dónde', 'Cómo', 'Que','Porque','Donde', 'Como')
    FraseCap = Frase.capitalize() 
    if (FraseCap.startswith(interrogaciones)):
        FraseResultado = "{}?".format(FraseCap)
    else:
        FraseResultado = "{}.".format(FraseCap)   
    return FraseResultado 


Frases  = []
while (True):
    Frase = input('Frase?')
    if (len(Frase) == 0):
        continue
    elif (Frase == '\end'):
        break
    
    Frase = creaFrase(Frase)
    Frases.append(Frase)

#sFrases = ''
#for Frase in Frases:
#    sFrases += Frase

print(' '.join(Frases))    

