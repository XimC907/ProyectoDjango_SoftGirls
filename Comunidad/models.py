from django.db import models

# Create your models here.
class Iniciativa(models.Model):
    id_iniciativa = models.CharField(max_length=10, primary_key=True)
    nombre_iniciativa = models.CharField(max_length=100)
    descripcion_iniciativa = models.TextField()
    categoria_principal_iniciativa = models.CharField(max_length=20)
    mision_iniciativa = models.TextField()
    vision_iniciativa = models.TextField()
    fecha_inicio_iniciativa = models.DateField()
    universidad_origin_iniciativa = models.CharField(max_length=100)
    numero_estudiantes_iniciativa = models.IntegerField()
    logo_iniciativa = models.CharField(max_length=200)
    sitio_web_iniciativa = models.CharField(max_length=200)
    email_contacto_iniciativa = models.EmailField()

    def __str__(self):
        return str(self.id_iniciativa)

class Miembro(models.Model):
    id_miembro = models.CharField(max_length=10, primary_key=True)
    nombre_miembro = models.CharField(max_length=100)
    rol_miembro = models.CharField(max_length=20)
    ocupacion_cargo_miembro = models.CharField(100)
    info_miembro = models.TextField()
    foto_miembro = models.CharField(max_length=200)
    correo_miembro = models.CharField(max_length=200)
    id_iniciativa = models.ForeignKey(Iniciativa, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id_miembro)

class UbicacionSede(models.Model):
    id_ubicacion = models.CharField(max_length=10, primary_key=True)
    nombre_lugar_ubicacion = models.CharField(max_length=100)
    direccion_ubicacion = models.CharField(max_length=100)
    ciudad_origen_ubicacion = models.CharField(50)
    pais_origen_ubicacion = models.CharField(50)
    link_maps_ubicacion = models.CharField(200)
    id_iniciativa = models.ForeignKey(Iniciativa, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id_ubicacion)

class RedSocial(models.Model):
    id_red_social = models.CharField(max_length=10, primary_key=True)
    plataforma_red_social = models.CharField(max_length=20)
    url_red_social = models.CharField(max_length=200)
    id_iniciativa = models.ForeignKey(Iniciativa, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id_red_social)

class Evento(models.Model):
    id_evento = models.CharField(max_length=10, primary_key=True)
    nombre_evento = models.CharField(max_length=100)
    descripcion_evento = models.TextField()
    tipo_participacion_evento = models.CharField(max_length=20)
    ocupacion_cargo_miembro = models.CharField(100)
    fecha_inicio_evento = models.DateTimeField()
    fecha_fin_evento = models.DateTimeField()
    lugar_evento = models.CharField(max_length=100)
    pais_origen_evento = models.CharField(max_length=50)
    ciudad_origen_evento = models.CharField(max_length=50)
    id_iniciativa = models.ForeignKey(Iniciativa, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id_evento)

class GaleriaEvento(models.Model):
    id_galeria = models.CharField(max_length=10, primary_key=True)
    imagen_galeria = models.CharField(max_length=200)
    descripcion_galeria = models.CharField(max_length=100)
    id_evento = models.ForeignKey(Evento, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id_galeria)