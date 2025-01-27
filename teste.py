import requests

from auth import CLIENT_ID, CLIENT_SECRET
# URL do endpoint do Banco Inter
url = "https://cdpj.partners.bancointer.com.br/oauth/v2/token"

# Arquivos do certificado e chave
cert_path = r"C:\\Users\\ADM\\Desktop\\PROJETOS\\Cobrança conceito\\Inter_API-Chave_e_Certificado\\certificado.crt"
key_path = r"C:\\Users\\ADM\\Desktop\\PROJETOS\\Cobrança conceito\\Inter_API-Chave_e_Certificado\\apiKey.key"


# Dados necessários para a autenticação (conforme a documentação)
data = {
    "client_id": CLIENT_ID,
    "client_secret": CLIENT_SECRET,
    "grant_type": "client_credentials"
}

# Enviando a requisição com os certificados
try:
    response = requests.post(
        url,
        data=data,
        cert=(cert_path, key_path)  # Fornecendo os arquivos .crt e .key
    )

    # Verificando a resposta
    if response.status_code == 200:
        print("Token recebido:", response.json())
    else:
        print(f"Erro {response.status_code}: {response.text}")

except Exception as e:
    print("Ocorreu um erro:", e)
