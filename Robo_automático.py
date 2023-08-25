import yfinance
import pyautogui
import pyperclip
import time

# Ticker é o código de uma ação.

ticker = input("Digite o código da ação: ") # PETR4.SA
dados = yfinance.Ticker(ticker)
dados.history()

# Configurando o período histórico (Ano = y / Mês = mo / Dia = d)

tabela = dados.history("6mo")
print(tabela)

# Selecionando apenas a coluna de fechamento (Close)

"""
Para selecionar a coluna desejada, basta colocar o nome dela e colchetes na
frente da variável que está armazenando os dados
"""

fechamento = tabela["Close"]
print(fechamento)




# Gerando um gráfico de linha

"""Vamos gerar um gráfico muito simples, apenas ultilizando o método .plot()"""


""" 
O comando fechamento.plot() está relacionado ao uso da biblioteca pandas e
é usado para traçar (ou plotar) um gráfico dos dados contidos na coluna de fechamento
de um DataFrame.

"""


fechamento.plot() # Plotando o gráfico de fechamento

# Gerando as estatísticas

"""
1 - Gerar estatísticas no python é muito simples, pois já temos os métodos prontos para
serem aplicados !

    Cotação max
    Cotação min
    Cotação atual: é a última linha ! Para acessá-la basta colocar [-1]
"""

maxima = fechamento.max()
minima = fechamento.min()
atual = fechamento[-1]
print(maxima)
print(minima)
print(atual)

# Enviando e-mail de forma automática

"""

- Processo de enviar um e-mail passo a passo:
    - abrir uma nova aba no navegador (clicar em + ou CTRL + T)
    - digitar o endereço do gmail (www.gmail.com) e digitar ENTER
    - clicar em **Escrever**
    - digitar o endereço de e-mail do destinatário
    - mudar para o campo Assunto (clicar no campo ou digitar tab)
    - digitar o Assunto
    - mudar para campo principal do e-mail (clicar no campo ou digitar tab)
    - escrever a mensagem
    - clicar em **Enviar**

"""

# Você irá instalar a biblioteca pip install pyautogui e também a pyperclip

# Criando o e-mail que vamos enviar

destinatario = "elechous@hotmail.com"
assunto = "Análise diária"
mensagem = f"""

Segue abaixo as análises da ação {ticker} dos últimos seis meses:

Cotação máxima: R${round(maxima,2)}
Cotação mínima: R${round(minima, 2)}
Cotação Atual: R${round(atual ,2)}

Atenciosamente,
MGP
"""
"""
Exemplo do que o comando round() faz, = arredondamento dos números.

numero = 3.14159
numero_arredondado = round(numero, 2)
print(numero_arredondado)  # Isso imprimirá 3.14

"""
print(destinatario)
print(assunto)
print(mensagem)

# Automatizando o envio

# Configurar uma pausa entre ações do pyautogui

pyautogui.PAUSE = 17

# abrir uma nova aba
pyautogui.hotkey("ctrl", "t")
pyautogui.click(x=514, y=18)


# Copiar o endereço do hotmail para o clipboard

pyperclip.copy("https://outlook.live.com/mail/0/")

# Colar o endereço e dar um ENTER

pyautogui.hotkey("ctrl", "v")
pyautogui.press('enter')

# Clicando no botão escrever

pyautogui.click(x=146, y=222)

# Preenchendo o destinatário

pyperclip.copy(destinatario)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("tab")

# Preenchendo o assunto
# ESTA DANDO ERRO DAQUI PARA BAIXO

pyperclip.copy(assunto)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("tab")

# Preenchendo a mensagem

pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl", "v")

# Clicar no botão enviar email

pyautogui.click(x=374, y=271)

# Fechar a aba do hotmail

pyautogui.hotkey("ctrl", "f4")

# Imprimir mensagem de enviado com sucesso

print("Email enviado com sucesso!")

