import pandas as pd

def excel_para_bloco_de_notas(arquivo_excel, arquivo_saida):
    df = pd.read_excel(arquivo_excel)

    df.to_csv(arquivo_saida, index=False, sep='\t')

if __name__ == "__main__":
    arquivo_excel = 'arquivo.xlsx'
    
    arquivo_saida = 'saida.txt'
    
    excel_para_bloco_de_notas(arquivo_excel, arquivo_saida)

    print(f"Conversão concluída. Os dados foram exportados para '{arquivo_saida}' em formato de bloco de notas.")
