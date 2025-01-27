import json
from QueryBrudam import queryFatura
from teste import loginInter, emitir_cobranca
from utilities import identificar_tipo_pessoa
import time

id = input('DIGITE O ID DA FATURA QUE GOSTARIA DE GERAR O BOLETO: ')

brudam = queryFatura(id)[0]
print(brudam)

if brudam['cnpj_cliente']:
    print('Boleto encontrado, processando...')
    time.sleep(2)
    nomeCliente = input('Informe o nome do cliente: ')
    
else:
    raise('Boleto não foi encontrado, tente novamente!')

token = loginInter()

conta_corrente = '172384079'

dados_cobranca = {
    "seuNumero": "9866",
    "valorNominal": 291.50,
    "dataVencimento": "2025-01-30",
    "numDiasAgenda": 30,
    "pagador": {
        "cpfCnpj": brudam['cnpj_cliente'],
        "tipoPessoa": identificar_tipo_pessoa(brudam['cnpj_cliente']),
        "nome": nomeCliente,
        "endereco": "Avenida Brasil, 1200",
        "cidade": "Belo Horizonte",
        "uf": "MG",
        "cep": "30110000",
    },
    
    "multa": {
        "taxa": 2,
        "codigo": "PERCENTUAL",
    },
    "mora": {
        "taxa": 0.07,
        "codigo": "TAXAMENSAL",
    },
   
 
}

# if token:
    
#     # Emitir cobrança
#     resposta_cobranca = emitir_cobranca(token, conta_corrente, dados_cobranca)
#     if resposta_cobranca:
        
#         print("Cobrança emitida com sucesso:", json.dumps(resposta_cobranca, indent=2))
#     else:
#         print("Falha ao emitir a cobrança.")
# else:
#     print("Falha ao obter o token de autenticação.")
