# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Actividad(models.Model):
    actividad_id = models.CharField(primary_key=True, max_length=45)
    actividad_uuid = models.IntegerField()
    actividad_nombre = models.CharField(max_length=100)
    actividad_level = models.IntegerField(blank=True, null=True)
    actividad_wbs = models.CharField(max_length=100, blank=True, null=True)
    proyecto = models.ForeignKey('Proyecto', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'actividad'


class Categoria(models.Model):
    categoria_id = models.AutoField(primary_key=True)
    categoria_nombre = models.CharField(max_length=45, blank=True, null=True)
    categoria_descripcion = models.TextField(blank=True, null=True)
    categoria_default = models.IntegerField()
    categoria_uid = models.BigIntegerField(unique=True, blank=True, null=True)
    rbs = models.ForeignKey('Rbs', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'categoria'


class Gerente(models.Model):
    gerente_id = models.AutoField(primary_key=True)
    gerente_nombre = models.CharField(max_length=100, blank=True, null=True)
    gerente_usuario = models.CharField(unique=True, max_length=45)
    gerente_correo = models.CharField(max_length=100, blank=True, null=True)
    gerente_fecha_creacion = models.DateTimeField(blank=True, null=True)
    gerente_correo_institucional = models.CharField(max_length=100, blank=True, null=True)
    gerente_profesion = models.CharField(max_length=100, blank=True, null=True)
    gerente_empresa = models.CharField(max_length=100, blank=True, null=True)
    gerente_metodologias = models.TextField(blank=True, null=True)
    gerente_certificaciones = models.TextField(blank=True, null=True)
    sector = models.ForeignKey('Sector', models.DO_NOTHING)
    pais = models.ForeignKey('Pais', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'gerente'


class Pais(models.Model):
    pais_id = models.AutoField(primary_key=True)
    pais_nombre = models.CharField(max_length=100, blank=True, null=True)
    pais_name = models.CharField(max_length=100)
    pais_nom = models.CharField(max_length=100)
    pais_iso_2 = models.CharField(max_length=45, blank=True, null=True)
    pais_iso_3 = models.CharField(max_length=45, blank=True, null=True)
    pais_phone_code = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pais'


class Proyecto(models.Model):
    proyecto_id = models.AutoField(primary_key=True)
    proyecto_nombre = models.CharField(max_length=100)
    proyecto_objetivo = models.TextField(blank=True, null=True)
    proyecto_alcance = models.TextField(blank=True, null=True)
    proyecto_descripcion = models.TextField(blank=True, null=True)
    proyecto_presupuesto = models.FloatField(blank=True, null=True)
    proyecto_fecha_inicio = models.DateField(blank=True, null=True)
    proyecto_fecha_finl = models.DateField(blank=True, null=True)
    proyecto_evaluacion_general = models.TextField(blank=True, null=True)
    proyecto_evaluacion = models.IntegerField(blank=True, null=True)
    proyecto_rbs_status = models.IntegerField()
    gerente = models.ForeignKey(Gerente, models.DO_NOTHING)
    sector = models.ForeignKey('Sector', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'proyecto'


class ProyectoHasRiesgo(models.Model):
    proyecto_has_riesgo_id = models.AutoField(primary_key=True)
    proyecto = models.ForeignKey(Proyecto, models.DO_NOTHING)
    riesgo = models.ForeignKey('Riesgo', models.DO_NOTHING)
    responsable = models.ForeignKey('Responsble', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proyecto_has_riesgo'


class ProyectoHasRiesgoActividad(models.Model):
    proyecto_has_riesgo_actividad_id = models.AutoField(primary_key=True)
    proyecto_has_riesgo = models.ForeignKey(ProyectoHasRiesgo, models.DO_NOTHING)
    actividad = models.ForeignKey(Actividad, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'proyecto_has_riesgo_actividad'


class Rbs(models.Model):
    rbs_id = models.AutoField(primary_key=True)
    rbs_default = models.IntegerField()
    gerente = models.OneToOneField(Gerente, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'rbs'


class Recurso(models.Model):
    recurso_id = models.AutoField(primary_key=True)
    recurso_nombre = models.CharField(max_length=45, blank=True, null=True)
    recurso_costo = models.FloatField(blank=True, null=True)
    proyecto = models.ForeignKey(Proyecto, models.DO_NOTHING)
    tipo_recurso = models.ForeignKey('TipoRecurso', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'recurso'


class Responsble(models.Model):
    responsable_id = models.AutoField(primary_key=True)
    responsble_nombre = models.CharField(max_length=100)
    responsble_descripcion = models.TextField(blank=True, null=True)
    proyecto = models.ForeignKey(Proyecto, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'responsble'


class Respuesta(models.Model):
    respuesta_id = models.AutoField(primary_key=True)
    respuesta_nombre = models.CharField(max_length=45, blank=True, null=True)
    respuesta_descripcion = models.TextField(blank=True, null=True)
    respuesta_costo = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'respuesta'


class Riesgo(models.Model):
    riesgo_id = models.AutoField(primary_key=True)
    riesgo_nombre = models.CharField(max_length=45, blank=True, null=True)
    riesgo_causa = models.TextField(blank=True, null=True)
    riesgo_evento = models.TextField(blank=True, null=True)
    riesgo_efecto = models.TextField(blank=True, null=True)
    riesgo_tipo = models.IntegerField(blank=True, null=True)
    riesgo_prom_evaluacion = models.FloatField(blank=True, null=True)
    riesgo_privacidad = models.IntegerField()
    riesgo_uid = models.BigIntegerField(unique=True, blank=True, null=True)
    sub_categoria = models.ForeignKey('SubCategoria', models.DO_NOTHING)
    riesgo_is_proyecto = int()

    class Meta:
        managed = False
        db_table = 'riesgo'


class RiesgoHasRespuesta(models.Model):
    riesgo_has_respuesta_id = models.AutoField(primary_key=True)
    riesgo = models.ForeignKey(Riesgo, models.DO_NOTHING)
    respuesta = models.ForeignKey(Respuesta, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'riesgo_has_respuesta'
        unique_together = (('riesgo', 'respuesta'),)


class Sector(models.Model):
    sector_id = models.AutoField(primary_key=True)
    sector_nombre = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'sector'


class SubCategoria(models.Model):
    sub_categoria_id = models.AutoField(primary_key=True)
    sub_categoria_nombre = models.CharField(max_length=45, blank=True, null=True)
    sub_categoria_descripcion = models.TextField(blank=True, null=True)
    sub_categoria_default = models.IntegerField()
    sub_categoria_uid = models.BigIntegerField(unique=True, blank=True, null=True)
    categoria = models.ForeignKey(Categoria, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sub_categoria'


class TipoRecurso(models.Model):
    tipo_recurso_id = models.AutoField(primary_key=True)
    tipo_recurso_nombre = models.CharField(max_length=45)
    tipo_recurso_descripcion = models.TextField(blank=True, null=True)
    gerente = models.ForeignKey(Gerente, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'tipo_recurso'

class ProyectoHasRiesgoRespuesta(models.Model):
    proyecto_has = models.OneToOneField('ProyectoHasRiesgo', models.DO_NOTHING, primary_key=True)
    respuesta_has = models.ForeignKey('RiesgoHasRespuesta', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'proyecto_has riesgo_respuesta'
        unique_together = (('proyecto_has', 'respuesta_has'),)



"""
class Actividad(models.Model):
    actividad_uuid = models.IntegerField()
    actividad_nombre = models.CharField(max_length=100)
    actividad_level = models.IntegerField(blank=True, null=True)
    actividad_wbs = models.CharField(max_length=100, blank=True, null=True)
    proyecto = models.ForeignKey('Proyecto', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'actividad'
        unique_together = (('actividad_uuid', 'proyecto'),)



class Categoria(models.Model):
    categoria_id = models.AutoField(primary_key=True)
    categoria_nombre = models.CharField(max_length=45, blank=True, null=True)
    categoria_descripcion = models.TextField(blank=True, null=True)
    categoria_uid = models.BigIntegerField(unique=True)
    rbs = models.ForeignKey('Rbs', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'categoria'


class Gerente(models.Model):
    gerente_id = models.AutoField(primary_key=True)
    gerente_nombre = models.CharField(max_length=100, blank=True, null=True)
    gerente_usuario = models.CharField(unique=True, max_length=45)
    gerente_correo = models.CharField(max_length=100, blank=True, null=True)
    gerente_fecha_creacion = models.DateTimeField(blank=True, null=True)
    gerente_correo_institucional = models.CharField(max_length=100, blank=True, null=True)
    gerente_profesion = models.CharField(max_length=100, blank=True, null=True)
    gerente_empresa = models.CharField(max_length=100, blank=True, null=True)
    gerente_metodologias = models.TextField(blank=True, null=True)
    gerente_certificaciones = models.TextField(blank=True, null=True)
    sector = models.ForeignKey('Sector', models.DO_NOTHING)
    pais = models.ForeignKey('Pais', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'gerente'


class Pais(models.Model):
    pais_id = models.AutoField(primary_key=True)
    pais_nombre = models.CharField(max_length=100, blank=True, null=True)
    pais_name = models.CharField(max_length=100)
    pais_nom = models.CharField(max_length=100)
    pais_iso_2 = models.CharField(max_length=45, blank=True, null=True)
    pais_iso_3 = models.CharField(max_length=45, blank=True, null=True)
    pais_phone_code = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pais'
        

class Proyecto(models.Model):
    proyecto_id = models.AutoField(primary_key=True)
    proyecto_nombre = models.CharField(max_length=100)
    proyecto_objetivo = models.TextField(blank=True, null=True)
    proyecto_alcance = models.TextField(blank=True, null=True)
    proyecto_descripcion = models.TextField(blank=True, null=True)
    proyecto_presupuesto = models.FloatField(blank=True, null=True)
    proyecto_fecha_inicio = models.DateField(blank=True, null=True)
    proyecto_fecha_finl = models.DateField(blank=True, null=True)
    proyecto_evaluacion_general = models.TextField(blank=True, null=True)
    proyecto_evaluacion = models.IntegerField(blank=True, null=True)
    proyecto_rbs_status = models.IntegerField()
    gerente = models.ForeignKey(Gerente, models.DO_NOTHING)
    sector = models.ForeignKey('Sector', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'proyecto'

class ProyectoHasRiesgo(models.Model):
    proyecto = models.OneToOneField(Proyecto, models.DO_NOTHING, primary_key=True)
    riesgo = models.ForeignKey('Riesgo', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'proyecto_has_riesgo'
        unique_together = (('proyecto', 'riesgo'),)


class Rbs(models.Model):
    rbs_id = models.AutoField(primary_key=True)
    rbs_default = models.IntegerField()
    gerente = models.OneToOneField(Gerente, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'rbs'



class Recurso(models.Model):
    recurso_id = models.AutoField(primary_key=True)
    recurso_nombre = models.CharField(max_length=45, blank=True, null=True)
    recurso_costo = models.FloatField(blank=True, null=True)
    proyecto = models.ForeignKey(Proyecto, models.DO_NOTHING)
    tipo_recurso = models.ForeignKey('TipoRecurso', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'recurso'


class Respuesta(models.Model):
    respuesta_id = models.AutoField(primary_key=True)
    respuesta_nombre = models.CharField(max_length=45, blank=True, null=True)
    respuesta_descripcion = models.TextField(blank=True, null=True)
    respuesta_costo = models.FloatField(blank=True, null=True)
    

    class Meta:
        managed = False
        db_table = 'respuesta'


class RespuestaHasRecurso(models.Model):
    respuesta = models.ForeignKey(Respuesta, models.DO_NOTHING, primary_key=True)
    recurso = models.ForeignKey(Recurso, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'respuesta_has_recurso'
        unique_together = (('respuesta', 'recurso'),)


class Riesgo(models.Model):
    riesgo_id = models.AutoField(primary_key=True)
    riesgo_nombre = models.CharField(max_length=45, blank=True, null=True)
    riesgo_causa = models.TextField(blank=True, null=True)
    riesgo_evento = models.TextField(blank=True, null=True)
    riesgo_efecto = models.TextField(blank=True, null=True)
    riesgo_tipo = models.IntegerField(blank=True, null=True)
    riesgo_prom_evaluacion = models.FloatField(blank=True, null=True)
    riesgo_privacidad = models.IntegerField(blank=True, null=True)
    riesgo_uid = models.BigIntegerField(blank=True, null=False)
    sub_categoria = models.ForeignKey('SubCategoria', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'riesgo'


class RiesgoHasRespuesta(models.Model):
    class Meta:
        managed = False
        db_table = 'riesgo_has_respuesta'
        unique_together = (('riesgo', 'respuesta'),)

    riesgo = models.ForeignKey(Riesgo, models.DO_NOTHING, primary_key=True)
    respuesta = models.ForeignKey(Respuesta, models.DO_NOTHING)

    



class Sector(models.Model):
    sector_id = models.AutoField(primary_key=True)
    sector_nombre = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'sector'


class SubCategoria(models.Model):
    sub_categoria_id = models.AutoField(primary_key=True)
    sub_categoria_nombre = models.CharField(max_length=45, blank=True, null=True)
    sub_categoria_descripcion = models.TextField(blank=True, null=True)
    sub_categoria_uid = models.BigIntegerField(unique=True)
    categoria = models.ForeignKey(Categoria, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sub_categoria'


class TipoRecurso(models.Model):
    tipo_recurso_id = models.AutoField(primary_key=True)
    tipo_recurso_nombre = models.CharField(max_length=45)
    tipo_recurso_descripcion = models.TextField(blank=True, null=True)
    gerente = models.OneToOneField(Gerente, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'tipo_recurso'"""
