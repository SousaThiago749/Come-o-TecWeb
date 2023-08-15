def extract_route(request):
    rota = ""
    contador = 0
    for letra in request:
        if letra == "/":
            contador = 1
        if contador == 1:
            rota += str(letra)
        if contador == 1 and letra == " ":
            rota = rota[1:]
            rota = rota.replace(" ","")
            return rota
        

def read_file(path):
    file = open(path, 'rb')
    content = file.read()
    file.close()
    return content