import pandas as pd
import pywhatkit as kit
import time

# ID da planilha (extraído da URL)
sheet_id = '1Ve3nEUhMwNYpZR0EuwKloLJv4iOiBjWEX0O6Tq7eLTg'

# URL para acessar o conteúdo da planilha como CSV
sheet_url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv'

# Ler a planilha no pandas
df = pd.read_csv(sheet_url)

# Filtrar por "Aguardando Squad" na coluna 'situação'
filtro_situacao = df[df['Situação'] == 'Aguardando Squad']

# Excluir as pessoas com o texto específico na coluna 'Sobre o seu nível de programação...'
filtro_final = filtro_situacao[
    filtro_situacao['Sobre o seu nível de programação, escolha a opção que você mais se identifica'] != 
    'Possuo conhecimento um pouco mais avançado. Quero entrar no mercado!'
]

# Exibir os resultados com as colunas 'Nome' e 'Número'
resultado = filtro_final[['Nome', 'Telefone']]

# Mensagem a ser enviada
mensagem = (
    "Boa tarde, {nome}, sou a Victoria, da Programar Com Você. "
    "Gostaria de informar que estamos com novas vagas na nossa mentoria. "
    "Para que eu possa te alocar no melhor squad possível, qual é sua disponibilidade de horário? "
    "Nossas mentorias acontecem duas vezes na semana em um horário fixo com duração de uma hora. "
    "Temos o objetivo de acelerar seu desenvolvimento como programador inserindo você em projetos reais e em times de desenvolvimento. "
    "Fico no aguardo da sua resposta! 🚀"
)

# Enviar mensagem para cada usuário
for index, row in resultado.iterrows():
    
    nome = row['Nome']
    telefone = row['Telefone']
    
    # Enviar mensagem via WhatsApp
    kit.sendwhatmsg_instantly(f"+55{telefone}", mensagem.format(nome=nome), 10)  # Atraso de 10 segundos para envio
    time.sleep(10)  # Atraso entre os envios para evitar spam
