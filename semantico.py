from Token import Token

class Semantico:

    def __init__(self, programa_objeto, variaveis_temporarias, contador_temporarias) -> None:
        self.pilha_semantica = []
        self.programa_objeto = programa_objeto
        self.variaveis_temporarias = variaveis_temporarias
        self.contador_temporarias = contador_temporarias
        self.token_aux = Token(classe='',lexema='',tipo='')
        self.variaveis_para_receber_tipo = []
    

    #Função do analisador semântico, recebe a regra e a classe do token
    def ativa_semantico(self, regra, A, B, token_atual, tabelaDeSimbolos):
        #print(f'Token atual entrando no semantico: {token_atual}')
        #print(f'Pilha -1: {self.pilha_semantica[-1]}')
        #print(f'Regra: {regra}')
        #print(f'Pilha inteira: {self.pilha_semantica}')
        regra = int(regra)
        

        if regra in [1,2,3,4,12,18,24,28,29,30]:
            #Numero das regras que não fazem nada
            pass
        elif regra == 5:
            #Imprimir três linhas brancas no arquivo objeto (espaço para futura inserção de
            #declaração de variáveis), pode ser ajustado pelo desenvolvedor
            self.programa_objeto += '\n'*3

        elif regra == 6:
            #Amarração de atributos, organizar a passagem de valores do atributo TIPO.tipo,
            #para L.TIPO;
            #token_atual.tipo = self.pilha_semantica[-1].tipo
                                           
            #self.pilha_semantica[-3].tipo = self.pilha_semantica[-2].tipo
                #L                                  #TIPO
            self.pilha_semantica[-2].tipo =  self.pilha_semantica[-3].tipo
            
            for variaveis in self.variaveis_para_receber_tipo:
                variaveis.tipo = self.pilha_semantica[-3].tipo
                self.programa_objeto += f'{variaveis.tipo} {variaveis.lexema}'
            self.variaveis_para_receber_tipo.clear()
            
        elif regra == 7:
            #Amarração de atributos, organizar a passagem de valores do atributo.
            #token_atual.tipo = self.pilha_semantica[-1].tipo
                #ID                              #L1
            self.pilha_semantica[-3].tipo = token_atual.tipo

            tabelaDeSimbolos.atualizaTokenParaSemantico(Token(classe=self.pilha_semantica[-3].classe , lexema=self.pilha_semantica[-3].lexema, tipo=self.pilha_semantica[-3].tipo))
            
                #L1                     #ID
            token_atual.tipo = self.pilha_semantica[-3]
            self.variaveis_para_receber_tipo.append(self.pilha_semantica[-3])
        elif regra == 8:
            #Ajustar o preenchimento de id.tipo na tabela de símbolos:
            #Impressão do id no .obj
            #atualiza o tipo na tabela de simbolos
            token_atual = self.pilha_semantica[-1]
            
            classe, lexema, tipo = token_atual.classe, token_atual.lexema, token_atual.tipo
            tabelaDeSimbolos.atualizaTokenParaSemantico(Token(classe=classe, lexema=lexema, tipo=tipo))
            
            self.programa_objeto += " " + self.pilha_semantica[-1].lexema + '; \n'

        elif regra == 9:
            #print(f'Token atual: {token_atual}')
            #print(f'Pilha semantica: {self.pilha_semantica[:]}')
            #print(f'Topo pilha semantica: {self.pilha_semantica[-1].tipo}')
            #TIPO.tipo <- inteiro.tipo
            token_atual.tipo = self.pilha_semantica[-1].tipo
            #Imprimir ( TIPO.tipo);
            self.programa_objeto += 'int'
        elif regra == 10:
            #TIPO.tipo <- real.tipo
            token_atual.tipo = self.pilha_semantica[-1].tipo
            #Imprimir ( TIPO.tipo); 

            self.programa_objeto += 'double'
        elif regra == 11:
            #TIPO.tipo <- literal.tipo
            token_atual.tipo = self.pilha_semantica[-1].tipo
            #Imprimir ( TIPO.tipo); 

            self.programa_objeto += 'literal'
        elif regra == 13:

            if self.pilha_semantica[-2].tipo is not None and self.pilha_semantica[-2].tipo != '':  
                if self.pilha_semantica[-2].tipo == 'literal':
                    
                    self.programa_objeto += f'scanf("%s", {self.pilha_semantica[-2].lexema})\n'
                    
                elif self.pilha_semantica[-2].tipo == 'inteiro':
                    
                    self.programa_objeto += f'scanf("%d", &{self.pilha_semantica[-2].lexema})\n'
                    
                elif self.pilha_semantica[-2].tipo == 'real':
                    
                    self.programa_objeto += f'scanf("%lf", &{self.pilha_semantica[-2].lexema})\n'
                else:
                    print("Variável não declarada")

        elif regra == 14:
            #Gerar código para o comando escreva no arquivo objeto.
            #Imprimir ( #printf(“ARG.lexema”); )
            self.programa_objeto += f'\n printf({self.pilha_semantica[-2].lexema}) \n'
        elif regra == 15:
            #ARG.atributos <- literal.atributos (Copiar todos os atributos de literal para os
            #atributos de ARG).
            token_atual = self.pilha_semantica[-1]

        elif regra == 16:
            #ARG.atributos <- num.atributos (Copiar todos os atributos de literal para os atributos
            #de ARG).
            token_atual = self.pilha_semantica[-1]
        elif regra == 17:
            #Verificar se o identificador foi declarado (execução da regra semântica de número
            #6).
            #Se sim, então:
            
            if type(self.pilha_semantica[-1]) != None:
                token_atual = self.pilha_semantica[-1]
            #ARG.atributos <- id.atributos (copia todos os atributos de id para os de ARG).
            #Caso Contrário:
            else:
                print('Erro: Variável não declarada')
                
        elif regra == 19:
            if (type(self.pilha_semantica[-4]) != None and self.pilha_semantica[-4].tipo != ''):
                if (type(self.pilha_semantica[-4])) == (type(self.pilha_semantica[-2])):
                                                                                                        # ou tipo?
                    #self.programa_objeto += f'{self.pilha_semantica[-4].lexema} {self.pilha_semantica[-3].lexema} {self.pilha_semantica[-2].lexema} {self.pilha_semantica[-1].lexema}'
                    self.programa_objeto += f'\n{self.pilha_semantica[-4].lexema} = {self.pilha_semantica[-2].lexema}{self.pilha_semantica[-1].lexema}'
                else:
                    print("Erro: Tipos diferentes para atribuição")
            else:
                print('Erro: Variável não declarada')
        elif regra == 20:
            #Verificar se tipo dos operandos de de LD são equivalentes e diferentes de literal.
            opr1 = self.pilha_semantica[-1] #Opr1
            opr2 = self.pilha_semantica[-3] #Opr2
            opa = self.pilha_semantica[-2] #OPA
            #print(f'Pilha: {self.pilha_semantica}')
            print(f'OPR1: {opr1}')
            print(f'OPR2: {opr2}')
            print(f'Token atual: {token_atual}')
            if (opr1.tipo == token_atual.tipo) and (opr1.tipo == opr2.tipo) and opr1.tipo != 'literal':
                #if tipo1 == 'literal':
                #    Tx = 'char' + " T" + str(self.contador_temporarias) + ";"
                #    self.variaveis_temporarias += Tx
                #    token_atual.lexema = "T" + str(self.contador_temporarias)
                if tipo1 == 'inteiro':
                    Tx = 'int' + " T" + str(self.contador_temporarias) + ";"
                    self.variaveis_temporarias += Tx + '\n'
                    token_atual.lexema = "T" + str(self.contador_temporarias)
                    
                if tipo1 == 'real':
                    Tx = 'double' + " T" + str(self.contador_temporarias) + ";"
                    self.variaveis_temporarias += Tx + '\n'
                    token_atual.lexema = "T" + str(self.contador_temporarias)
                
                
                self.programa_objeto += f'T{self.contador_temporarias} = {opr1.lexema} {opa.lexema} {opr2.lexema};'
                self.contador_temporarias += 1
                
            else:
                print('Erro: Operandos com tipos incompatíveis')
            #Se sim, então:
            #Gerar uma variável numérica temporária Tx, em que x é um número gerado
            #sequencialmente.
            #LD.lexema <- Tx
            #Imprimir (Tx = OPRD.lexema opa.tipo OPRD.lexema) no arquivo objeto.
            #Caso contrário emitir “Erro: Operandos com tipos incompatíveis” ”, linha e coluna
            #onde ocorreu o erro no fonte.
                
        elif regra == 21:
            #LD.atributos <- OPRD.atributos (Copiar todos os atributos de OPRD para os atributos
            #de LD).
            token_atual = self.pilha_semantica[-1]
        elif regra == 22:
            #Verificar se o identificador está declarado.
            if type(self.pilha_semantica[-1]) != None:
                token_atual = self.pilha_semantica[-1]
            else: 
                print("Erro: Variável não declarada")

            pass
        elif regra == 23:
            #OPRD.atributos <- num.atributos (Copiar todos os atributos de num para os atributos
            #de OPRD).
            token_atual = self.pilha_semantica[-1]
        elif regra == 25:
            #Imprimir ( } ) no arquivo objeto.
            self.programa_objeto += '} \n'

        elif regra == 26:
            #Imprimir ( if (EXP_R.lexema) { ) no arquivo objeto.
            self.programa_objeto += f'\nif({self.pilha_semantica[-3].lexema})' + '\n{'
        elif regra == 27:
            
            tipo1 = self.pilha_semantica[-3].tipo
            tipo2 = self.pilha_semantica[-1].tipo
            opr = self.pilha_semantica[-2]
           
            if (tipo1 == tipo2) or (tipo1 == 'real' and tipo2 == 'int') or (tipo1 == 'int' and tipo2 == 'real'):
                self.variaveis_temporarias += 'int' + " T" + str(self.contador_temporarias) + "; \n"
                
                
                token_atual.lexema = "T" + str(self.contador_temporarias)
                token_atual.tipo = self.pilha_semantica[-1].tipo
                
                traduz_operador_para_c = opr.lexema
                if traduz_operador_para_c == '=':
                    traduz_operador_para_c = '=='
                elif traduz_operador_para_c == '<>':
                    traduz_operador_para_c = '!='
                self.programa_objeto += f'T{self.contador_temporarias} = {self.pilha_semantica[-1].lexema} {traduz_operador_para_c} {self.pilha_semantica[-3].lexema}'
            #Se sim, então:
                self.contador_temporarias += 1
            #Gerar uma variável booleana temporária Tx, em que x é um número
            #gerado sequencialmente.
            #EXP_R.lexema <- Tx
            #Imprimir (Tx = OPRD.lexema opr.tipo OPRD.lexema) no arquivo objeto.
            else:
                print('Erro: Operandos com tipos incompatíveis')
            #Caso contrário emitir “Erro: Operandos com tipos incompatíveis” ”, linha e coluna
            #onde ocorreu o erro no fonte.
        elif regra == 31:
            #self.programa_objeto += '} \n'
            pass
        elif regra == 32:
            self.programa_objeto += '\nreturn 0;\n}\n'
        
        return token_atual
