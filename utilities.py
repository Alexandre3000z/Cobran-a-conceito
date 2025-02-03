import re
import requests

def identificar_tipo_pessoa(documento):
# Remove caracteres não numéricos
    documento = ''.join(filter(str.isdigit, documento))
    
    if len(documento) == 11:
        return "FISICA"  # CPF possui 11 dígitos
    elif len(documento) == 14:
        return "JURIDICA"  # CNPJ possui 14 dígitos
    else:
        raise ValueError("Documento inválido. Um CPF deve ter 11 dígitos e um CNPJ deve ter 14 dígitos.")
    
    


def validar_cep(cep):
    """Verifica se o CEP tem um formato válido (8 dígitos numéricos)"""
    return re.fullmatch(r"\d{8}", cep) is not None    
    
def puxarCEP(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'
    headers = {'Content-Type': 'application/json'}
    try:
        response = requests.get(
            url,
            headers=headers,
            
        )
        resposta = response.json()
        return resposta
    
    except Exception as e:
        print(f'Erro ao consultar o CEP do cliente: {e}')    
        
puxarCEP(60864625)        