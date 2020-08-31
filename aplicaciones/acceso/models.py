from django.db import models
from django.contrib.auth.models import User

# Create your models here

class TipoTabla(models.Model):
	tipo = models.CharField('Tipo de tabla:', max_length = 20, null = False, blank = False)

	class Meta:
		verbose_name        = "Tipo de tabla"
		verbose_name_plural = "Tipos de tablas"

	def __str__(self):
		return self.Tipo

class Empresas(models.Model):
	nit            = models.CharField('NIT:',max_length = 60, null = False , blank = False)
	nombre         = models.CharField('nombre:', max_length = 60, null = False, blank = False)
	direccion      = models.CharField('direccion:', max_length = 100, null = False , blank = False)
	telefonos      = models.CharField('telefonos de la empresa:', max_length = 80)
	usuario        = models.ForeignKey(User, on_delete = models.PROTECT)
	fecha_creacion = models.DateTimeField(auto_now = False, auto_now_add = True)
	estado         = models.BooleanField(default = True)
    id_tipo_tabla    = models.ForeignKey(TipoTabla, on_delete = models.PROTECT , default = 1)


	class Meta:
		verbose_name        = "Empresa"
		verbose_name_plural = "Empresas"

	def __str__(self):
		return self.Nit +"\t"+ self.nombre

class Fincas(models.Model):
	nombre              = models.CharField('nombre:', max_length = 60, null = False, blank = False)
	direccion           = models.CharField('direccion:', max_length = 100, null = False , blank = False)
	ubicacion_geofrafica = models.CharField('Ubicacion geografica', max_length = 60 , blank = False)
	responsable         = models.CharField(max_length = 100, blank = False)
	id_usuario             = models.ForeignKey(User, on_delete = models.PROTECT)
	fecha_creacion      = models.DateTimeField(auto_now = False, auto_now_add = True)
    id_tipo_tabla    = models.ForeignKey(TipoTabla, on_delete = models.PROTECT , default = 1)


class Cargos(models.Model):
	cargo          = models.CharField('Cargo:', max_length = 40 , null = False, blank = False)
	descripcion    = models.CharField('Descripcion del cargo:', max_length = 300)
	id_finca          = models.ForeignKey(Fincas, on_delete = models.PROTECT)
	estado         = models.BooleanField(default = True)
	id_usuario        = models.ForeignKey(User ,on_delete = models.PROTECT)
	fecha_creacion = models.DateTimeField(auto_now = False, auto_now_add = True)
	id_tipo_tabla    = models.ForeignKey(TipoTabla, on_delete = models.PROTECT , default = 1)


	class Meta:
		verbose_name        = "Cargo"
		verbose_name_plural = "Cargos"


	def __str__(self):
		return self.id + "\t" + self.Cargo

class TipoEmpleado(models.Model):
	tipo           = models.CharField('Tipo de empleado:', max_length = 20, null = False, blank = False)
	descripcion    = models.CharField('Descripcion:', max_length = 100)
	id_finca          = models.ForeignKey(Fincas, on_delete = models.PROTECT)
	estado         = models.BooleanField(default = True)
	id_usuario        = models.ForeignKey(User ,on_delete = models.PROTECT)
	fecha_creacion = models.DateTimeField(auto_now = False, auto_now_add = True)
	id_tipo_tabla    = models.ForeignKey(TipoTabla, on_delete = models.PROTECT , default = 1)

	class Meta:
		verbose_name        = "Tipo de empleado"
		verbose_name_plural = "Tipos de empleado"


	def __str__(self):
		return self.id + "\t" + self.Tipo


