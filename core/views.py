from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Arma, Municao, Calibre, ObjetoTipo, Objeto
from .serializers import ArmaSerializer, MunicaoSerializer, CalibreSerializer


class ArmaAPIView(APIView):

    @staticmethod
    def get(request):
        armas = Arma.objects.all()
        serializer = ArmaSerializer(armas, many=True)
        return Response(serializer.data)


class MunicaoAPIView(APIView):

    @staticmethod
    def get(request):
        municoes = Municao.objects.all()
        serializer = MunicaoSerializer(municoes, many=True)
        return Response(serializer.data)
