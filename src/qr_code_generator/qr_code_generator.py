import pandas as pd
import qrcode
import sys
import os

# Caminho para o diretório do projeto
project_root = "C:\\Users\\casag\\Qrcode_generator"
sys.path.insert(0, project_root)

# Ler a planilha do Excel
planilha = pd.read_excel(r"C:\Users\casag\Downloads\hc.xlsx")
# planilha_10_registros = planilha.head(10)
# print(planilha_10_registros)

# Função para criar um código QR e salvar em um arquivo
def criar_qrcode(texto, nome_arquivo):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(texto)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(nome_arquivo)

# Diretório para salvar os códigos QR
qr_dir = "src/qrcodes"
os.makedirs(qr_dir, exist_ok=True)  # Cria o diretório se ele não existir

# Iterar sobre as linhas da planilha e criar QR codes
# Iterar sobre as linhas da planilha e criar QR codes
for index, linha in planilha.iterrows():
    numero_matricula = '{:08}'.format(str(linha["ID EMPLOYER"]))  # Formata o número de matrícula com zeros à esquerda

    # Crie uma cópia da linha, excluindo a coluna de número de matrícula
    linha_sem_matricula = linha.drop("ID EMPLOYER")

    # Transformar a linha em uma string CSV usando vírgulas
    conteudo_linha = ','.join(map(str, linha_sem_matricula))

    # Gerar um código QR com base no número de matrícula
    nome_arquivo = os.path.join(qr_dir, f"{numero_matricula}.png")
    criar_qrcode(conteudo_linha, nome_arquivo)





# Agora, você pode ler os QR codes gerados usando uma biblioteca apropriada.
