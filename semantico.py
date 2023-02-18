#TODO:
#Não pode grar codigo.obj (ou .C) quando houver erro
#Para isso, salvar em uma string o código todo, e só salvar
#Em arquivo quando receber o accept


def insere_no_objeto(string, tipo):
    pass


#Função do analisador semântico, recebe a regra e a classe do token
def semantico(regra, a):
    if regra in [1,2,3,4,12,18,24,28,29,30]:
        #Numero das regras que não fazem nada
        pass
    if regra == 5:
        #Imprimir três linhas brancas no arquivo objeto (espaço para futura inserção de
        #declaração de variáveis), pode ser ajustado pelo desenvolvedor
        pass
    elif regra == 6:
        #Amarração de atributos, organizar a passagem de valores do atributo TIPO.tipo,
        #para L.TIPO;
        pass
    elif regra == 7:
        #Amarração de atributos, organizar a passagem de valores do atributo.
        pass
    elif regra == 8:
        #Ajustar o preenchimento de id.tipo na tabela de símbolos:
        #Impressão do id no .obj
        pass
    elif regra == 9:
        #TIPO.tipo <- inteiro.tipo
        #Imprimir ( TIPO.tipo);
        pass
    elif regra == 10:
        #TIPO.tipo <- real.tipo
        #Imprimir ( TIPO.tipo); 
        pass
    elif regra == 11:
        #TIPO.tipo <- literal.tipo
        #Imprimir ( TIPO.tipo); 
        pass
    elif regra == 13:
        #Verificar se o campo tipo do identificador está preenchido indicando a declaração
        #do identificador (execução da regra semântica de número 6).
        #Se sim, então:
        #Se id.tipo = literal Imprimir ( scanf(“%s”, id.lexema); )
        #Se id.tipo = inteiro Imprimir ( scanf(“%d”, &id.lexema); )
        #Se id.tipo = real Imprimir ( scanf(“%lf”, &id.lexema); )
        #Caso Contrário:
        #Emitir na tela “Erro: Variável não declarada”, linha e coluna onde ocorreu o
        #erro no fonte.
        pass
    elif regra == 14:
        #Gerar código para o comando escreva no arquivo objeto.
        #Imprimir ( printf(“ARG.lexema”); )
        pass
    elif regra == 15:
        #ARG.atributos <- literal.atributos (Copiar todos os atributos de literal para os
        #atributos de ARG).
        pass
    elif regra == 16:
        #ARG.atributos <- num.atributos (Copiar todos os atributos de literal para os atributos
        #de ARG).
        pass
    elif regra == 17:
        #Verificar se o identificador foi declarado (execução da regra semântica de número
        #6).
        #Se sim, então:
        #ARG.atributos <- id.atributos (copia todos os atributos de id para os de ARG).
        #Caso Contrário:
        # Emitir na tela “Erro: Variável não declarada” , linha e coluna onde ocorreu o
        #erro no fonte.
        pass
    elif regra == 19:
        #Verificar se id foi declarado (execução da regra semântica de número 6). Se sim,
        #então:
        #| Realizar verificação do tipo entre os operandos id e LD (ou seja, |
        #se ambos são do mesmo tipo).
        #| Se sim, então:
        #| | Imprimir (id.lexema rcb.tipo LD.lexema) no arquivo objeto.
        #| Caso contrário emitir: ”Erro: Tipos diferentes para atribuição”,
        #|__________linha e coluna onde ocorreu o erro no fonte.
        #Caso contrário emitir “Erro: Variável não declarada” ”, linha e coluna onde ocorreu
        #o erro no fonte.
        pass
    elif regra == 20:
        #Verificar se tipo dos operandos de de LD são equivalentes e diferentes de literal.
        #Se sim, então:
        #Gerar uma variável numérica temporária Tx, em que x é um número gerado
        #sequencialmente.
        #LD.lexema <- Tx
        #Imprimir (Tx = OPRD.lexema opa.tipo OPRD.lexema) no arquivo objeto.
        #Caso contrário emitir “Erro: Operandos com tipos incompatíveis” ”, linha e coluna
        #onde ocorreu o erro no fonte.
        pass
    elif regra == 21:
        #LD.atributos <- OPRD.atributos (Copiar todos os atributos de OPRD para os atributos
        #de LD).
        pass
    elif regra == 22:
        #Verificar se o identificador está declarado.
        #Se sim, então:
        #OPRD.atributos <- id.atributos
        #Caso contrário emitir “Erro: Variável não declarada” ”, linha e coluna onde ocorreu
        #o erro no fonte.
        pass
    elif regra == 23:
        #OPRD.atributos <- num.atributos (Copiar todos os atributos de num para os atributos
        #de OPRD).
        pass
    elif regra == 25:
        #Imprimir ( } ) no arquivo objeto.
        pass
    elif regra == 26:
        #Imprimir ( if (EXP_R.lexema) { ) no arquivo objeto.
        pass
    elif regra == 27:
        #Verificar se os tipos de dados de OPRD são iguais ou equivalentes para a
        #realização de comparação relacional.
        #Se sim, então:
        #Gerar uma variável booleana temporária Tx, em que x é um número
        #gerado sequencialmente.
        #EXP_R.lexema <- Tx
        #Imprimir (Tx = OPRD.lexema opr.tipo OPRD.lexema) no arquivo objeto.
        #Caso contrário emitir “Erro: Operandos com tipos incompatíveis” ”, linha e coluna
        #onde ocorreu o erro no fonte.
        pass
    elif regra == 31:
        #Letra D (Descobrir)
        pass
    elif regra == 32:
        #Letra E (Descobrir)
        pass