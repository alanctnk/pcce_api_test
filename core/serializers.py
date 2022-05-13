from rest_framework import serializers

from .models import Arma, Calibre, Municao, ObjetoTipo, Objeto


class ObjetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Objeto
        fields = (
            'id',
            'objeto_tipo'
        )


class ObjTipoSreializer(serializers.ModelSerializer):
    class Meta:
        model = ObjetoTipo
        fields = (
            'id',
            'tipo_de_objeto'
        )


class ArmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arma
        fields = (
            'id',
            'marca',
            'modelo',
            'calibre',
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
            'valor_estimado',
            'calibre'
        )


class CalibreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calibre
        fields = (
            'id',
            'desc_calibre',
        )
