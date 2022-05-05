import requests

headers = {'Authorization': 'Token ba987131bf42c8df4447c789453ecd65b26ab1b0'}

url_base_cursos = 'http://127.0.0.1:8000/api/v1/cursos/'
url_base_avaliacoes= 'http://127.0.0.1:8000/api/v1/avaliacoes/'

resultado = requests.get(url=url_base_cursos, headers=headers)

# Verificando o status code
print(f'Código: {resultado.status_code}')

# Testando se o endpopint está correto
assert resultado.status_code == 200

# Verificando a quantidade de resgistros
print(resultado.json()['count'])

# Testando a quantidade de registros
assert resultado.json()['count'] == 7