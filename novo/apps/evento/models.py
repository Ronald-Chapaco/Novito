from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Rubro(models.Model):
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nombre


class Pais(models.Model):
    nombre = models.CharField(max_length=20)

    def __unicode__(self):
        return self.nombre

    class Meta:
#        verbose_name = ''
        verbose_name_plural = "Paises"


class Provincia(models.Model):
    nombre = models.CharField(max_length=20)
    pais = models.ForeignKey(Pais)

    def __unicode__(self):
        return '{0}, {1}'.format(self.nombre, self.pais.__unicode__())


class Localidad(models.Model):
    nombre = models.CharField(max_length=20)
    provincia = models.ForeignKey(Provincia)

    def __unicode__(self):
        return '{0}, {1}'.format(self.nombre, self.provincia.__unicode__())

    class Meta:
#        verbose_name = ''
        verbose_name_plural = "Localidades"



class Localizacion(models.Model):
    barrio = models.CharField(max_length=20)
    calle = models.CharField(max_length=20)
    numero = models.IntegerField()
    numero_local = models.IntegerField()
    localidad = models.ForeignKey(Localidad)

    def __unicode__(self):
        return '{0} {1} {2}, {3} '.format(self.barrio, self.calle, self.numero,
            self.localidad.__unicode__())

    class Meta:
#        verbose_name = ''
        verbose_name_plural = "Localizaciones"




class TipoEvento(models.Model):
    nombre = models.CharField(max_length=30)

    def __unicode__(self):
        return self.nombre


class Evento(models.Model):
    invitados = models.ManyToManyField(User, null=True, blank=True,
        related_name="eventos_invitado")
    nombre = models.CharField(default="Nombre", max_length=30)
    descripcion = models.TextField(max_length=300)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    fecha_creacion = models.DateField()
    localizacion = models.ForeignKey(Localizacion)
    creador = models.ForeignKey(User, related_name="eventos_creados")
    estado = models.CharField(default="noleido", max_length=30)
    tipo = models.ForeignKey(TipoEvento, default="", null=True, blank=True)
    imagen = models.ImageField(default='images/calendario-default.png',
        upload_to="eventos")

    def __unicode__(self):
        return self.descripcion

    def get_comments_evento(self):
        return EventoComment.objects.filter(evento=self)

class EventoComment(models.Model):
    evento = models.ForeignKey(Evento)
    comment = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)

    class Meta:
        verbose_name = _("Evento Comment")
        verbose_name_plural = _("Evento Comments")
        ordering = ("date",)

    def __unicode__(self):
        return u'{0} - {1}'.format(self.user.username, self.evento.descripcion)  


class TipoSector(models.Model):
    titulo = models.CharField(max_length=30)

    class Meta:
        verbose_name = "TipoSector"
        verbose_name_plural = "TipoSectors"

    def __unicode__(self):
        return self.titulo


class Rueda(models.Model):
    titulo = models.CharField(max_length=50)
    creador = models.ForeignKey(User, related_name="rudas_creados")
    tipo = models.ManyToManyField(TipoSector, null=True, blank=True,
        related_name="sectores")
    descripcion = models.TextField(max_length=500)
    fecha_creacion = models.DateField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    imagen = models.ImageField(default='images/calendario-default.png',
        upload_to="eventos")
    lugar = models.CharField(max_length=50)
    contacto = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=6, decimal_places=2)

    # TODO: Define fields here

    class Meta:
        verbose_name = "Rueda"
        verbose_name_plural = "Ruedas"

    def __unicode__(self):
        return self.titulo

    def get_comments_rueda(self):
        return RuedaComment.objects.filter(rueda=self)


class RuedaComment(models.Model):
    rueda = models.ForeignKey(Rueda)
    comment = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)

    class Meta:
        verbose_name = _("Rueda Comment")
        verbose_name_plural = _("Rueda Comments")
        ordering = ("date",)

    def __unicode__(self):
        return u'{0} - {1}'.format(self.user.username, self.rueda.descripcion) 

    # TODO: Define custom methods here
