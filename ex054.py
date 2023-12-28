print('\033[31mCondições de pagamento\033')
print('\033[30m-\033'*40)
preco = float(input('\033[32mDigite o valor do produto:\033 '))
cond = int(input('''\033[32mSelecione a opção de pagamento:
DIGITE 1 : Pagamento em dinheiro ou cheque (recebe 10% de desconto no valor total).
DIGITE 2 : Pagamento a vista no Cartão de Debíto ou Crédito (recebe 5% de desconto no valor total).
DIGITE 3 : Pagamento em 2X no Cartão de Crédito (mesmo valor)
DIGITE 4 : Pagamento em 3X ou mais no Cartão de Crédito (adição de 20% no valor total) 
OPÇÃO : \033'''))
print('\033[30m-\033'*40)
con1 = preco - preco * 10 / 100
con2 = preco - preco * 5 / 100
con3 = preco / 2
con4 = preco * 20 / 100 + preco
if cond == 1:
    print('''\033[30mO valor da compra é de :\033 \033[31mR${:.2f}\033
\033[30mE o valor a ser pago será de :\033 \033[31mR${:.2f}\033
\033[30mPagamentos a vista ou em cheque recebem 10% de desconto\033 '''.format(preco, con1))
elif cond == 2:
    print('''\033[30mO valor da compra é de :\033 \033[31mR${:.2f}\033
\033[30mE o valor a ser pago será :\033 \033[31mR${:.2f}\033
\033[30mPagamentos a vista no cartão de debíto ou crédito recebem 5% de desconto\033'''.format(preco, con2))
elif cond == 3:
    print('''\033[30mO valor total da compra é :\033 \033[31mR${:.2f}\033
\033[30mE o valor de cada parcela será de :\033 \033[31mR${:.2f}\033 '''.format(preco, con3))
elif cond == 4:
    parcela = int(input('\033[30mDigite em quantas vezes você deseja pagar\033: '))
    if parcela < 3:
        print('''\033[30mO valor total da compra é : R${:.2f}
E o valor de cada parcela será de :\033 R${:.2f} '''.format(preco, con3))
    else:
        total = con4 / parcela
        print('''O valor da compra é de :\033[30m R${:.2f}
E o valor a ser pago será de :\033 R$ {:.2f}
\033[30mEm {} parcelas de:\033 R${:.2f}
\033[30mPagamentos em 3x ou mais possuem juros de 20%.\033'''.format(preco, con4, parcela, total))
else:
    print('\033[31mOpção inexistente.\033')
