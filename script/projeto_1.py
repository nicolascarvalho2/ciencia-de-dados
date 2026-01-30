#importanto bibliotecas e base de dados
import pandas as pd
from pathlib import Path

# caminho da pasta onde está este arquivo .py
BASE_DIR = Path(__file__).resolve().parent

# sobe uma pasta e acessa o Excel
caminho_excel = BASE_DIR.parent / "Vendas+-+Base+de+Dados.xlsx"

tabela_vendas = pd.read_excel(caminho_excel)

# print(tabela_vendas.head())

#Calculando produto mais vendido (quantidade)

tabela_qtd_prod = tabela_vendas.groupby('Produto').sum()
tabela_qtd_prod = tabela_qtd_prod[['Quantidade']]
tabela_qtd_prod = tabela_qtd_prod.sort_values(by='Quantidade', ascending=False)

# print(tabela_qtd_prod)

#calcular produto mais vendido (faturamento)

tabela_vendas['Faturamento'] = tabela_vendas['Quantidade'] * tabela_vendas['Valor Unitário']
tab_faturamento_prod = tabela_vendas.groupby('Produto').sum()
tab_faturamento_prod = tab_faturamento_prod[['Faturamento']].sort_values(by='Faturamento', ascending=False)

# print(tab_faturamento_prod)

#Calculando a loja/estado que mais vendeu
tb_faturamento_loja = tabela_vendas.groupby('Loja').sum()
tb_faturamento_loja = tb_faturamento_loja[['Faturamento']]
tb_faturamento_loja = tb_faturamento_loja.sort_values(by='Faturamento', ascending=False)

# print(tb_faturamento_loja)

#Calculando ticket medio por loja/estado

tabela_vendas['Ticket Médio'] = tabela_vendas['Valor Unitário']
tb_ticket_medio = tabela_vendas.groupby('Loja').mean(numeric_only=True)
tb_ticket_medio = tb_ticket_medio[['Ticket Médio']].sort_values(by='Ticket Médio', ascending=False)
# print(tb_ticket_medio)

#Construindo um dashboard usando plotly

import plotly.express as px


grafico = px.bar(tb_faturamento_loja, y='Faturamento', x=tb_faturamento_loja.index)
grafico.show()