from django.db import models
from django.contrib.auth.models import User

# Create your models here



class Empresas(models.Model):
	nit            = models.CharField('NIT:',max_length = 60, null = False , blank = False)
	nombre         = models.CharField('nombre:', max_length = 60, null = False, blank = False)
	direccion      = models.CharField('direccion:', max_length = 100, null = False , blank = False)
	telefonos      = models.CharField('telefonos de la empresa:', max_length = 80)
	usuario        = models.ForeignKey(User, on_delete = models.PROTECT)
	fecha_creacion = models.DateTimeField(auto_now = False, auto_now_add = True)
	estado         = models.BooleanField(default = True)    


	class Meta:
		verbose_name        = "Empresa"
		verbose_name_plural = "Empresas"

	def __str__(self):
		return self.nit +"\t"+ self.nombre


class Fincas(models.Model):
	nombre              = models.CharField('nombre:', max_length = 60, null = False, blank = False)
	direccion           = models.CharField('direccion:', max_length = 100, null = False , blank = False)
	ubicacion_geofrafica = models.CharField('Ubicacion geografica', max_length = 60 , blank = False)
	responsable         = models.CharField(max_length = 100, blank = False)
	usuario             = models.ForeignKey(User, on_delete = models.PROTECT)
	fecha_creacion      = models.DateTimeField(auto_now = False, auto_now_add = True)


class TipoTabla(models.Model):
	tipo = models.CharField('Tipo de tabla:', max_length = 20, null = False, blank = False)

	class Meta:
		verbose_name        = "Tipo de tabla"
		verbose_name_plural = "Tipos de tablas"

	def __str__(self):
		return self.tipo


class Cargos(models.Model):
	cargo          = models.CharField('Cargo:', max_length = 40 , null = False, blank = False)
	descripcion    = models.CharField('Descripcion del cargo:', max_length = 300)
	finca          = models.ForeignKey(Fincas, on_delete = models.PROTECT)
	estado         = models.BooleanField(default = True)
	usuario        = models.ForeignKey(User ,on_delete = models.PROTECT)
	fecha_creacion = models.DateTimeField(auto_now = False, auto_now_add = True)
	tipo_tabla    = models.ForeignKey(TipoTabla, on_delete = models.PROTECT , default = 1)


	class Meta:
		verbose_name        = "Cargo"
		verbose_name_plural = "Cargos"


	def __str__(self):
		return self.id + "\t" + self.cargo

class TipoEmpleado(models.Model):
	tipo           = models.CharField('Tipo de empleado:', max_length = 20, null = False, blank = False)
	descripcion    = models.CharField('Descripcion:', max_length = 100)
	finca          = models.ForeignKey(Fincas, on_delete = models.PROTECT)
	estado         = models.BooleanField(default = True)
	usuario        = models.ForeignKey(User ,on_delete = models.PROTECT)
	fecha_creacion = models.DateTimeField(auto_now = False, auto_now_add = True)
	tipo_tabla    = models.ForeignKey(TipoTabla, on_delete = models.PROTECT , default = 1)

	class Meta:
		verbose_name        = "Tipo de empleado"
		verbose_name_plural = "Tipos de empleado"


	def __str__(self):
		return self.id + "\t" + self.tipo


class Empleados(models.Model):
	cedula         = models.CharField('Cedula:', max_length = 50, null=False, blank=False)
	nombre         = models.CharField('nombre del empleado:', max_length = 20)
	apellido       = models.CharField('Apellido del empledado:', max_length = 20)
	cargo        = models.ForeignKey(Cargos,on_delete = models.PROTECT)
	tipo_emp      = models.ForeignKey(TipoEmpleado,on_delete = models.PROTECT)
	direccion      = models.CharField('direccion del empleado:',max_length = 100 , null = False, blank = False)
	telefonos      = models.CharField('telefonos del empleado:', max_length = 80)
	email           = models.CharField('Correo Electronico:', max_length = 30)
	finca          = models.ForeignKey(Fincas, on_delete = models.PROTECT)
	estado         = models.BooleanField(default = True)
	usuario        = models.ForeignKey(User ,on_delete = models.PROTECT)
	fecha_creacion = models.DateTimeField(auto_now = False, auto_now_add = True)
	tipo_tabla    = models.ForeignKey(TipoTabla, on_delete = models.PROTECT, default = 2)


	class Meta:
		verbose_name        = "Empleado"
		verbose_name_plural = "Empleados"

	def __str__(self):
		return self.cedula + "\t" + self.nombre

