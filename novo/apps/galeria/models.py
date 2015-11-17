from django.db import models
from django.db.models.signals import post_delete
from django.core.urlresolvers import reverse
from django.dispatch import receiver
from django.contrib.auth.models import User



class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __unicode__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('cat-album')    


class Fotos(models.Model):
    """ Fotos del album """

    categoria = models.ForeignKey(Categoria, null=True, blank=True)
    titulo = models.CharField(max_length=50, default='No title')
    foto = models.ImageField(upload_to='Galeria/')
    fecha = models.DateField(auto_now_add=True)
    favorito = models.BooleanField(default=False)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('lista-fotos')


@receiver(post_delete, sender=Fotos)
def foto_delete(sender, instance, **kwargs):
    """ Borra los ficheros de las fotos que se eliminan. """
    instance.foto.delete(False)

class Comentario(models.Model):
    foto = models.ForeignKey(Fotos)
    contenido = models.TextField()
    fecha = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.contenido

    def get_absolute_url(self):
        return reverse('lista-fotos',args=[str(self.id)])
    