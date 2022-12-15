import tabela_de_estados as TabelaDeEstados
from scanner_felps import Scanner as Scanner

arquivo = open("teste.txt", "r", encoding="utf-8")
#arquivo = open("novo_teste.txt", "r")
#arquivo = open("teste_avancado.txt", "r")
codigoFonte = arquivo.readlines()


def limpa_codigo(codigoFonte):
  size=len(codigoFonte)-1
  codigoFonte[size] = codigoFonte[size]+'\n'
  try:
      while True:
          codigoFonte.remove('\n')
  except ValueError:
      pass
  return codigoFonte


codigoFormatado = limpa_codigo(codigoFonte) 
#print(codigoFormatado)
scanner = Scanner(codigoFormatado)
token = scanner.scanner()
print(token)

while True:
    if (token.classe == "EOF"):
        break
    token = scanner.scanner()
    print(token)
print('\n')

scanner.Tabela_de_Simbolos.imprimir_tabela()