class Color(models.Model):
	color          = models.CharField('Color:', max_length = 20, blank = False, null = False)
	finca          = models.ForeignKey(Fincas, on_delete = models.PROTECT)
	estado         = models.BooleanField(default = True)
	usuario        = models.ForeignKey(User ,on_delete = models.PROTECT)
	fecha_creacion = models.DateTimeField(auto_now = False, auto_now_add = True)
	tipo_tabla    = models.ForeignKey(TipoTabla, on_delete = models.PROTECT, default = 1)


	class Meta:
		verbose_name        = "Color"
		verbose_name_plural = "Colores"


	def __str__(self):
		self.id + "\t" + self.color

class SemanaAnio(models.Model):
	semana         = models.IntegerField('Semana del año:', null = False, blank = False)
	color        = models.ForeignKey(Color,on_delete = models.PROTECT)
	year           = models.IntegerField('Año', null = False, blank = False)
	fecha_inicial   = models.DateTimeField('Fecha Inicial:', auto_now_add = False)
	fecha_final     = models.DateTimeField('Fecha Final:', auto_now_add = False)
	finca          = models.ForeignKey(Fincas, on_delete = models.PROTECT)
	estado         = models.BooleanField(default = True)
	usuario        = models.ForeignKey(User ,on_delete = models.PROTECT)
	fecha_creacion = models.DateTimeField(auto_now = False, auto_now_add = True)
	tipo_tabla    = models.ForeignKey(TipoTabla, on_delete = models.PROTECT , default = 2)


	class Meta:
		verbose_name = "Semana del año"
		verbose_name = "Semanas del año"

	def __str__(self):
		return self.id + "\t" + self.semana

class EntradaSalidaEmp(models.Model):
	empleado     = models.ForeignKey(Empleados, on_delete = models.PROTECT)
	fecha          = models.DateTimeField('Fecha:',auto_now_add = False)
	semana       = models.ForeignKey(SemanaAnio, on_delete = models.PROTECT)
	hora_entrada    = models.TimeField('Hora de entrada:', auto_now_add = False, null=False, blank=False)
	detalle_entrada = models.CharField('Detalle de la entrada:', max_length = 200, null = False, blank = False)
	hora_salida     = models.TimeField('Hora de Salida:', auto_now_add = False)
	detalle_salida  = models.CharField('Detalle de la Salida:', max_length = 200, null = False, blank = False)
	finca          = models.ForeignKey(Fincas, on_delete = models.PROTECT)
	estado         = models.BooleanField(default = True)
	usuario        = models.ForeignKey(User,on_delete = models.PROTECT)
	fecha_creacion = models.DateTimeField(auto_now = False, auto_now_add = True)
	tipo_tabla    = models.ForeignKey(TipoTabla, on_delete = models.PROTECT, default = 2)

	class Meta:
		verbose_name = "Entrada y salida de empleado"
		verbose_name = "Entradas y salidas de empleados"

	def __str__(self):
		return self.id_empleado + "\t" + self.fecha

class Programacion(models.Model):
	fecha          = models.DateTimeField('Fecha de programacion:', auto_now_add = False)
	semana       = models.ForeignKey(SemanaAnio, on_delete = models.PROTECT)
	finca          = models.ForeignKey(Fincas, on_delete = models.PROTECT)
	estado         = models.BooleanField(default = True)
	usuario        = models.ForeignKey(User ,on_delete = models.PROTECT)
	fecha_creacion = models.DateTimeField(auto_now = False, auto_now_add = True)
	tipo_tabla    = models.ForeignKey(TipoTabla, on_delete = models.PROTECT, default = 2)
	

	class Meta:
		verbose_name        = "programacion"
		verbose_name_plural = "Programaciones"

	def __str__(self):
		return self.id_semana +"\t" + self.fecha

