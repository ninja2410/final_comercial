# Generated by Django 2.0.9 on 2018-11-21 23:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Asignacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Boleta', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Codigo', models.CharField(blank=True, max_length=200, null=True, unique=True)),
                ('Primer_Nombre', models.CharField(max_length=200)),
                ('Primer_Apellido', models.CharField(blank=True, max_length=200, null=True)),
                ('Genero', models.CharField(choices=[('Hombre', 'Hombre'), ('Mujer', 'Mujer')], default='Hombre', max_length=7)),
                ('nacimiento', models.DateField()),
                ('direccion', models.CharField(blank=True, max_length=200, null=True)),
                ('telefono', models.CharField(blank=True, max_length=200, null=True)),
                ('telefono2', models.CharField(blank=True, max_length=200, null=True)),
                ('estado', models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo'), ('PendienteExamen', 'Pendiente De Examen'), ('PendienteInscripcion', 'Pendiente De Inscripcion')], default='Inactivo', max_length=20)),
                ('fechaingreso', models.DateTimeField(blank=True, null=True)),
                ('Creado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Encargado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombres', models.CharField(max_length=200)),
                ('Apellidos', models.CharField(max_length=200)),
                ('telefono_celular', models.CharField(blank=True, max_length=200, null=True)),
                ('direccion', models.CharField(max_length=200)),
                ('telefono_casa', models.CharField(blank=True, max_length=200, null=True)),
                ('Trabajo', models.CharField(blank=True, max_length=200, null=True)),
                ('telefono_trabajo', models.CharField(blank=True, max_length=200, null=True)),
                ('Dpi', models.CharField(blank=True, max_length=200, null=True)),
                ('estado', models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], default='Inactivo', max_length=20)),
                ('fechaingreso', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=130)),
                ('precio', models.IntegerField()),
                ('Fecha_Ingreso', models.DateTimeField(blank=True, null=True)),
                ('Estado', models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], default='Activo', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='PersonalOperativo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Primer_Nombre', models.CharField(max_length=200)),
                ('Segundo_Nombre', models.CharField(default='N/A', max_length=200)),
                ('Primer_Apellido', models.CharField(max_length=200)),
                ('Segundo_Apellido', models.CharField(default='N/A', max_length=200)),
                ('Telefono_Casa', models.CharField(blank=True, max_length=200, null=True)),
                ('Telefono_Celular', models.CharField(blank=True, max_length=200, null=True)),
                ('Direccion', models.CharField(max_length=128)),
                ('Dpi', models.CharField(max_length=20)),
                ('Estado_Civil', models.CharField(choices=[('Soltero', 'Soltero'), ('Casado', 'Casado'), ('Viudo', 'Viudo'), ('Divorsiado', 'Divorsiado')], default='Soltero', max_length=20)),
                ('Fecha_Nacimiento', models.DateField(blank=True, null=True)),
                ('Lugar_Nacimiento', models.CharField(max_length=128)),
                ('No_Hijos', models.CharField(choices=[('sin', 'Sin Hijos'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('mas', 'Mas de 5...')], default='sin', max_length=20)),
                ('Nit', models.CharField(max_length=20)),
                ('Igss', models.CharField(max_length=30)),
                ('Fecha_Inicio_Labores', models.DateField(blank=True, null=True)),
                ('Nivel_Academico', models.CharField(max_length=50)),
                ('Titulo', models.CharField(max_length=50)),
                ('Salario', models.CharField(max_length=50)),
                ('Hora_Entrada', models.TimeField(blank=True, null=True)),
                ('Hora_Salida', models.TimeField(blank=True, null=True)),
                ('fechaingreso', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Plato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=130)),
                ('Estado', models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], default='Activo', max_length=10)),
                ('Fecha_Ingreso', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='asignacion',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurante.Menu'),
        ),
        migrations.AddField(
            model_name='asignacion',
            name='plato',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurante.Plato'),
        ),
    ]