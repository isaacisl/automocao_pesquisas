import pandas as pd

# Carrega o arquivo Excel
df = pd.read_excel("base.xlsx")
print("Total de colunas no arquivo:", len(df.columns))

# Remove as últimas 3 colunas
df = df.drop(df.columns[-3:], axis=1)


print("Total de colunas no arquivo:", len(df.columns))

# Remove a coluna na posição 2 (índice 2)
df = df.drop(df.columns[1], axis=1)

## Movendo itens para o final da tabela do excel 
coluna_ID = df.pop(df.columns[0])  # Remove a coluna 1 do DataFrame e armazena
df[df.columns[-1] + 'ID'] = coluna_ID  # Adiciona a coluna no final com um nome temporário

coluna_populacao = df.pop(df.columns[0]) ## Remove e armazena a coluna população 
df[df.columns[-1] + 'População'] = coluna_populacao # Adiciona a coluna no Final com o nome ajustado


## Movendo itens para o inicio da tabela
coluna_regiao = df.pop(df.columns[3])  
coluna_uf = df.pop(df.columns[1])      

df.insert(0, 'Região', coluna_regiao) 
df.insert(1, 'UF', coluna_uf)         


# Remove as colunas status e observações e coloca no final
coluna_status = df.pop(df.columns[4])  # Remove a coluna no índice 4
coluna_obs = df.pop(df.columns[4])     # Remove a coluna no índice 4 (era 5 originalmente)

# Adiciona as colunas ao final com os nomes corretos
df['Status'] = coluna_status
df['Observações'] = coluna_obs


#Adiciona coluna dos portes
coluna_porte = ['vazio'] * len(df)  # Repete 'vazio' para todas as linhas
df.insert(26, 'Porte', coluna_porte)


# Remove a coluna emails
df = df.drop([df.columns[14]], axis=1)


# -----------  Començando a tratar os dados ------------

# =cont.valores
colunas_intervalo = df.iloc[:, 14:23]  # Do índice 14 até o 20 (21 é exclusivo)
colunas_dados = colunas_intervalo.notna().sum(axis=1)


# Insere a nova coluna na posição 14
df.insert(14, 'dados', colunas_dados)





# Salva o resultado em um novo arquivo
df.to_excel('base_modificada.xlsx', index=False)

print("Últimas 3 colunas removidas com sucesso!")
