arquivo = open("teste.txt", "r")
codigoFonte = arquivo.readlines()

def cleanCode(codigoFonte):
  size=len(codigoFonte)-1
  codigoFonte[size] = codigoFonte[size]+'\n'
  try:
      while True:
          codigoFonte.remove('\n')
  except ValueError:
      pass
  return codigoFonte
  
codigoFormatado = cleanCode(codigoFonte)


lexico = lex.AnalisadorLexico(codigoFormatado)
token = lexico.SCANNER()
print(token.toString())

while True:
  if(token.classe == 'EOF'):
    break
  token = lexico.SCANNER()
  print(token.toString())
print('\n')
lexico.tabelaDeSimbolos.toString()