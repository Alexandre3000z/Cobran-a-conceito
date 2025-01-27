def identificar_tipo_pessoa(documento):
# Remove caracteres não numéricos
    documento = ''.join(filter(str.isdigit, documento))
    
    if len(documento) == 11:
        return "FISICA"  # CPF possui 11 dígitos
    elif len(documento) == 14:
        return "JURIDICA"  # CNPJ possui 14 dígitos
    else:
        raise ValueError("Documento inválido. Um CPF deve ter 11 dígitos e um CNPJ deve ter 14 dígitos.")