import requests

class TesteCursos:

    headers = {'Authorization': 'Token ba987131bf42c8df4447c789453ecd65b26ab1b0'}
    url_base_cursos = 'http://127.0.0.1:8000/api/v1/cursos/'

    def test_get_cursos(self):
        cursos = requests.get(url=self.url_base_cursos, headers=self.headers)
        assert cursos.status_code == 200
    
    def test_get_curso(self):
        curso = requests.get(url=f'{self.url_base_cursos}7/', headers=self.headers)
        assert curso.status_code == 200

    def test_put_curso(self):

        dados = {
            "titulo": "Curso de TypeScript",
            "url": "https://www.udemy.com/course/criando-apis-rest-com-django-rest-framework-essencial/learn/lecture/17829044#overview"
        }

        atualizar = requests.put(url=f'{self.url_base_cursos}7/', headers=self.headers, data=dados)

        assert atualizar.status_code == 200


    def test_put_titulo_curso(self):
    
        dados = {
            "titulo": "Curso de TypeScripts",
            "url": "https://www.udemy.com/courses/criando-apis-rest-com-django-rest-framework-essencial/learn/lecture/17829044#overview"
        }

        atualizar = requests.put(url=f'{self.url_base_cursos}7/', headers=self.headers, data=dados)

        assert atualizar.json()['titulo'] == atualizar['titulo']

    def test_detele_curso(self):

        dados = requests.put(url=f'{self.url_base_cursos}5/', headers=self.headers)
        assert dados.status_code == 204
        assert len(dados.text) == 0

