import requests
from auth import PASSWORD, USER

#Requisição basica de fatura pelo ID
def queryFatura(id):
    
  
    url = f"https://conceitocargas.brudam.com.br/api/v1/financeiro/faturas?id={id}"  # Substitua pela URL correta

    data = {
        
        "auth": {
            "usuario": USER,
            "senha": PASSWORD
        }
    }

    # Enviando uma solicitação POST
    try:
        response = requests.get(url, json=data)
        
        # Verificando a resposta
        if response.status_code == 200:
            teste = response.json()
            return (teste['data']['documentos'])
            
        else:
            print(f"Erro: {response.status_code} - {response.text}")
    except Exception as e:
        print("Ocorreu um erro:", e)
