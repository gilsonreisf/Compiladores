arquivo = open("teste.txt", "r")
codigoFonte = arquivo.readlines()

def limpa_codigo(codigoFonte):
  novo_codigo = []
  for i in codigoFonte:
    novo_codigo.append(i[:][:-1])
  return novo_codigo
  
codigoFormatado = limpa_codigo(codigoFonte)

codigo_final = []
for line in codigoFormatado:
    for caractere in line:
        codigo_final.append(caractere)

print(codigo_final)

'''
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
'''