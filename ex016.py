print ('Novo Salário do funcionario')
sal = float(input('Digite o salário atual do funcionario: '))
ajus = (sal*15/100)
nsal = sal + ajus
print ('O Salario atual do funcionario é de: R${:.2f} \n O novo salario com reajuste é: R${:.2f} '.format(sal,nsal))