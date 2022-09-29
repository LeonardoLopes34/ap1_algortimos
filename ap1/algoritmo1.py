faturamento = int(input("Insira o faturamento da sua empresa: "))
pis = faturamento/100*0.65
cofins = faturamento/100*3
custos = int(input("Insira os custos da empresa: "))
impostos = pis+cofins
custos2= custos+impostos
lucro = faturamento-custos2
round_pis = round(pis, 2)
round_cofins = round(cofins, 2)
round_lucro = round(lucro, 2)



print(f"O faturamento da sua empresa é de R$: {faturamento}")
print(f"O imposto PIS que sua empresa paga é de R$: {round_pis}")
print(f"O imposto COFINS que sua empresa paga é de R$: {round_cofins}")
print(f"O lucro da sua empresa é de R$: {round_lucro}")