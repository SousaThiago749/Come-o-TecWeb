import json
from exemplo_de_uso import db
from database import *

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

def load_data():
    db = Database('banco')
    notes = db.get_all()
    return notes

# def load_data(arquivo):
#     path = "{nome}".format(nome=arquivo)
#     with open(path, 'r', encoding='utf-8') as arq:
#         dicionario = json.load(arq)
#     return dicionario

def load_template(arquivo):
    path = "templates/{nome}".format(nome=arquivo)
    with open(path, 'r', encoding='utf-8') as arq:
        conteudo = arq.read()
    return conteudo

def build_response(body='', code=200, reason='OK', headers=''):
    if headers=='':
        string = "HTTP/1.1 {code} {reason}\n\n{body}".format(code=code, reason=reason, headers=headers, body=body)
    else:
        string = "HTTP/1.1 {code} {reason}\n{headers}\n\n{body}".format(code=code, reason=reason, headers=headers, body=body) 
    return string.encode()