from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import *

router = SimpleRouter()
router.register('armas', ArmasAPIView)
router.register('municoes', MunicoesAPIView)
router.register('calibres', CalibresAPIView)
router.register('objetos_tipo', ObjTiposAPIView)

urlpatterns = [
    path('objetos/', ObjCodAPIView.as_view(), name='objetos'),

]
