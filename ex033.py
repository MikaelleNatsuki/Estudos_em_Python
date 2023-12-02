import re
print("Localizando uma palavra no texto")
print('metodo de localização de palavras')
nome = (str(input('Digite o seu nome: ')))
print('Nome:',nome)
if re.search('Silva', nome, re.IGNORECASE):
    print("Seu nome tem o nome Silva")
else:
    print("Seu nome não tem o nome Silva")