class Empleados(models.Model):
	cedula         = models.CharField('Cedula:', max_length = 50, null=False, blank=False)
	nombre         = models.CharField('nombre del empleado:', max_length = 20)
	apellido       = models.CharField('Apellido del empledado:', max_length = 20)
	id_cargo        = models.ForeignKey(Cargos,on_delete = models.PROTECT)
	id_tipo_emp      = models.ForeignKey(TipoEmpleado,on_delete = models.PROTECT)
	direccion      = models.CharField('direccion del empleado:',max_length = 100 , null = False, blank = False)
	telefonos      = models.CharField('telefonos del empleado:', max_length = 80)
	email           = models.CharField('Correo Electronico:', max_length = 30)
	id_finca          = models.ForeignKey(Fincas, on_delete = models.PROTECT)
	estado         = models.BooleanField(default = True)
	id_usuario        = models.ForeignKey(User ,on_delete = models.PROTECT)
	fecha_creacion = models.DateTimeField(auto_now = False, auto_now_add = True)
	id_tipo_tabla    = models.ForeignKey(TipoTabla, on_delete = models.PROTECT, default = 2)


	class Meta:
		verbose_name        = "Empleado"
		verbose_name_plural = "Empleados"

	def __str__(self):
		return self.Cedula + "\t" + self.nombre

class Color(models.Model):
	color          = models.CharField('Color:', max_length = 20, blank = False, null = False)
	id_finca          = models.ForeignKey(Fincas, on_delete = models.PROTECT)
	estado         = models.BooleanField(default = True)
	id_usuario        = models.ForeignKey(User ,on_delete = models.PROTECT)
	fecha_creacion = models.DateTimeField(auto_now = False, auto_now_add = True)
	id_tipo_tabla    = models.ForeignKey(TipoTabla, on_delete = models.PROTECT, default = 1)


	class Meta:
		verbose_name        = "Color"
		verbose_name_plural = "Colores"


	def __str__(self):
		self.id + "\t" + self.Color

class SemanaAnio(models.Model):
	semana         = models.IntegerField('Semana del año:', null = False, blank = False)
	id_color        = models.ForeignKey(Color,on_delete = models.PROTECT)
	year           = models.IntegerField('Año', null = False, blank = False)
	fecha_inicial   = models.DateTimeField('Fecha Inicial:', auto_now_add = False)
	fecha_final     = models.DateTimeField('Fecha Final:', auto_now_add = False)
	id_finca          = models.ForeignKey(Fincas, on_delete = models.PROTECT)
	estado         = models.BooleanField(default = True)
	id_usuario        = models.ForeignKey(User ,on_delete = models.PROTECT)
	fecha_creacion = models.DateTimeField(auto_now = False, auto_now_add = True)
	id_tipo_tabla    = models.ForeignKey(TipoTabla, on_delete = models.PROTECT , default = 2)


	class Meta:
		verbose_name = "Semana del año"
		verbose_name = "Semanas del año"

	def __str__(self):
		return self.id + "\t" + self.Semana

class EntradaSalidaEmp(models.Model):
	id_empleado     = models.ForeignKey(Empleados, on_delete = models.PROTECT)
	fecha          = models.DateTimeField('Fecha:',auto_now_add = False)
	id_semana       = models.ForeignKey(SemanaAnio, on_delete = models.PROTECT)
	hora_entrada    = models.TimeField('Hora de entrada:', auto_now_add = False)
	detalle_entrada = models.CharField('Detalle de la entrada:', max_length = 200, null = False, blank = False)
	hora_salida     = models.TimeField('Hora de Salida:', auto_now_add = False)
	detalle_salida  = models.CharField('Detalle de la Salida:', max_length = 200, null = False, blank = False)
	id_finca          = models.ForeignKey(Fincas, on_delete = models.PROTECT)
	estado         = models.BooleanField(default = True)
	id_usuario        = models.ForeignKey(User ,on_delete = models.PROTECT)
	fecha_creacion = models.DateTimeField(auto_now = False, auto_now_add = True)
	id_tipo_tabla    = models.ForeignKey(TipoTabla, on_delete = models.PROTECT, default = 2)

	class Meta:
		verbose_name = "Entrada y salida de empleado"
		verbose_name = "Entradas y salidas de empleados"

	def __str__(self):
		return self.idEmpleado + "\t" + self.nombreApellido

