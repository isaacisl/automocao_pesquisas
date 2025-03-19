import pandas as pd

arquivo = "base.xlsx"  
df = pd.read_excel(arquivo)

df = df.drop(df.columns[-3:], axis=1) # Remover as 3 ultimas colunas

dependencias = {
    "1.1. Se sim, qual o percentual de reajuste dos vencimentos da carreira do magistério será concedido em 2025?": 
    "1. O Município concedeu ou vai conceder reajuste dos vencimentos da carreira do magistério em 2025?",
    "1.2. Se sim, O reajuste aos profissionais do magistério em 2025 foi ou será estabelecido em lei municipal?": 
    "1. O Município concedeu ou vai conceder reajuste dos vencimentos da carreira do magistério em 2025?",
}


def validar_dependencias(df, subordinada, principal):
    
    mascara = (df[principal] == "Sim, concedeu ou vai conceder") & (df[subordinada].isna() | (df[subordinada] == ""))
    df.loc[mascara, subordinada] = "não respondeu"


for subordinada, principal in dependencias.items():
    validar_dependencias(df, subordinada, principal)



coluna_alvo_1 = "1. O Município concedeu ou vai conceder reajuste dos vencimentos da carreira do magistério em 2025?"
coluna_alvo_2 = "2. Até o momento, foram ajuizadas ações locais questionando o reajuste do piso do magistério?" 
coluna_alvo_3 = "3. Há no Município processos/ações/decisões judiciais determinando o cumprimento do piso do magistério conforme critério definido na Lei 11.738/2008?"
coluna_alvo_4 = "4. Com o percentual de reajuste do magistério concedido pelo Município em 2025, os limites com gastos com pessoal estabelecidos pela LRF estão/ficarão comprometidos?"


def marcar_nao_respondido(df, coluna_alvo):
    # Encontrar o índice da coluna alvo
    indice_alvo = df.columns.get_loc(coluna_alvo)
    
    # Definir o intervalo de colunas a verificar (próximas 12 colunas ou até o final)
    inicio = indice_alvo + 1
    fim = min(indice_alvo + 13, len(df.columns))
    outras_colunas = df.columns[inicio:fim].tolist()

    # Se não houver colunas subsequentes (coluna_alvo é a última), pular a lógica
    if not outras_colunas:
        print(f"Aviso: '{coluna_alvo}' é a última coluna. Não há colunas posteriores para verificar. Pulando...")
        return

    condicao_vazia = df[coluna_alvo].isna() | (df[coluna_alvo] == "")
    condicao_outras_preenchidas = df[outras_colunas].notna().any(axis=1)
    mascara = condicao_vazia & condicao_outras_preenchidas
    
    df.loc[mascara, coluna_alvo] = "Não respondeu"


marcar_nao_respondido(df, coluna_alvo_1)
marcar_nao_respondido(df, coluna_alvo_2)
marcar_nao_respondido(df, coluna_alvo_3)
marcar_nao_respondido(df, coluna_alvo_4)



df.to_excel("pesquisa_consolidada.xlsx", index=False)
print("Planilha consolidada salva como 'pesquisa_consolidada.xlsx'.")








