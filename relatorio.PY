coletas = []
num_coletas = 3
cv_meta=10
nomes_pins = [
    "Leads Meta",
    "Leads Real",
    "Dif",
    "N° de Matrículas",
    "% de Conversão Meta",
    "% de Conversão Real",
    "Diferença de % de Conversão",
    "Investimento Gastos",
    "R$ Em Matrículas",
    "Retorno"
]
Coletas_nomes=[
     "MGB",
     "Itaúna",
     "Horto",
]
leads_uni_meta= [300, 100, 100]
for i in range(num_coletas):
    print(f"{Coletas_nomes[i]}:")
    valores = []
    for c in range(10):
            pin=c
            if pin in [0]:
               valores.append(leads_uni_meta[i])
            elif pin in [2, 4, 6, 9, 0]:
                 valores.append(0)
            else:
                entrada= float(input(f"{nomes_pins[c]}: "))
                valores.append(entrada)
    leads_meta=valores[0]
    leads_real = valores[1]
    dif = leads_real - leads_meta
    cv_real = valores[5]  # % de Conversão Real
    dif_cv = cv_real - cv_meta
    invest_uni = valores[7]  # Investimento Gastos
    gastos_uni = valores[8]  # R$ Em Matrículas
    retorno_uni = gastos_uni - invest_uni



    valores[1] = (f"{leads_real:.0f}")
    valores[0] = leads_meta
    if dif>0:
        valores[2] = (f"+ {dif:.0f}")
    else:
        valores[2] = dif
    valores[4] = (f"{cv_meta}%")
    valores[5] = (f"{cv_real:.1f}%")
    valores[6] = (f"{dif_cv:.1f}%")
    valores[9] = (f"{retorno_uni:.2f}")  # Atualiza o retorno
    coletas.append(valores)



for i in range(num_coletas):
    print(f"\n{Coletas_nomes[i]}: ")
    for pin in range(10):
        print(f"{nomes_pins[pin]}: {coletas[i][pin]}")
print("\nVALOR GERAL DE INVESTIMENTOS E RETORNO")


matriculados=sum(coleta[3] for coleta in coletas)

captados=float(input("leads captados: "))
faltantes=(captados - matriculados)
captados_pctg=100
matriculados_pctg= (matriculados/captados*100)
faltantes_pctg= (100-matriculados_pctg)
eficiência_cv=(matriculados_pctg-cv_meta)



pin=7

soma_investimentos = sum(coleta[pin] for coleta in coletas)
print(f"Investimento R$: {soma_investimentos:.2f}")

pin=8

soma_matrículas = sum(coleta[pin] for coleta in coletas)
print(f"VALOR EM MATRÍCULAS R$: {soma_matrículas:.2f}")

pin=9

diferença_retorno= (soma_matrículas - soma_investimentos)
print(f"RETORNO R$: {diferença_retorno:.2f}")

print("RELATÓRIO DE EFICIÊNCIA DO TP:")
print(f"Leads captados: {captados:.0f}|{captados_pctg:.0f}%")
print(f"Leads matrículados: {matriculados}|{matriculados_pctg:.1f}%")
print(f"Leads a matricular: {faltantes}|{faltantes_pctg:.1f}%")
print(f"Meta de conversão: {cv_meta}%")
print(f"Real conversão: {matriculados_pctg:.1f}%")
if eficiência_cv == 0.00:
     print(f"Eficiência de conversão: META BATIDA!")
elif eficiência_cv > 0:
    print(f"Eficiência de conversão: +{eficiência_cv:.1f}%")
else:
    print(f"Eficiência de conversão: {eficiência_cv:.1f}%")

