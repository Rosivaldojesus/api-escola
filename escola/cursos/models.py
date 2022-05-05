from django.db import models

# Create your models here.

class Base(models.Model):
    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True

class Curso(Base):
    titulo = models.CharField(max_length=255)
    url = models.URLField(unique=True)

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['-id']

    def __str__(self) -> str:
        return self.titulo

class Avaliacao(Base):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='avaliacoes')
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    comentario = models.TextField()
    avaliacao = models.DecimalField(max_digits=2, decimal_places=1)

    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'
        unique_together = ['email', 'curso']
        ordering = ['-id']

    def __str__(self) -> str:
        return f'{self.nome} avaliou o curso {self.curso} com nota {self.avaliacao}'



