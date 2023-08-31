import json

def extract_route(request):
    barra = request.find('/')
    http = request.find('HTTP')
    rota = request[barra+1:http-1]
    return rota
        

def read_file(path):
    file = open(path, 'rb')
    content = file.read()
    file.close()
    return content

# def load_data(arquivo):
#     path = "data/{nome}".format(nome=arquivo)
#     with open(path, 'r', encoding='utf-8') as arq:
#         dicionario = json.load(arq)
#     return dicionario

def load_data(arquivo):
    path = "{nome}".format(nome=arquivo)
    with open(path, 'r', encoding='utf-8') as arq:
        dicionario = json.load(arq)
    return dicionario

def load_template(arquivo):
    path = "templates/{nome}".format(nome=arquivo)
    with open(path, 'r', encoding='utf-8') as arq:
        conteudo = arq.read()
    return conteudo

def build_response(body='', code=200, reason='OK', headers=''):
    response = f'HTTP/1.1 {code} {reason}\n'
    if headers:
        response += f'{headers}\n'
    response += '\n'
    if body:
        response += f'{body}'
    return response.encode()