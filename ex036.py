#entrada
valorCasa = float(input('Valor da casa: '))
salario = float(input('Salário: '))
anos = int(input('Em quantos anos vai pagar: '))

#processamento
qtdMeses = anos * 12
prestacao = valorCasa / qtdMeses
sal30porCento = salario * 0.30
if prestacao > sal30porCento:
    saida = 'Prestação mensal é de R${:.2f} excedendo 30% do salário (R${:.2f}). Empréstimo \033[31mNEGADO\033[m.'.format(prestacao, sal30porCento)
else:
    saida = 'Prestação mensal é de R${:.2f}. (30% do salário R${:.2f}). Empréstimo \033[32mACEITO\033[m.'.format(prestacao, sal30porCento)

#saída
print(saida)



