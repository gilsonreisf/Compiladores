def lerArquivo(nome_arquivo):
  with open(nome_arquivo, 'r') as fp:
    codigoFonte = fp.read()
    return codigoFonte  