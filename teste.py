import requests
import json

from auth import CLIENT_ID, CLIENT_SECRET

# Arquivos do certificado e chave
cert_path = r"C:\\Users\\ADM\\Desktop\\PROJETOS\\Cobrança conceito\\Inter_API-Chave_e_Certificado\\certificado.crt"
key_path = r"C:\\Users\\ADM\\Desktop\\PROJETOS\\Cobrança conceito\\Inter_API-Chave_e_Certificado\\apiKey.key"


nomeCliente = 'TESTANDO TESTE'
def loginInter():
    # URL do endpoint do Banco Inter
    url = "https://cdpj.partners.bancointer.com.br/oauth/v2/token"

    


    # Dados necessários para a autenticação (conforme a documentação)
    data = {
    "client_id": CLIENT_ID,
    "client_secret": CLIENT_SECRET,
    "grant_type": "client_credentials",
    "scope": "boleto-cobranca.write"
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
            
            token = response.json().get("access_token")
            print(token)
            return token
        else:
            print(f"Erro {response.status_code}: {response.text}")
            return None
        
    
    except Exception as e:
        print("Ocorreu um erro:", e)


def emitir_cobranca(token, conta_corrente, dados_cobranca):
    url_cobranca_pix = "https://cdpj.partners.bancointer.com.br/cobranca/v3/cobrancas"

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "x-conta-corrente": conta_corrente,
    }

    try:
        response = requests.post(
            url_cobranca_pix,
            headers=headers,
            cert=(cert_path, key_path),
            json=dados_cobranca,
        )

        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"Erro ao emitir cobrança: {e}")
        return None

# conta_corrente = "172384079"

# # Dados da cobrança
# dados_cobranca = {
#     "seuNumero": "9866",
#     "valorNominal": 291.50,
#     "dataVencimento": "2025-01-30",
#     "numDiasAgenda": 30,
#     "pagador": {
#         "cpfCnpj": "04009865000170",
#         "tipoPessoa": "JURIDICA",
#         "nome": nomeCliente,
#         "endereco": "Avenida Brasil, 1200",
#         "cidade": "Belo Horizonte",
#         "uf": "MG",
#         "cep": "30110000",
#     },
    
#     "multa": {
#         "taxa": 2,
#         "codigo": "PERCENTUAL",
#     },
#     "mora": {
#         "taxa": 0.07,
#         "codigo": "TAXAMENSAL",
#     },
   
 
# }

# Obter token

# token = loginInter()

# if token:
    
#     # Emitir cobrança
#     resposta_cobranca = emitir_cobranca(token, conta_corrente, dados_cobranca)
#     if resposta_cobranca:
        
#         print("Cobrança emitida com sucesso:", json.dumps(resposta_cobranca, indent=2))
#     else:
#         print("Falha ao emitir a cobrança.")
# else:
#     print("Falha ao obter o token de autenticação.")

        
        
        
        