class Programacion(models.Model):
	fecha          = models.DateTimeField('Fecha de programacion:', auto_now_add = False)
	id_semana       = models.ForeignKey(SemanaAnio, on_delete = models.PROTECT)
	id_finca          = models.ForeignKey(Fincas, on_delete = models.PROTECT)
	estado         = models.BooleanField(default = True)
	id_usuario        = models.ForeignKey(User ,on_delete = models.PROTECT)
	fecha_creacion = models.DateTimeField(auto_now = False, auto_now_add = True)
	id_tipo_tabla    = models.ForeignKey(TipoTabla, on_delete = models.PROTECT, default = 2)
	

	class Meta:
		verbose_name        = "programacion"
		verbose_name_plural = "Programaciones"

	def __str__(self):
		return self.idSemana +"\t" + self.Fecha

class Labores(models.Model):
	labor          = models.CharField('Labor:', max_length = 60, null = False, blank = False)
	descripcion    = models.CharField('Descripcion de la labor:', max_length = 60)
	id_finca          = models.ForeignKey(Fincas, on_delete = models.PROTECT)
	estado         = models.BooleanField(default = True)
	id_usuario        = models.ForeignKey(User ,on_delete = models.PROTECT)
	fecha_creacion = models.DateTimeField(auto_now = False, auto_now_add = True)
	id_tipo_tabla    = models.ForeignKey(TipoTabla, on_delete = models.PROTECT , default = 1)


	class Meta:
		verbose_name        = "Labor"
		verbose_name_plural = "Labores"

	def __str__(self):
		return self.id +"\t"+ self.Labor

class Procesos(models.Model):
	procesos       = models.CharField('Procesos:', max_length = 60, null = False, blank = False)
	descripcion    = models.CharField('Descripcion del proceso:', max_length = 60)
	id_finca          = models.ForeignKey(Fincas, on_delete = models.PROTECT)
	estado         = models.BooleanField(default = True)
	id_usuario        = models.ForeignKey(User ,on_delete = models.PROTECT)
	id_fecha_creacion = models.DateTimeField(auto_now = False, auto_now_add = True)
	id_tipo_tabla    = models.ForeignKey(TipoTabla, on_delete = models.PROTECT, default = 1)


	class Meta:
		verbose_name        = "Proceso"
		verbose_name_plural = "Procesos"

	def __str__(self):
		return self.id +"\t"+ self.Procesos

class DetalleProgramacion(models.Model):
	id_programacion = models.ForeignKey(Programacion, on_delete = models.PROTECT)
	id_empleado     = models.ForeignKey(Empleados, on_delete = models.PROTECT)
	id_labor        = models.ForeignKey(Labores, on_delete = models.PROTECT)
	id_proceso      = models.ForeignKey(Procesos, on_delete = models.PROTECT)
	id_finca          = models.ForeignKey(Fincas, on_delete = models.PROTECT)
	estado         = models.BooleanField(default = True)
	id_usuario        = models.ForeignKey(User ,on_delete = models.PROTECT)
	fecha_creacion = models.DateTimeField(auto_now = False, auto_now_add = True)
	id_tipo_tabla    = models.ForeignKey(TipoTabla, on_delete = models.PROTECT, default = 2)


	class Meta:
		verbose_name  = "Detalle de programacion"
		verbose_name_plural = "Detalles de programaciones"

	def __str__(self):
		return self.idProgramacion +"\t"+ self.idEmpleado +"\t"+ self.idLabor +"\t"+ self.idProceso

class FuncionesEmpleados(models.Model):
	funcion        = models.CharField('Funcion:', max_length = 60, null = False, blank = False)
	descripcion    = models.CharField('Descripcion de la funcion:', max_length = 300)
	id_finca          = models.ForeignKey(Fincas, on_delete = models.PROTECT)
	estado         = models.BooleanField(default = True)
	id_usuario        = models.ForeignKey(User ,on_delete = models.PROTECT)
	fecha_creacion = models.DateTimeField(auto_now = False, auto_now_add = True)
	id_tipo_tabla    = models.ForeignKey(TipoTabla, on_delete = models.PROTECT, default = 1)

	class Meta:
		verbose_name        = "Funcion del empleado"
		verbose_name_plural = "Funciones de los empleados"

	def __str__(self):
		return self.id +"\t"+ self.Funcion

