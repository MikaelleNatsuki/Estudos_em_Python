print('-----Classificando atletas-----')
nome = str(input('Olá atleta!, qual o seu nome?: ')).capitalize()
idade = int(input('Diga a sua idade: '))
if idade <= 9:
    print('''{} sua idade é de: {}
 E a sua categoria é : \033[32mMIRIN\033 '''.format(nome, idade))
elif idade <= 14:
    print('''{} sua idade é de: {}
E a sua categoria é : \033[34mINFANTIL\033'''.format(nome, idade))
elif idade <= 19:
    print('''{} sua idade é de: {}
E sua categoria é : \033[33mJUNIOR\033'''.format(nome, idade))
elif idade <= 25:
    print('''{} sua idade é de: {}
E sua categoria é : \033[35mSÊNIOR\033'''.format(nome, idade))
elif idade >= 25:
    print('''{} sua idade é de : {}
E sua categoria é : \033[31mMASTER\033'''.format(nome, idade))
