class Regras:
  def retornaElementos(self, index_reduce):
    arquivo_fonte = open('./tabelas/regras.txt' , encoding="utf-8")
    linha = arquivo_fonte.readlines()[int(index_reduce) -1]
    A, B = linha.split(' -> ')
    B = B.strip()
    regra = linha.strip()
    B = B.split(' ')
    
    arquivo_fonte.close()
    return A, B, regra


    