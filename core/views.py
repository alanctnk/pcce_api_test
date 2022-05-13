from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Arma, Municao, Calibre, ObjetoTipo, Objeto
from .serializers import ArmaSerializer, MunicaoSerializer, CalibreSerializer, ObjTipoSerializer, ObjetoSerializer


class ArmasAPIView(viewsets.ModelViewSet):
    queryset = Arma.objects.all()
    serializer_class = ArmaSerializer


class MunicoesAPIView(viewsets.ModelViewSet):
    queryset = Municao.objects.all()
    serializer_class = MunicaoSerializer


class CalibresAPIView(viewsets.ModelViewSet):
    queryset = Calibre.objects.all()
    serializer_class = CalibreSerializer


class ObjTiposAPIView(viewsets.ModelViewSet):
    queryset = ObjetoTipo.objects.all()
    serializer_class = ObjTipoSerializer


class ObjCodAPIView(APIView):
    @staticmethod
    def get(request):
        objeto = Objeto.objects.all()
        serializer = ObjetoSerializer(objeto, many=True)
        return Response(serializer.data)
