import pandas as pd
from funcoes_auxiliares_sintatico import preencherErros


df_action = pd.read_csv('./tabelas/action.csv')
def mainAction():
    preencherErros(df_action, './tabelas/action.csv')


def action(estado, classe):
    try:
        return df_action[classe][estado]
    except KeyError:
        return ['e']