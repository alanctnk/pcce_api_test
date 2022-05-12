from rest_framework import serializers

from .models import Arma, Calibre, Municao, ObjetoTipo, Objeto


class ArmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arma
        fields = (
            'id',
            'marca',
            'modelo',
            'calibre_id',
            'quantidade_de_tiros',
            'valor_estimado'
        )


class MunicaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Municao
        fields = (
            'id',
            'marca',
            'modelo',
            'calibre_id'
        )


class CalibreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calibre
        fields = (
            'desc_calibre',
        )
