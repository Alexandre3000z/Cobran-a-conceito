from login import queryFatura

id = input('DIGITE O ID DA FATURA QUE GOSTARIA DE GERAR O BOLETO: ')

brudam = queryFatura(id)

print(brudam)