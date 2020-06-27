import json
import requests
import datetime

#---------------------------------------------------------------------------#
#   Date Formatting
#---------------------------------------------------------------------------#

data_e_hora_atuais = datetime.datetime.now()
data_anterior = data_e_hora_atuais - datetime.timedelta(days=1)

data = data_e_hora_atuais.strftime('%Y%m%d')
d = data_anterior.strftime("%Y%m%d")
data_formatada = data_e_hora_atuais.strftime('%d/%m/%Y')


#--------------------------------------------------------------------------#
#   Links APIs
#--------------------------------------------------------------------------#

api_boletim = 'https://brasil.io/api/dataset/covid19/boletim/data/?format=json'

#---------------------------------------------------------------------------#
#   Boletins diarios de cada estado brasileiro
#---------------------------------------------------------------------------#

def get_boletins_anterior():

    data = datetime.datetime.now()
    data_atual_formatado = data.strftime('%Y-%m-%d')
    d = data_anterior.strftime("%Y-%m-%d")    
    
    informacoes = []

    request = requests.get(api_boletim)
    
    if request.status_code == 200:
        reddit_data = json.loads(request.content)

    # Obter as informacoes dos boletins do dia anterior
    for info in reddit_data['results']:
        if info['date'] == d:
            informacoes.append(info)

    return informacoes


def state_situations():
    
    api_situacao_estados = 'https://covid19-brazil-api.now.sh/api/report/v1/brazil/'
    api_situacao_estados += data+'?format=json'

    r = requests.get(api_situacao_estados)
    
    dados = []

    if r.status_code == 200:
        reddit_data = json.loads(r.content)
        
        '''
            * Condicional verificando o tamanho do retorno do conteudo
            * que busca informações do dia atual, caso não possua nenhum
            * dado, ele busca o do dia anterior
        '''
        
        if(len(reddit_data['data']) == 0):
            
            api_situacao_estados = 'https://covid19-brazil-api.now.sh/api/report/v1/brazil/'+d+'?format=json'
            
            r = requests.get(api_situacao_estados)

            if r.status_code == 200:
                reddit_data = json.loads(r.content)


    for i in reddit_data['data']:
        dados.append(i)

    return dados
