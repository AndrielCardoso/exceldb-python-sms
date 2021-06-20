"""
Objetivo: Desenvolver um código capaz de analisar dentro de um banco de dados .xlsx com 6 planilhas, algum vendendor
que realizou uma venda maior que 55.000 e enviar uma mensagem de texto para o telefone selecionado.
"""

import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC82acf9c92382d7b359364e8a79c5047f"
# Your Auth Token from twilio.com/console
auth_token  = "9b6c10d11bbdb32c93b1982ce90b54e2"
client = Client(account_sid, auth_token)

lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']


for mes in lista_meses:
    tabelas = pd.read_excel(f'{mes}.xlsx')
    if (tabelas['Vendas'] >= 55000).any():
        vendedor = tabelas.loc[tabelas['Vendas'] >= 55000, 'Vendedor'].values[0]
        vendas = tabelas.loc[tabelas['Vendas'] >= 55000, 'Vendas'].values[0]
        message = client.messages.create(
            to="+5547996085407",
            from_="+15599222432",
            body=f"No mês de {mes} o vendedor {vendedor} vendeu {vendas} reais e bateu a meta!")

        print(message.sid)
