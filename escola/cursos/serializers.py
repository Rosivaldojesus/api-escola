from pyexpat import model
from rest_framework import serializers

from .models import Curso, Avaliacao

class AvaliacaoSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Avaliacao
        fields = (
            'id', 'curso', 'nome', 'email', 'comentario', 'avaliacao', 'criacao', 'ativo'
        )




class CursoSerializer(serializers.ModelSerializer):

    # Nasted Relationship
    # avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

    # HyperlinkedRelatedField
    avaliacoes = serializers.HyperlinkedRelatedField(many=True, view_name='avaliacao-detail', read_only=True)

    class Meta:
        model = Curso
        fields = (
            'id', 'titulo', 'url', 'criacao', 'ativo', 'avaliacoes'
        )