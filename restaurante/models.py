from django.db import models
from django.contrib import admin
from django.core.validators import MaxValueValidator, MinValueValidator

#alumnos
class Menu(models.Model):
    nombre  =   models.CharField(max_length=130)
    precio = models.IntegerField()
    Fecha_Ingreso = models.DateTimeField(blank=True, null=True)
    Estados = (
	    ('Activo', 'Activo'),
	    ('Inactivo', 'Inactivo'),
	    )
    Estado = models.CharField(
	    max_length=10,
	    choices=Estados,
	    default='Activo',
	    )
    def publish(self):
    	self.Fecha_Ingreso = timezone.now()
    	self.save()

    def __str__(self):
        return self.nombre

class Plato(models.Model):
    nombre  =   models.CharField(max_length=130)
    Estados = (
	    ('Activo', 'Activo'),
	    ('Inactivo', 'Inactivo'),
	    )
    estado = models.CharField(
	    max_length=10,
	    choices=Estados,
	    default='Activo',
	    )
    Fecha_Ingreso = models.DateTimeField(blank=True, null=True)

    def publish(self):
    	self.Fecha_Ingreso = timezone.now()
    	self.save()

    def __str__(self):
        return '%s' % (self.nombre)

class Cliente(models.Model):
    Creado = models.ForeignKey('auth.User', on_delete=models.CASCADE,blank=True, null=True)
    Codigo = models.CharField(max_length=200,null=True,blank=True, unique =True)
    Primer_Nombre = models.CharField(max_length=200,)
    Primer_Apellido = models.CharField(max_length=200,blank=True, null=True)
    HOMBRE = 'Hombre'
    MUJER = 'Mujer'
    GENEROS = (
        (HOMBRE, 'Hombre'),
        (MUJER, 'Mujer'),
    )
    Genero = models.CharField(
        max_length=7,
        choices=GENEROS,
        default=HOMBRE,
    )
    nacimiento = models.DateField(
           blank=False, null=False)
    direccion = models.CharField(max_length=200, blank=True, null=True)
    telefono = models.CharField(max_length=200, blank=True, null=True)
    telefono2 = models.CharField(max_length=200, blank=True, null=True)
    Estados = (
    ('Activo', 'Activo'),
    ('Inactivo', 'Inactivo'),
    ('PendienteExamen', 'Pendiente De Examen'),
    ('PendienteInscripcion', 'Pendiente De Inscripcion'),
    )
    estado = models.CharField(
        max_length=20,
        choices=Estados,
        default='Inactivo',
    )
    fechaingreso = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.fechaingreso = timezone.now()
        self.save()

    def __str__(self):
        return '%s %s %s %s %s %s' % (self.Codigo,self.Primer_Nombre, self.Primer_Apellido)

class Encargado(models.Model):
    Nombres = models.CharField(max_length=200)
    Apellidos = models.CharField(max_length=200)
    telefono_celular = models.CharField(max_length=200, blank=True, null=True)
    direccion = models.CharField(max_length=200)
    telefono_casa = models.CharField(max_length=200, blank=True, null=True)
    Trabajo = models.CharField(max_length=200, blank=True, null=True)
    telefono_trabajo = models.CharField(max_length=200, blank=True, null=True)
    Dpi = models.CharField(max_length=200, blank=True, null=True)
    Estados = (
    ('Activo', 'Activo'),
    ('Inactivo', 'Inactivo'),
    )
    estado = models.CharField(
        max_length=20,
        choices=Estados,
        default='Inactivo',
    )
    fechaingreso = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.fechaingreso = timezone.now()
        self.save()

    def __str__(self):
        return '%s %s' % (self.Nombres, self.Apellidos)


class Asignacion(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    plato = models.ForeignKey(Plato, on_delete=models.CASCADE)
    def __str__(self):
        return '%s %s %s' % (self.menu, self.plato, self.boleta)



class PersonalOperativo(models.Model):
    Primer_Nombre = models.CharField(max_length=200)
    Primer_Apellido = models.CharField(max_length=200)
    Telefono_Casa = models.CharField(max_length=200, blank=True, null=True)
    Direccion = models.CharField(max_length=128)
    Dpi = models.CharField(max_length=20)
    Tipos = (
    ('Soltero', 'Soltero'),
    ('Casado', 'Casado'),
    ('Viudo', 'Viudo'),
    ('Divorsiado', 'Divorsiado'),
    )
    Estado_Civil = models.CharField(
        max_length=20,
        choices=Tipos,
        default='Soltero',
    )
    Fecha_Nacimiento = models.DateField(
        blank=True, null=True)
    Lugar_Nacimiento = models.CharField(max_length=128)
    Nit = models.CharField(max_length=20)
    Igss = models.CharField(max_length=30)
    Fecha_Inicio_Labores = models.DateField(
        blank=True, null=True)
    Nivel_Academico = models.CharField(max_length=50)
    Titulo = models.CharField(max_length=50)
    Salario = models.CharField(max_length=50)
    Hora_Entrada = models.TimeField(blank=True, null=True)
    Hora_Salida = models.TimeField(blank=True, null=True)
    fechaingreso = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.fechaingreso = timezone.now()
        self.save()

    def __str__(self):
        return '%s %s' % (self.Primer_Nombre, self.Primer_Apellido)
