from django.db import models


class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class ObjetoTipo(Base):
    tipo_de_objeto = models.CharField(max_length=64)


class Calibre(Base):
    desc_calibre: models.CharField(max_length=45)


class Arma(Base):
    calibre_id = models.ForeignKey(Calibre, related_name='armas', on_delete=models.CASCADE)
    marca = models.CharField(max_length=64)
    modelo = models.CharField(max_length=64)
    quantidade_de_tiros = models.IntegerField()
    valor_estimado = models.FloatField()
    imagem = models.URLField()


class Municao(Base):
    calibre_id = models.ForeignKey(Calibre, related_name='armas', on_delete=models.CASCADE)
    marca = models.CharField(max_length=64)
    modelo = models.CharField(max_length=64)
    valor_estimado = models.FloatField()


class Objeto(models.Model):
    objeto_tipo_id = models.ForeignKey(ObjetoTipo, related_name='objetos', on_delete=models.CASCADE)
