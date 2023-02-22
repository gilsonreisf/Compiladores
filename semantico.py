#TODO:
#Não pode grar codigo.obj (ou .C) quando houver erro
#Para isso, salvar em uma string o código todo, e só salvar
#Em arquivo quando receber o accept
from Token import Token

def inicia_arquivo_objeto():
    with open('PROGRAMA.C', 'x') as f:
        f.write('#include <stdio.h>')

def insere_no_objeto(string, tipo):
    pass


#Função do analisador semântico, recebe a regra e a classe do token
def semantico(regra, token_atual, A, B, tabelaDeSimbolos):
    token_aux = Token(classe='',lexema='',tipo='')
    flag_amarracao = False
    
    if regra in [1,2,3,4,12,18,24,28,29,30]:
        #Numero das regras que não fazem nada
        pass
    if regra == 5:
        #Imprimir três linhas brancas no arquivo objeto (espaço para futura inserção de
        #declaração de variáveis), pode ser ajustado pelo desenvolvedor
        return '\n'*3
        
    elif regra == 6:
        #Amarração de atributos, organizar a passagem de valores do atributo TIPO.tipo,
        #para L.TIPO;
        token_atual.tipo = token_aux.tipo
        flag_amarracao = True
    elif regra == 7:
        print("=_"*20)
        print(f"Token atual: {token_atual}")
        #Amarração de atributos, organizar a passagem de valores do atributo.
        token_atual.tipo = token_aux.tipo
        #Atualiza tabela de simbolos
        classe, lexema, tipo = token_atual.classe, token_atual.lexema, token_atual.tipo
        tabelaDeSimbolos.atualizarToken(Token(classe=classe, lexema=lexema, tipo=tipo))
        
        #L1 tipo = L2 tipol 
        #token_atual.tipo = token_aux.tipo

    elif regra == 8:
        #Ajustar o preenchimento de id.tipo na tabela de símbolos:
        #Impressão do id no .obj
        #atualiza o tipo na tabela de simbolos
        classe, lexema, tipo = token_atual.classe, token_atual.lexema, token_atual.tipo
        tabelaDeSimbolos.atualizarToken(Token(classe=classe, lexema=lexema, tipo=tipo))

    elif regra == 9:
        #TIPO.tipo <- inteiro.tipo
        token_aux.tipo = 'inteiro'
        #Imprimir ( TIPO.tipo);
        return 'int'
    elif regra == 10:
        #TIPO.tipo <- real.tipo
        #Imprimir ( TIPO.tipo); 
        token_aux.tipo = 'real'
        return 'double'
    elif regra == 11:
        #TIPO.tipo <- literal.tipo
        #Imprimir ( TIPO.tipo); 
        token_aux.tipo = 'literal'
        return 'literal'
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
        
        if token_aux.tipo == 'literal':
            return f'scanf("%s", {token_atual.lexema})'
        elif token_aux.tipo == 'inteiro':
            return f'scanf("%d", &{token_atual.lexema})'
        elif token_aux.tipo == 'real':
            return f'scanf ("%lf", &{token_atual.lexema})'
        else:
            #TODO: Propagar linha e coluna pra chegar até aqui
            #Emitir na tela “Erro: Variável não declarada”, linha e coluna onde ocorreu o
            #erro no fonte.
            print("Variável não declarada")
        
    elif regra == 14:
        #Gerar código para o comando escreva no arquivo objeto.
        #Imprimir ( printf(“ARG.lexema”); )
        return f'printf("{token_atual.lexema}")'
    elif regra == 15:
        #ARG.atributos <- literal.atributos (Copiar todos os atributos de literal para os
        #atributos de ARG).
        token_atual = token_aux
        
    elif regra == 16:
        #ARG.atributos <- num.atributos (Copiar todos os atributos de literal para os atributos
        #de ARG).
        token_atual = token_aux
    elif regra == 17:
        #Verificar se o identificador foi declarado (execução da regra semântica de número
        #6).
        #Se sim, então:
        if flag_amarracao:
            token_atual = token_aux
        #ARG.atributos <- id.atributos (copia todos os atributos de id para os de ARG).
        #Caso Contrário:
        else:
            print('Variável não declarada')
        # Emitir na tela “Erro: Variável não declarada” , linha e coluna onde ocorreu o
        #erro no fonte.
        pass
    elif regra == 19:
        #Verificar se id foi declarado (execução da regra semântica de número 6). Se sim,
        #então:
        
        if flag_amarracao:
            if token_atual.tipo == token_aux.tipo:
        #| Realizar verificação do tipo entre os operandos id e LD (ou seja, |
        #se ambos são do mesmo tipo).
        #| Se sim, então:
        #| | Imprimir (id.lexema rcb.tipo LD.lexema) no arquivo objeto.
                return f'{token_atual.lexema} {token_atual.tipo} {token_aux.lexema}'
        #| Caso contrário emitir: ”Erro: Tipos diferentes para atribuição”,
            else:
                print('Erro: Variável não declarada')
        #|__________linha e coluna onde ocorreu o erro no fonte.
        #Caso contrário emitir “Erro: Variável não declarada” ”, linha e coluna onde ocorreu
        #o erro no fonte.
        pass
    elif regra == 20:
        #Verificar se tipo dos operandos de de LD são equivalentes e diferentes de literal.
        if (B[0] == B[-1]) and (B[-1] != 'literal'): 
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
        token_atual = token_aux
    elif regra == 22:
        #Verificar se o identificador está declarado.
        #Se sim, então:
        if flag_amarracao:
            token_atual = token_aux
        else:
            print('Erro: Variável não declarada')
        #OPRD.atributos <- id.atributos
        #Caso contrário emitir “Erro: Variável não declarada” ”, linha e coluna onde ocorreu
        #o erro no fonte.
        pass
    elif regra == 23:
        #OPRD.atributos <- num.atributos (Copiar todos os atributos de num para os atributos
        #de OPRD).
        token_atual = token_aux
    elif regra == 25:
        #Imprimir ( } ) no arquivo objeto.
        return '} \n'
        
    elif regra == 26:
        #Imprimir ( if (EXP_R.lexema) { ) no arquivo objeto.
        return '\n {'
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
    
