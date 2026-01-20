#importanto bibliotecas e base de dados
import pandas as pd

tabela_vendas = pd.read_excel("C:\\Users\\nicol\\Downloads\\Vendas+-+Base+de+Dados.xlsx")
print(tabela_vendas)

#Calculando produto mais vendido (quantidade)

tabela_qtd_prod = tabela_vendas.groupby('Produto').sum()
tabela_qtd_prod = tabela_qtd_prod[['Quantidade']]
tabela_qtd_prod = tabela_qtd_prod.sort_values(by='Quantidade', ascending=False)

print(tabela_qtd_prod)

#calcular produto mais vendido (faturamento)

tabela_vendas['Faturamento'] = tabela_vendas['Quantidade'] * tabela_vendas['Valor Unitário']
tab_faturamento_prod = tabela_vendas.groupby('Produto').sum()
tab_faturamento_prod = tab_faturamento_prod[['Faturamento']].sort_values(by='Faturamento', ascending=False)

print(tab_faturamento_prod)