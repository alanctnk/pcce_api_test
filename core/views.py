from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Arma, Municao, Calibre, ObjetoTipo, Objeto
from .serializers import ArmaSerializer, MunicaoSerializer, CalibreSerializer, ObjTipoSreializer, ObjetoSerializer


class ArmasAPIView(generics.ListCreateAPIView):
    queryset = Arma.objects.all()
    serializer_class = ArmaSerializer


class ArmaPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Arma.objects.all()
    serializer_class = ArmaSerializer


class MunicoesAPIView(generics.ListCreateAPIView):
    queryset = Municao.objects.all()
    serializer_class = MunicaoSerializer


class MunicaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Municao.objects.all()
    serializer_class = MunicaoSerializer


class CalibresAPIView(generics.ListCreateAPIView):
    queryset = Calibre.objects.all()
    serializer_class = CalibreSerializer


class CalibreAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Calibre.objects.all()
    serializer_class = CalibreSerializer


class ObjTiposAPIView(generics.ListCreateAPIView):
    queryset = ObjetoTipo.objects.all()
    serializer_class = ObjTipoSreializer


class ObjTipoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ObjetoTipo.objects.all()
    serializer_class = ObjTipoSreializer


class ObjCodAPIView(APIView):
    @staticmethod
    def get():
        objeto = Objeto.objects.all()
        serializer = ObjetoSerializer(objeto, many=True)
        return Response(serializer.data)
