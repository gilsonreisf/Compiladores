from Token import Token
from caractere_invalido_error import CaractereInvalidoError
from tabela_de_estados import TabelaDeEstados
from tabela_de_simbolos import TabelaDeSimbolos
from funcoes_auxiliares_lexico import lerArquivo



class Scanner:
    
    def __init__(self, nome_arquivo):
        
             
        self.codigoFonte = lerArquivo(nome_arquivo)
        self.ponteiro = 0
        self.linha = 1
        self.coluna = 1        

    def tratarEspacosVazios(self, lexema, char, estadoAtual):
        literalIncompleto = [7, 8]
        comentarioIncompleto = [12, 13]
        espacosVazios = [' ', '\n', '\t']

        if (char not in espacosVazios) or ((estadoAtual in literalIncompleto)) or ((estadoAtual in comentarioIncompleto)):
            lexema = lexema + char
            return lexema
        else:
            return lexema

    def tratarFinalDeLinha(self, lexema, tabelaEstados: TabelaDeEstados, tabelaDeSimbolos: TabelaDeSimbolos):
        literalIncompleto = [7, 8]
        comentarioIncompleto = [12, 13]
        estadoAtual = tabelaEstados.estado_atual
        
        if ((estadoAtual in literalIncompleto)) or ((estadoAtual in comentarioIncompleto)):
            self.lancaErro(tabelaEstados.estado_atual)
            return tabelaDeSimbolos.construirToken(tabelaEstados, lexema, True)

    def avancaLeitura(self):
        self.ponteiro = self.ponteiro + 1
        self.coluna = self.coluna + 1 
    
    
    def SCANNER(self, tabelaEstados: TabelaDeEstados, tabelaDeSimbolos: TabelaDeSimbolos):

        tabelaEstados.estado_atual = 0
        lexema = ''


        while self.ponteiro <= len(self.codigoFonte):
        

            try:

                char = self.codigoFonte[self.ponteiro]
                entrada = tabelaEstados.verificaTipoCaractere(char)
                if (tabelaEstados.verificarSeEntradaPertenceAoAlfabeto(entrada)):
                    tabelaEstados.irParaProximoEstado(entrada)

                elif(tabelaEstados.verificarSeComentarioOuLiteral()):
                    tabelaEstados.irParaProximoEstado(entrada)

                else:
                    raise CaractereInvalidoError

                

            except CaractereInvalidoError:
                if len(lexema) > 0:
                    return tabelaDeSimbolos.construirToken(tabelaEstados, lexema)
                
                self.lancaErro(tabelaEstados.estado_atual, char)
                self.avancaLeitura()
                
                return tabelaDeSimbolos.construirToken(tabelaEstados, char, True)

            except KeyError: # Erro quando o próximo estado é inválido
                if (tabelaEstados.estado_atual == 4 or tabelaEstados.estado_atual == 5): # Número exponencial incompleto
                    self.lancaErro(tabelaEstados.estado_atual)
                    return tabelaDeSimbolos.construirToken(tabelaEstados, lexema, True)

                if tabelaEstados.estado_atual == 14: # Comentário encerrado (não deve ser exibido coomo token)
                    tabelaEstados.estado_atual = 0
                    lexema = ''
                    continue       
                
                if len(lexema) > 0:
                    return tabelaDeSimbolos.construirToken(tabelaEstados, lexema)
                
                self.lancaErro(tabelaEstados.estado_atual, char)
                self.avancaLeitura()
                return tabelaDeSimbolos.construirToken(tabelaEstados, char, True)
                
            except IndexError: # Tratamento para quando ler o último caractere do código fonte
                self.avancaLeitura()
                if len(lexema) > 0:
                    if tabelaEstados.estado_atual not in tabelaEstados.estados_finais:
                        self.lancaErro(tabelaEstados.estado_atual)
                    
                    return tabelaDeSimbolos.construirToken(tabelaEstados, lexema)
                else: 
                    break
            
            
            else:
                self.avancaLeitura()

                if char == '\n':

                    literalIncompleto = [7, 8]
                    comentarioIncompleto = [12, 13]
                    estadoAtual = tabelaEstados.estado_atual
                    self.linha = self.linha + 1
                    
                    if ((estadoAtual in literalIncompleto)) or ((estadoAtual in comentarioIncompleto)):
                        self.lancaErro(tabelaEstados.estado_atual)
                        return tabelaDeSimbolos.construirToken(tabelaEstados, lexema, True) 

                    self.coluna = 1
                
                lexema = self.tratarEspacosVazios(lexema, char, tabelaEstados.estado_atual)

        
        return Token('EOF', 'EOF', None)



    def lancaErro(self, estado, c=''):
        if estado == 2 or estado == 4 or estado == 5:
            print(f'ERRO LÉXICO - Número incompleto. Linha {self.linha}, coluna {self.coluna}')
        elif estado == 7 or estado == 8:
            print(f'ERRO LÉXICO - Literal incompleto. Linha {self.linha}, coluna {self.coluna -1}')
        elif estado == 12 or estado == 13:
            print(f'ERRO LÉXICO - Comentário incompleto. Linha {self.linha}, coluna {self.coluna -1}')
        else:
            print(f'ERRO LÉXICO - Caractere inválido: "{c}". Linha {self.linha}, coluna {self.coluna}')