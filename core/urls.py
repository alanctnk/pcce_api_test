from django.urls import path

from .views import *

urlpatterns = [
    path('armas/', ArmasAPIView.as_view(), name='armas'),
    path('calibres/', CalibresAPIView.as_view(), name='calibres'),
    path('municoes/', MunicoesAPIView.as_view(), name='municoes'),
    path('objetos_tipo/', ObjTiposAPIView.as_view(), name='objetos_tipo'),
    path('objetos/', ObjCodAPIView.as_view(), name='objetos'),
    path('armas/<int:pk>', ArmaPIView.as_view(), name='arma'),
    path('municoes/<int:pk>', MunicaoAPIView.as_view(), name='municao'),
    path('calibres/<int:pk>', CalibreAPIView.as_view(), name='calibre'),
    path('objetos_tipo/<int:pk>', ObjTipoAPIView, name='objeto_tipo')
]