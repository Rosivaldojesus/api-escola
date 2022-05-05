import requests

headers = {'Authorization': 'Token ba987131bf42c8df4447c789453ecd65b26ab1b0'}

url_base_cursos = 'http://127.0.0.1:8000/api/v1/cursos/'
url_base_avaliacoes= 'http://127.0.0.1:8000/api/v1/avaliacoes/'

curso_atualizado = {
    "titulo": "Novo curso de ReactJS",
    "url": "https://www.udemy.com/course/criando-apis-rest-com-django-rest-framework-essencial/"
}

resultado = requests.put(url=f'{url_base_cursos}7/', headers=headers, data=curso_atualizado)

# Testando o código de status HTTP
assert resultado.status_code == 200

# Testando o título
assert resultado.json()['titulo'] == curso_atualizado['titulo']