class FuncionesXEmpleados(models.Model):
	id_funcion      = models.ForeignKey(FuncionesEmpleados, on_delete = models.PROTECT)
	id_empleado     = models.ForeignKey(Empleados, on_delete = models.PROTECT)
	id_finca          = models.ForeignKey(Fincas, on_delete = models.PROTECT)
	estado         = models.BooleanField(default = True)
	id_usuario        = models.ForeignKey(User ,on_delete = models.PROTECT)
	fecha_creacion = models.DateTimeField(auto_now = False, auto_now_add = True)
	id_tipo_tabla    = models.ForeignKey(TipoTabla, on_delete = models.PROTECT , default = 2)

	class Meta:
		verbose_name = "FuncionesXEmpleado"

	def __str__(self):
		return self.id

class Visitantes(models.Model):
	nit_edula      = models.CharField('Nit / Cedula:', max_length = 60,)
	nombre_apellido = models.CharField('nombre y Apellidos', max_length = 60)
	id_finca          = models.ForeignKey(Fincas, on_delete = models.PROTECT)
	estado         = models.BooleanField(default = True)
	id_usuario        = models.ForeignKey(User ,on_delete = models.PROTECT)
	fecha_creacion = models.DateTimeField(auto_now = False, auto_now_add = True)
	id_tipo_tabla    = models.ForeignKey(TipoTabla, on_delete = models.PROTECT, default = 1)

	class Meta:
		verbose_name        = "Visitante"
		verbose_name_plural = "Visitantes"

	def __str__(self):
		return self.nitCedula +"\t"+ self.nombreApellido

class EntradaSalidaVisitas(models.Model):
	id_visitante    = models.ForeignKey(Visitantes, on_delete = models.PROTECT)
	fecha          = models.DateTimeField('Fecha:', auto_now_add = False)
	id_semana       = models.ForeignKey(SemanaAnio, on_delete = models.PROTECT)
	hora_entrada    = models.TimeField('Hora de Entrada:', auto_now_add = False)
	detalle_entrada = models.CharField('Detalle de entrada:', max_length = 200, null = False, blank = False)
	hora_salida     = models.TimeField('Hora de salida:', auto_now_add = False)
	detalle_salida  = models.CharField('Detalle de la salida:', max_length = 200, null = False)
	id_finca          = models.ForeignKey(Fincas, on_delete = models.PROTECT)
	estado         = models.BooleanField(default = True)
	id_usuario        = models.ForeignKey(User ,on_delete = models.PROTECT)
	fecha_creacion = models.DateTimeField(auto_now = False, auto_now_add = True)
	id_tipo_tabla    = models.ForeignKey(TipoTabla, on_delete = models.PROTECT, default = 2)


	class Meta:
		verbose_name        = "Entrada y salida de visita"
		verbose_name_plural = "Entradas y salidas de visitas"

	def __str__(self):
		return self.idVisitante +"\t"+ self.Fecha

class EntradaVehiculos(models.Model):
	id_visitante     = models.ForeignKey(Visitantes, on_delete = models.PROTECT, null = True, blank = True)
	id_empleado      = models.ForeignKey(Empleados , on_delete = models.PROTECT, null = True, blank = True)
	placa_vehiculo   = models.CharField('Placa del vehiculo:', max_length = 20)
	carga_entrada    = models.CharField('Carga de entrada:', max_length = 40, null = False, blank = False)
	carga_salida     = models.CharField('Carga de la salida:', max_length = 40, null = False, blank = False)
	n_poma          = models.IntegerField(null = False, blank = False)
	cantidad_pales   = models.IntegerField(null = False, blank = False)
	cajas_sueltas    = models.IntegerField(null = False, blank = False)
	id_finca           = models.ForeignKey(Fincas, on_delete = models.PROTECT)
	estado          = models.BooleanField(default = True)
	id_usuario         = models.ForeignKey(User ,on_delete = models.PROTECT)
	fecha_creacion  = models.DateTimeField(auto_now = False, auto_now_add = True)
	id_tipo_tabla     = models.ForeignKey(TipoTabla, on_delete = models.PROTECT, default = 2)

	class Meta:
		verbose_name        = "Entrada y salida de vehiculo"
		verbose_name_plural = "Entrada y salida de vehiculos"

	def __str__(self):
		return self.idVisitante +"\t"+ self.placaVehiculo



















 


