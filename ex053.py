frase = str(input('Digite a frase: ')).strip().upper()
frase = "".join(frase.split())
fraseInvertida = frase[::-1]
if frase == fraseInvertida:
    print("{} é um palíndromo.".format(frase))
else:
    print("{} NÃO é um palíndromo.".format(frase))
