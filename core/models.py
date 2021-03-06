from django.db import models
from django.db.models.signals import post_save


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
    calibre = models.ForeignKey(Calibre, related_name='armas', on_delete=models.CASCADE, null=True)
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
    calibre = models.ForeignKey(Calibre, related_name='munições', on_delete=models.CASCADE, null=True)
    marca = models.CharField(max_length=64)
    modelo = models.CharField(max_length=64)
    valor_estimado = models.FloatField()

    class Meta:
        verbose_name = "Munição"
        verbose_name_plural = "Munições"

    def __str__(self):
        return f"{self.marca} model {self.modelo}"


class Objeto(models.Model):
    objeto_tipo = models.ForeignKey(ObjetoTipo, related_name='objetos', on_delete=models.CASCADE)

    def __str__(self):
        return f"Objeto cod. {self.objeto_tipo}"


def save_objeto(sender, instance, created, **kwargs):
    obj = sender.objects.latest('id')
    if created:
        Objeto.objects.create(objeto_tipo=obj)


post_save.connect(save_objeto, sender=ObjetoTipo)
