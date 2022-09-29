peso_atual = int(input("Insira o peso atual do paciente: "))
liquidos = int(input("Insira os líquidos que o paciente ingeriu nas últimas 24h: "))
peso_seco = peso_atual-liquidos
diferenca = peso_atual - peso_seco

if diferenca >= 1 and diferenca < 2:
    print(f"A diferença entre os dois pesos é de {diferenca} e o tempo da hemodiálise será de 2h")
elif diferenca >=2 and diferenca <3:
    print(f"A diferença entre os dois pesos é de {diferenca} e o tempo da hemodiálise será de 3h")
else:
    print(f"A diferença entre os dois pesos é de {diferenca} e o tempo da hemodiálise será de 4h")