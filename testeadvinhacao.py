velocidade = float(input("Qual foi a velocidade percorrida?"))
velocidadeMaxima = 80.0
multa = (velocidade-80) * 7

if velocidade > velocidadeMaxima:
    print("Você foi multado! Terá que pagar uma multa de {} reais".format(multa))
else:
    print("Ta deboas")