frase = 'Curso em Vídeo Python'
print (frase[3]) #mostra a 4° letra
print (frase[3:13]) #mostra da 4° a 12° letra
print (frase[:14]) #mostra do inicio até a 13° letra
print (frase[13:]) #mostra do 13° até o final
print (frase[1:15])#mostra a 2° letra até a 14° letra
print (frase[1:15:2]) #mostra da 2° letra até a 14° letra pulando de 2 em 2
print (frase[1::2]) #mostra da 2° letra até o fim pulando de 2 em 2
print (frase[::2]) #mostra a string inteira pulando de 2 em 2
print (frase.count('o')) #mostra quantas vezes tem a letra o (minuscula pois o python e case sensitive) na string
print (frase.upper().count('O')) #a função upper tranforma a letra selecionada pelo usuario (no caso o) em letras maiusculas,e o count localiza quantas letras o possui na string, sendo elas maiusculas ou minusculas
print (len(frase)) #conta quantas letras e espaços possui na frase
print (len(frase.strip())) #remove espaços inuteis, como o do começo e do final da string
print (frase.replace('Python','Android')) #substitui a palavra da string, porém ela e imutavel, ela so aparece no momento em que pedimos a substituição
# #caso queira realmente fazer a substituição, deve se fazer o seguinte:
# frase = frase.replace('Python','Android')
print ('Curso'in frase) #retorna True se possuir a palavra na string
print (frase.find('Curso')) #retorna aonde a string está localizada (aonde esta a primeira letra dela), se colocar algo que nao possui na frase ele retorna -1, sempre colocar do jeito que esta na string, pois o python e case sensitive
print (frase.lower().find('vídeo')) #Assim mesmo que a palavra esteja em maiusculo, ele ira retornar sua localização, pois o lower deixa tudo em minusculo
print (frase.split()) #ele fatia a frase da variavel, criando uma lista
dividido = frase.split() #cria uma variavel/objeto para a divisão de palavras
print(dividido[0]) #Exibe a primeira palavra da frase que se inicia por zero)
print (dividido [2] [3]) #Exibe a segunda string dividida e sua 4° letra