class Labores(models.Model):
	labor          = models.CharField('Labor:', max_length = 60, null = False, blank = False)
	descripcion    = models.CharField('Descripcion de la labor:', max_length = 60)
	finca          = models.ForeignKey(Fincas, on_delete = models.PROTECT)
	estado         = models.BooleanField(default = True)
	usuario        = models.ForeignKey(User ,on_delete = models.PROTECT)
	fecha_creacion = models.DateTimeField(auto_now = False, auto_now_add = True)
	tipo_tabla    = models.ForeignKey(TipoTabla, on_delete = models.PROTECT , default = 1)


	class Meta:
		verbose_name        = "Labor"
		verbose_name_plural = "Labores"

	def __str__(self):
		return self.id +"\t"+ self.labor

class Procesos(models.Model):
	procesos       = models.CharField('Procesos:', max_length = 60, null = False, blank = False)
	descripcion    = models.CharField('Descripcion del proceso:', max_length = 60)
	finca          = models.ForeignKey(Fincas, on_delete = models.PROTECT)
	estado         = models.BooleanField(default = True)
	usuario        = models.ForeignKey(User ,on_delete = models.PROTECT)
	fecha_creacion = models.DateTimeField(auto_now = False, auto_now_add = True)
	tipo_tabla    = models.ForeignKey(TipoTabla, on_delete = models.PROTECT, default = 1)


	class Meta:
		verbose_name        = "Proceso"
		verbose_name_plural = "Procesos"

	def __str__(self):
		return self.id +"\t"+ self.procesos

class DetalleProgramacion(models.Model):
	programacion = models.ForeignKey(Programacion, on_delete = models.PROTECT)
	empleado     = models.ForeignKey(Empleados, on_delete = models.PROTECT)
	labor        = models.ForeignKey(Labores, on_delete = models.PROTECT)
	proceso      = models.ForeignKey(Procesos, on_delete = models.PROTECT)
	finca          = models.ForeignKey(Fincas, on_delete = models.PROTECT)
	estado         = models.BooleanField(default = True)
	usuario        = models.ForeignKey(User ,on_delete = models.PROTECT)
	fecha_creacion = models.DateTimeField(auto_now = False, auto_now_add = True)
	tipo_tabla    = models.ForeignKey(TipoTabla, on_delete = models.PROTECT, default = 2)


	class Meta:
		verbose_name  = "Detalle de programacion"
		verbose_name_plural = "Detalles de programaciones"

	def __str__(self):
		return self.id_programacion +"\t"+ self.id_empleado +"\t"+ self.id_labor +"\t"+ self.id_proceso

class FuncionesEmpleados(models.Model):
	funcion        = models.CharField('Funcion:', max_length = 60, null = False, blank = False)
	descripcion    = models.CharField('Descripcion de la funcion:', max_length = 300)
	finca          = models.ForeignKey(Fincas, on_delete = models.PROTECT)
	estado         = models.BooleanField(default = True)
	usuario        = models.ForeignKey(User ,on_delete = models.PROTECT)
	fecha_creacion = models.DateTimeField(auto_now = False, auto_now_add = True)
	tipo_tabla    = models.ForeignKey(TipoTabla, on_delete = models.PROTECT, default = 1)

	class Meta:
		verbose_name        = "Funcion del empleado"
		verbose_name_plural = "Funciones de los empleados"

	def __str__(self):
		return self.id +"\t"+ self.funcion

