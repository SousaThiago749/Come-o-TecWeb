from utils import load_data, load_template, build_response
from database import Database
import urllib

#importar objeto
#comecar com um objeto no inicio do index
#tacar o getall dentro do for, e do load data
#mudar o load data
def index(request):

    # A string de request sempre começa com o tipo da requisição (ex: GET, POST)
    if request.startswith('POST'):
        request = request.replace('\r', '')  # Remove caracteres indesejados
        # Cabeçalho e corpo estão sempre separados por duas quebras de linha
        partes = request.split('\n\n')
        corpo = partes[1]
        params = {}
        # Preencha o dicionário params com as informações do corpo da requisição
        # O dicionário conterá dois valores, o título e a descrição.
        # Posteriormente pode ser interessante criar uma função que recebe a
        # requisição e devolve os parâmetros para desacoplar esta lógica.
        # Dica: use o método split da string e a função unquote_plus
        for chave_valor in corpo.split('&'):
            texto = chave_valor.split("=")
            params[texto[0]] = urllib.parse.unquote_plus(texto[1],encoding="UTF-8", errors="replace")
            #params[texto[0]] = texto[1].replace("+"," ")
            return build_response(code=303, reason='See Other', headers='Location: /')
            

    # O RESTO DO CÓDIGO DA FUNÇÃO index CONTINUA DAQUI PARA BAIXO...
    # Cria uma lista de <li>'s para cada anotação
    # Se tiver curiosidade: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(title=dados['titulo'], details=dados['detalhes'])
        #for dados in load_data('notes.json')
        for dados in load_data()
    ]
    notes = '\n'.join(notes_li)


    return build_response(load_template('index.html').format(notes=notes))