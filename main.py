import tabela_de_estados as TabelaDeEstados
import scanner as Scanner

arquivo = open("teste.txt", "r")
codigoFonte = arquivo.readlines()

def limpa_codigo(codigoFonte):
  novo_codigo = []
  for i in codigoFonte:
    novo_codigo.append(i[:][:-1])
  return novo_codigo
  
codigoFormatado = limpa_codigo(codigoFonte)


tabelaEstados = TabelaDeEstados()
scanner = Scanner(codigoFormatado)

scanner.scannerMain(tabelaEstados, codigoFormatado)

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