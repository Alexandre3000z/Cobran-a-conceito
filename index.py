import json
from QueryBrudam import queryFatura
from teste import loginInter, emitir_cobranca
from utilities import identificar_tipo_pessoa, validar_cep
import time

id = input('INFORME O ID DA FATURA QUE GOSTARIA DE GERAR O BOLETO: ')


# Loop para garantir que um CEP válido seja inserido
while True:
    cep = input("INFORME O CEP DO CLIENTE: ")
    
    if validar_cep(cep):
        print("✅ CEP válido:", cep)
        break  # Sai do loop se o CEP for válido
    else:
        print("❌ CEP inválido! O CEP deve conter exatamente 8 dígitos numéricos. Tente novamente.")


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
    "seuNumero": id,
    "valorNominal": brudam['valor'],
    "dataVencimento": brudam['data_vencimento'],
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

print(dados_cobranca)

# if token:
    
#     # Emitir cobrança
#     resposta_cobranca = emitir_cobranca(token, conta_corrente, dados_cobranca)
#     if resposta_cobranca:
        
#         print("Cobrança emitida com sucesso:", json.dumps(resposta_cobranca, indent=2))
#     else:
#         print("Falha ao emitir a cobrança.")
# else:
#     print("Falha ao obter o token de autenticação.")
