import pandas as pd

df_goto = pd.read_csv('./tabelas/goto.csv')

def goto(estado, classe):
    return df_goto[classe][estado]
  