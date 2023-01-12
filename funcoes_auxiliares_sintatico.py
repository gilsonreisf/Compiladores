def isNaN(num):
    return num != num

def preencherErros(df, arquivoPath):
  colunas = df.columns
  qtdDeLinhas = len(df)
  for coluna in colunas:
    for index in range(qtdDeLinhas):
      if(isNaN(df[coluna][index])):
        df.loc[index, coluna] = 'e'+ str(index)

  df.to_csv(arquivoPath, index=False)


def desempilhar(pilha):
  if pilha:
    pilha.pop()
    if(len(pilha) == 0):
      pilha.append(0)

  else:
    pilha.append(0)
