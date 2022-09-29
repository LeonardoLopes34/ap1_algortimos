cigarro = int(input("Insira quantos cigarros você fuma por dia: "))
meses = int(input("Insira quantos meses você fuma: "))
horas = (cigarro*15)/60
cigarro_mes = (cigarro*15)*30

if meses <3:
    print(f'Você fuma a {meses} meses e por isso você tem dentes amarelos e perdeu {horas} horas de vida ')
elif meses >= 3 and meses <=12:
    print(f'Você fuma a {meses} meses e por isso você tem perda de paladar, respiração comprometida e perdeu {horas} horas de vida')
else:
    print(f'Você fuma a {meses} meses e por isso você está com o pulmão comprometido e perdeu {horas} horas de vida')