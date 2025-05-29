#comentar o sistema inteiro, montando diagramas e explicar como se comunicam
# no diagrama de classe tem q ter. EX pessoa: atributos[nome, idade, cpf] metodos [andar, correr, falar] 
#deixar o codigo limpo e organizado para ajudar na rapidez e facilidade de ajustes futuros



# OQUE DEVE SER VALIDADO EM UMA API --------------------------

# Endpoints: seus metodos (GET, POST, PUT, DELETE)

# Parametros: quais sao e para que servem. Ex:GET/user?age=30 ----- age é utilizado para filtrar usuarios com 30 anos

# Codigo de erro: ERROR 404, para q serve, deixar indicado

# Autenticaçao e autorizaçao: ver permissoes do usuario


# ATIVIDADE---------


# API adivice

# Endpoints? Sim HTTPS-GET
# Parametros? sim https://api.adviceslip.com/advice
# Mostra erros? NAO, nao tem parte para erros
# Ela requer autenticação? NAO, é uma API simples de conselho


def atividade():

    qualEndpoint = ''
    qualParametro = ''
    qualError = ''
    qualtoken = ''

    endpoint = input("essa API tem Endpoints? s/n: ")
    if endpoint == 's':
        qualEndpoint = input("qual? GET/PUT/POST/DELETE: ")
    elif endpoint == 'n':
        qualEndpoint = "nao tem Endpoint"
    else:
        print("digite certo!")
        return
    parametros = input("Ela tem parametros? s/n:")
    if parametros == 's':
        qualParametro = input("copie e cole aqui a url do parametro: ")
    elif parametros == 'n':
        qualParametro = 'Nao tem parametros'
    else:
        print("digite certo!")
        return
    error = input("Essa api mostra a resolução caso apareça algum erro? como 404, 401... s/n:")
    if error == 's':
        qualError = int(input("digite um erro que aparece: "))
    elif error == 'n':
        qualError = 'nao tem resoluçao de erros'
    else:
        print("digite certo!")
        return
    autenticacao = input("Ela requer autenticação? s/n:") 
    if autenticacao == 's':
        qualtoken = input("digite o token de autenticação: ")
    elif autenticacao == 'n':
        qualtoken = 'nao tem autenticaçao'
    else:
        print("digite certo!")
    print("------------------------------------------")
    print(f"A documentação dessa API é:\nEndpoint: {qualEndpoint}\nParametros: {qualParametro}\nErro: {qualError}\nautenticação: {qualtoken}")
    ("------------------------------------------")
atividade()





# 1 - liga as classe
# 2 - herança , pai herda pro filho
# 3 - composição (força a apagar os filhos se for apagar o pai)
# 4 - agregação (pode apagar o pai)