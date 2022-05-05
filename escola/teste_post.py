import requests

headers = {'Authorization': 'Token ba987131bf42c8df4447c789453ecd65b26ab1b0'}

url_base_cursos = 'http://127.0.0.1:8000/api/v1/cursos/'
url_base_avaliacoes= 'http://127.0.0.1:8000/api/v1/avaliacoes/'

resultado = requests.get(url=url_base_cursos, headers=headers)

novo_curso = {
    "titulo": "Web ReactJS",
    "url": "https://www.udemy.com/course/2"
}

resultado = requests.post(url=url_base_cursos, headers=headers, data=novo_curso)

# Testando o código de status HTTP 201
assert resultado.status_code == 201

# Testando se o titulo do curso retornado é o mesmo do informado
assert resultado.json()['titulo'] == novo_curso['titulo']