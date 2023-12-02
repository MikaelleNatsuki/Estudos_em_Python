print('Localizando a palavra santo')
cidade = (str(input('Digite o nome da sua Cidade: '))).strip().capitalize()
print(cidade)

if cidade.startswith('santo'.capitalize()):
    print('Sua cidade começa com SANTO!.')
else:
    print('Sua cidade não começa com SANTO.')
