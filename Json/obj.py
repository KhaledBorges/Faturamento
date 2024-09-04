# Importante: no meu sistema somente está funcionando quando executado pelo terminal
# Preferi deixar este aviso do que fazer import do OS, pois uso linux e os códigos que eu usar talvez não funcionem para outros

import json

with open('dados.json', 'r') as f:
    dados = json.load(f)

faturamentos = [dia['valor'] for dia in dados if dia['valor'] > 0]

if len(faturamentos) == 0:
    print("Não há faturamento disponível para o cálculo.")
else:

    menor_faturamento = min(faturamentos)
    maior_faturamento = max(faturamentos)


    media_faturamento = sum(faturamentos) / len(faturamentos)


    dias_acima_da_media = sum(1 for faturamento in faturamentos if faturamento > media_faturamento)


    print(f"Menor faturamento: {menor_faturamento:.2f}")
    print(f"Maior faturamento: {maior_faturamento:.2f}")
    print(f"Dias com faturamento acima da média: {dias_acima_da_media}")
