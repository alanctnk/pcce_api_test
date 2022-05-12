from django.db import models


class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class ObjetoTipo(Base):
    tipo_de_objeto = models.CharField(max_length=64)

    def __str__(self):
        return self.tipo_de_objeto


class Calibre(Base):
    desc_calibre = models.CharField(max_length=64)

    def __str__(self):
        return self.desc_calibre


class Arma(Base):
    calibre_id = models.ForeignKey(Calibre, related_name='armas', on_delete=models.CASCADE)
    marca = models.CharField(max_length=64)
    modelo = models.CharField(max_length=64)
    quantidade_de_tiros = models.IntegerField()
    valor_estimado = models.FloatField()
    imagem = models.URLField(blank=True)

    class Meta:
        verbose_name = "Arma"
        verbose_name_plural = "Armas"

    def __str__(self):
        return f"{self.marca} model {self.modelo}"


class Municao(Base):
    calibre_id = models.ForeignKey(Calibre, related_name='munições', on_delete=models.CASCADE)
    marca = models.CharField(max_length=64)
    modelo = models.CharField(max_length=64)
    valor_estimado = models.FloatField()

    class Meta:
        verbose_name = "Munição"
        verbose_name_plural = "Munições"

    def __str__(self):
        return f"{self.marca} model {self.modelo}"


class Objeto(models.Model):
    objeto_tipo_id = models.ForeignKey(ObjetoTipo, related_name='objetos', on_delete=models.CASCADE)
