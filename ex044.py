print('{:=^40}'.format(' LOJAS ALEXIS '))
preco = float(input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO')
print('''[ 1 ] à vista dinheiro/cheque 
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opc = int(input('Qual é a opção? '))

if opc == 1:
    precoFinal = preco - (preco * 0.10)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, precoFinal))
elif opc == 2:
    precoFinal = preco - (preco * 0.05)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, precoFinal))
elif opc == 3:
    parcela = preco / 2
    print('Sua compra será dividida em 2x de R${:.2f}.'.format(parcela))
elif opc == 4:
    parcelaQtd = int(input('Quantas parcelas? '))
    precoFinal = preco + (preco * 0.20)
    parcela = precoFinal / parcelaQtd
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS.'.format(parcelaQtd, parcela))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, precoFinal))
else:
    print('Opção inválida...')