from email import header
import requests

# GET Avaliações
#avaliacoes = requests.get('http://127.0.0.1:8000/api/v2/avaliacoes/')

# Acessando o status http
#print(avaliacoes.status_code)

# Acessando os dados da respota
#print(avaliacoes.json())

# Verificar o tipo de dados
#print(type(avaliacoes.json()))

# Acessando a quantidade de registros
#print(avaliacoes.json()['count'])


# Acessando os resultados da página
#print(avaliacoes.json()['results'])


# Acessando o primeiro elemento da lista de resultados
#print(avaliacoes.json()['results'][0])


# Acessando o último elemento da lista de resultados
#print(avaliacoes.json()['results'][-1])


# Acessando somente o nome da última pessoa que fez avaliação
#print(avaliacoes.json()['results'][-1]['nome'])

# ===========================================

# GET Avaliação
#avaliacao = requests.get('http://127.0.0.1:8000/api/v2/avaliacoes/2/')
#print(avaliacao.json())

# ===========================================

# GET cursos utilizando o Token

headers = {'Authorization': 'Token ba987131bf42c8df4447c789453ecd65b26ab1b0'}

cursos = requests.get(url='http://127.0.0.1:8000/api/v2/cursos/', headers=headers)
print(cursos.json())