class FuncionesXEmpleados(models.Model):
	funcion      = models.ForeignKey(FuncionesEmpleados, on_delete = models.PROTECT)
	empleado     = models.ForeignKey(Empleados, on_delete = models.PROTECT)
	finca          = models.ForeignKey(Fincas, on_delete = models.PROTECT)
	estado         = models.BooleanField(default = True)
	usuario        = models.ForeignKey(User ,on_delete = models.PROTECT)
	fecha_creacion = models.DateTimeField(auto_now = False, auto_now_add = True)
	tipo_tabla    = models.ForeignKey(TipoTabla, on_delete = models.PROTECT , default = 2)

	class Meta:
		verbose_name = "FuncionesXEmpleado"

	def __str__(self):
		return self.id

class Visitantes(models.Model):
	nit_cedula      = models.CharField('Nit / Cedula:', max_length = 60,)
	nombre_apellido = models.CharField('nombre y Apellidos', max_length = 60)
	finca          = models.ForeignKey(Fincas, on_delete = models.PROTECT)
	estado         = models.BooleanField(default = True)
	usuario        = models.ForeignKey(User ,on_delete = models.PROTECT)
	fecha_creacion = models.DateTimeField(auto_now = False, auto_now_add = True)
	tipo_tabla    = models.ForeignKey(TipoTabla, on_delete = models.PROTECT, default = 1)

	class Meta:
		verbose_name        = "Visitante"
		verbose_name_plural = "Visitantes"

	def __str__(self):
		return self.nit_cedula +"\t"+ self.nombre_apellido


class EntradaSalidaVisitas(models.Model):
	visitante    = models.ForeignKey(Visitantes, on_delete = models.PROTECT)
	fecha          = models.DateTimeField('Fecha:', auto_now_add = False)
	semana       = models.ForeignKey(SemanaAnio, on_delete = models.PROTECT)
	hora_entrada    = models.TimeField('Hora de Entrada:', auto_now_add = False)
	detalle_entrada = models.CharField('Detalle de entrada:', max_length = 200, null = False, blank = False)
	hora_salida     = models.TimeField('Hora de salida:', auto_now_add = False, null=True)
	detalle_salida  = models.CharField('Detalle de la salida:', max_length = 200,blank=True, null = True)
	finca          = models.ForeignKey(Fincas, on_delete = models.PROTECT)
	estado         = models.BooleanField(default = True)
	usuario        = models.ForeignKey(User ,on_delete = models.PROTECT)
	fecha_creacion = models.DateTimeField(auto_now = False, auto_now_add = True)
	tipo_tabla    = models.ForeignKey(TipoTabla, on_delete = models.PROTECT, default = 2)


	class Meta:
		verbose_name        = "Entrada y salida de visita"
		verbose_name_plural = "Entradas y salidas de visitas"

	def __str__(self):
		return self.id_visitante +"\t"+ self.fecha

class EntradaVehiculos(models.Model):
	visitante     = models.ForeignKey(Visitantes, on_delete = models.PROTECT, null = True, blank = True)
	empleado      = models.ForeignKey(Empleados , on_delete = models.PROTECT, null = True, blank = True)
	placa_vehiculo   = models.CharField('Placa del vehiculo:', max_length = 20)
	carga_entrada    = models.CharField('Carga de entrada:', max_length = 40, null = False, blank = False)
	carga_salida     = models.CharField('Carga de la salida:', max_length = 40, null = False, blank = False)
	n_poma          = models.IntegerField(null = False, blank = False)
	cantidad_pales   = models.IntegerField(null = False, blank = False)
	cajas_sueltas    = models.IntegerField(null = False, blank = False)
	finca           = models.ForeignKey(Fincas, on_delete = models.PROTECT)
	estado          = models.BooleanField(default = True)
	usuario         = models.ForeignKey(User ,on_delete = models.PROTECT)
	fecha_creacion  = models.DateTimeField(auto_now = False, auto_now_add = True)
	tipo_tabla     = models.ForeignKey(TipoTabla, on_delete = models.PROTECT, default = 2)

	class Meta:
		verbose_name        = "Entrada y salida de vehiculo"
		verbose_name_plural = "Entrada y salida de vehiculos"

	def __str__(self):
		return self.id_visitante +"\t"+ self.placa_vehiculo