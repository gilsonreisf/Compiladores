import tabela_de_estados as TabelaDeEstados
from scanner_felps import Scanner as Scanner

arquivo = open("teste.txt", "r")
codigoFonte = arquivo.readlines()

def limpa_codigo(codigoFonte):
  novo_codigo = []
  for i in codigoFonte:
    novo_codigo.append(i[:][:-1])
  return novo_codigo


codigoFormatado = limpa_codigo(codigoFonte)
print(codigoFormatado)
scanner = Scanner(codigoFormatado)
token = scanner.scanner()
#print(token)

while True:
    if not(token):# and (token.classe == "EOF"):
        break
    token = scanner.scanner()
    #print(token)
print('\n')

scanner.Tabela_de_Simbolos.imprimir_tabela()