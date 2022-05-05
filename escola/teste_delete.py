import requests

headers = {'Authorization': 'Token ba987131bf42c8df4447c789453ecd65b26ab1b0'}

url_base_cursos = 'http://127.0.0.1:8000/api/v1/cursos/'
url_base_avaliacoes= 'http://127.0.0.1:8000/api/v1/avaliacoes/'


resultado = requests.delete(url=f'{url_base_cursos}6/', headers=headers)

# Testando o código HTTP
assert resultado.status_code == 204

# Testando se o tamanho do conteúdo é 0
assert len(resultado.text) == 0
