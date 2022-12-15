from Token import Token
from tabela_de_estados import TabelaDeEstados

class Tabela_de_Simbolos:
    def __init__(self):

        self.tabela = []

        self.tabela.append(Token(classe="inicio",lexema="inicio",tipo="inicio"))
        self.tabela.append(Token(classe="varinicio",lexema="varinicio",tipo="varinicio"))
        self.tabela.append(Token(classe="varfim", lexema="varfim", tipo="varfim"))
        self.tabela.append(Token(classe="escreva",lexema="escreva", tipo="escreva"))
        self.tabela.append(Token(classe="leia", lexema="leia",tipo= "leia"))
        self.tabela.append(Token(classe="se", lexema="se",tipo= "se"))
        self.tabela.append(Token(classe="entao",lexema= "entao",tipo= "entao"))
        self.tabela.append(Token (classe="fimse",lexema= "fimse",tipo= "fimse"))
        self.tabela.append(Token(classe="fim",lexema= "fim", tipo="fim"))
        self.tabela.append(Token(classe="inteiro",lexema= "inteiro",tipo= "inteiro"))
        self.tabela.append(Token(classe="literal",lexema= "literal",tipo= "literal"))
        self.tabela.append(Token(classe="real",lexema= "real",tipo= "real"))


    def buscar_token(self, token:Token):
            for t in self.tabela:
                if(t.lexema == token.lexema):
                    return t
            return None
        

    def inserir_token(self, token:Token):
            token_encontrado = self.buscar_token(token)
            if(token_encontrado is None):
                if(token.classe == "id"):
                    self.tabela.append(token)
                return token
            else:
                return token_encontrado

    def atualizar_token(self, token: Token):
        if(token.classe == "id"):
                token_tabela_simbolos = self.buscar_token(token)
                if(token_tabela_simbolos):
                    self.tabela.remove(token_tabela_simbolos)
                    self.tabela.append(token)  

    def imprimir_tabela(self):
            for t in self.tabela:
                print(f"Classe:{t.classe}, Lexema:{t.lexema}, Tipo:{t.tipo}")

    def construir_token(self, tabela_de_estados: TabelaDeEstados, lexema: str):
        classe = tabela_de_estados.retornaClasse()
        tipo = tabela_de_estados.retornaTipo()
        if classe == 'id':
            token = self.buscar_token(Token(classe, lexema, tipo))
            if token is None:
                token = self.inserir_token(Token(classe, lexema, tipo))
            self.atualizar_token(token)
            return token
        else:
            return Token(classe, lexema, tipo)