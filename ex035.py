print('Quantas letras "A" possui na frase')
frase = (str(input('Digite uma frase:')))
print('A frase possui: ', (frase.upper().count('A'), 'letras.'))
print('Ela aparece pela primeira vez na posição: ', (frase.upper().index('A')))
print('Ela aparece pela ultima vez na posição:  ', (frase.upper().rfind('A')))
print(frase)