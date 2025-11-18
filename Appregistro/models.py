# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TipoUsuario(models.Model):
    tipo_de_usuario = models.CharField(max_length=100, db_comment='Aca se introduce el tipo del usuario ej: Administrador o externo')

    class Meta:
        db_table = 'Tipo_Usuario'


class Usuario(models.Model):
    nombre = models.CharField(max_length=100, db_comment='Aca se introduce el nombre del usuario')
    numero_identificacion = models.CharField(unique=True, max_length=100, db_comment='Aca se introduce el numero de identificaci¾n del usuario')
    correo = models.CharField(max_length=100, db_comment='Aca se introduce el correo del usuario')
    celular = models.CharField(max_length=20, blank=True, null=True, db_comment='Aca se introduce el celular del usuario')
    idtipo_usuario = models.ForeignKey(TipoUsuario, models.DO_NOTHING, db_column='idtipo_usuario', blank=True, null=True, db_comment='Esta es la llave foranea idTipo_usuario')

    class Meta:
        db_table = 'usuario'


class TipoVehiculo(models.Model):
    tipo_de_vehiculo = models.CharField(max_length=50, db_comment='Aca se introduce cual es el tipo de vehiculo ej: Carro o Moto')

    class Meta:
        db_table = 'tipo_vehiculo'


class Color(models.Model):
    color_vehiculo = models.CharField(max_length=50, db_comment='Aca se introduce el color del vehiculo ej: azul, rojo etc')

    class Meta:
        db_table = 'color'


class Marca(models.Model):
    marca_vehiculo = models.CharField(max_length=50, db_comment='Aca va la marca de la que es el vehiculo ej: Chevrolet, Pulsar etc')

    class Meta:
        db_table = 'marca'


class Modelo(models.Model):
    modelo_vehiculo = models.CharField(max_length=50, db_comment='Aca iria el modelo del cual es la marca del vehiculo ej: spark gt, ns200 etc')
    idmarca = models.ForeignKey(Marca, models.DO_NOTHING, db_column='idmarca', blank=True, null=True)

    class Meta:
        db_table = 'modelo'


class EstadoEspacio(models.Model):
    estado_espacio_parqueo = models.CharField(max_length=50, db_comment='Aca apareceria el estado del espacio en el cual esta el vehiculo el cual podra ser libre u ocupado')

    class Meta:
        db_table = 'estado_espacio'


class Tarifa(models.Model):
    valor_hora = models.DecimalField(max_digits=10, decimal_places=2, db_comment='Aca iria el valor de la hora teniendo en cuenta el tipo de vehiculo')
    idtipo_vehiculo = models.ForeignKey(TipoVehiculo, models.DO_NOTHING, db_column='idtipo_vehiculo', blank=True, null=True, db_comment='Esta es la llave foranea idtipo_vehiculo')

    class Meta:
        db_table = 'tarifa'


class Vehiculo(models.Model):
    placa = models.CharField(unique=True, max_length=20, db_comment='Aca iria la placa de cada vehiculo')
    idtipo_vehiculo = models.ForeignKey(TipoVehiculo, models.DO_NOTHING, db_column='idtipo_vehiculo', blank=True, null=True, db_comment='Esta es la llave foranea idtipo_vehiculo')
    idcolor = models.ForeignKey(Color, models.DO_NOTHING, db_column='idcolor', blank=True, null=True, db_comment='Esta es la llave foranea idcolor')
    idmarca = models.ForeignKey(Marca, models.DO_NOTHING, db_column='idmarca', blank=True, null=True, db_comment='Esta es la llave foranea idmarca')
    idusuario = models.ForeignKey(Usuario, models.DO_NOTHING, db_column='idusuario', blank=True, null=True, db_comment='Esta es la llave foranea idusuario')

    class Meta:
        db_table = 'vehiculo'
        db_table_comment = 'esta tabla es de muchos con muchos'


class Espacio(models.Model):
    idestado_espacio = models.ForeignKey(EstadoEspacio, models.DO_NOTHING, db_column='idestado_espacio', blank=True, null=True)
    codigo = models.CharField(unique=True, max_length=20, db_comment='Es el codigo del espacio, cada espacio tiene un codigo distinto')

    class Meta:
        db_table = 'espacio'


class Registro(models.Model):
    idvehiculo = models.IntegerField(blank=True, null=True)
    idespacio = models.ForeignKey(Espacio, models.DO_NOTHING, db_column='idespacio', blank=True, null=True)
    fecha_ingreso = models.DateField(db_comment='Aca iria la fecha en la que el vehiculo ingreso al parqueadero ')
    hora_ingreso = models.TimeField(db_comment='Aca iria la hora en la que ingreso el vehiculo al parqueadero')
    fecha_salida = models.DateField(db_comment='Aca va la fecha en la que el vehiculo salio del parqueadero')
    hora_salida = models.TimeField(db_comment='Aca va la hora exacta en la que el vehiculo salio del parqueadero')

    class Meta:
        db_table = 'registro'


class Pago(models.Model):
    idregistro = models.ForeignKey(Registro, models.DO_NOTHING, db_column='idregistro', blank=True, null=True)
    idtarifa = models.ForeignKey(Tarifa, models.DO_NOTHING, db_column='idtarifa', blank=True, null=True)
    monto_pago = models.DecimalField(max_digits=10, decimal_places=2, db_comment='Aca va el monto de pago total')
    fecha_pago = models.DateTimeField(db_comment='Esta es la fecha en la que el usuario realizo el pago')

    class Meta:
        db_table = 'pago'
