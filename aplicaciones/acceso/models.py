from django.db import models
from django.contrib.auth.models import User

# Create your models here

class Empresas(models.Model):
	Nit            = models.CharField('NIT:',max_length = 60, null = False , blank = False)
	Nombre         = models.CharField('Nombre:', max_length = 60, null = False, blank = False)
	Direccion      = models.CharField('Direccion:', max_length = 100, null = False , blank = False)
	Telefonos      = models.CharField('Telefonos de la empresa:', max_length = 80)
	usuario        = models.ForeignKey(User, on_delete = models.CASCADE)
	fecha_creacion = models.DateTimeField(auto_now = False, auto_now_add = True)
	Estado         = models.BooleanField(default = True)


	class Meta:
		verbose_name        = "Empresa"
		verbose_name_plural = "Empresas"

	def __str__(self):
		return self.Nit +"\t"+ self.Nombre

class Fincas(models.Model):
	Nombre              = models.CharField('Nombre:', max_length = 60, null = False, blank = False)
	Direccion           = models.CharField('Direccion:', max_length = 100, null = False , blank = False)
	ubicacionGeofrafica = models.CharField('Ubicacion geografica', max_length = 60 , blank = False)
	Responsable         = models.CharField(max_length = 100, blank = False)
	usuario             = models.ForeignKey(User, on_delete = models.CASCADE)
	fecha_creacion      = models.DateTimeField(auto_now = False, auto_now_add = True)


class tipoTabla(models.Model):
	Tipo = models.CharField('Tipo de tabla:', max_length = 80, null = False, blank = False)

	class Meta:
		verbose_name        = "Tipo de tabla"
		verbose_name_plural = "Tipos de tablas"

	def __str__(self):
		return self.Tipo


class Cargos(models.Model):
	Cargo          = models.CharField('Cargo:', max_length = 40 , null = False, blank = False)
	Descripcion    = models.CharField('Descripcion del cargo:', max_length = 300)
	Finca          = models.ForeignKey(Fincas, on_delete = models.CASCADE)
	Estado         = models.BooleanField(default = True)
	usuario        = models.ForeignKey(User ,on_delete = models.CASCADE)
	fecha_creacion = models.DateTimeField(auto_now = False, auto_now_add = True)
	idTipoTabla    = models.ForeignKey(tipoTabla, on_delete = models.CASCADE , default = 1)


	class Meta:
		verbose_name        = "Cargo"
		verbose_name_plural = "Cargos"


	def __str__(self):
		return self.id + "\t" + self.Cargo

class TipoEmpleado(models.Model):
	Tipo           = models.CharField('Tipo de empleado:', max_length = 20, null = False, blank = False)
	Descripcion    = models.CharField('Descripcion:', max_length = 100)
	Finca          = models.ForeignKey(Fincas, on_delete = models.CASCADE)
	Estado         = models.BooleanField(default = True)
	usuario        = models.ForeignKey(User ,on_delete = models.CASCADE)
	fecha_creacion = models.DateTimeField(auto_now = False, auto_now_add = True)
	idTipoTabla    = models.ForeignKey(tipoTabla, on_delete = models.CASCADE , default = 1)

	class Meta:
		verbose_name        = "Tipo de empleado"
		verbose_name_plural = "Tipos de empleado"


	def __str__(self):
		return self.id + "\t" + self.Tipo


class Empleados(models.Model):
	Cedula         = models.CharField('Cedula:', max_length = 50, null=False, blank=False)
	Nombre         = models.CharField('Nombre del empleado:', max_length = 20)
	Apellido       = models.CharField('Apellido del empledado:', max_length = 20)
	idCargo        = models.ForeignKey(Cargos,on_delete = models.CASCADE)
	idTipoEmp      = models.ForeignKey(TipoEmpleado,on_delete = models.CASCADE)
	Direccion      = models.CharField('Direccion del empleado:',max_length = 100 , null = False, blank = False)
	Telefonos      = models.CharField('Telefonos del empleado:', max_length = 80)
	Mail           = models.CharField('Correo Electronico:', max_length = 30)
	Finca          = models.ForeignKey(Fincas, on_delete = models.CASCADE)
	Estado         = models.BooleanField(default = True)
	usuario        = models.ForeignKey(User ,on_delete = models.CASCADE)
	fecha_creacion = models.DateTimeField(auto_now = False, auto_now_add = True)
	idTipoTabla    = models.ForeignKey(tipoTabla, on_delete = models.CASCADE, default = 2)


	class Meta:
		verbose_name        = "Empleado"
		verbose_name_plural = "Empleados"

	def __str__(self):
		return self.Cedula + "\t" + self.Nombre

class Color(models.Model):
	Color          = models.CharField('Color:', max_length = 20, blank = False, null = False)
	Finca          = models.ForeignKey(Fincas, on_delete = models.CASCADE)
	Estado         = models.BooleanField(default = True)
	usuario        = models.ForeignKey(User ,on_delete = models.CASCADE)
	fecha_creacion = models.DateTimeField(auto_now = False, auto_now_add = True)
	idTipoTabla    = models.ForeignKey(tipoTabla, on_delete = models.CASCADE, default = 1)


	class Meta:
		verbose_name        = "Color"
		verbose_name_plural = "Colores"


	def __str__(self):
		self.id + "\t" + self.Color

class SemanaAnio(models.Model):
	Semana         = models.IntegerField('Semana del año:', null = False, blank = False)
	idColor        = models.ForeignKey(Color,on_delete = models.CASCADE)
	Year           = models.IntegerField('Año', null = False, blank = False)
	fechaInicial   = models.DateTimeField('Fecha Inicial:', auto_now_add = False)
	fechaFinal     = models.DateTimeField('Fecha Final:', auto_now_add = False)
	Finca          = models.ForeignKey(Fincas, on_delete = models.CASCADE)
	Estado         = models.BooleanField(default = True)
	usuario        = models.ForeignKey(User ,on_delete = models.CASCADE)
	fecha_creacion = models.DateTimeField(auto_now = False, auto_now_add = True)
	idTipoTabla    = models.ForeignKey(tipoTabla, on_delete = models.CASCADE , default = 2)


	class Meta:
		verbose_name = "Semana del año"
		verbose_name = "Semanas del año"

	def __str__(self):
		return self.id + "\t" + self.Semana

class EntradaSalidaEmp(models.Model):
	idEmpleado     = models.ForeignKey(Empleados, on_delete = models.CASCADE)
	Fecha          = models.DateTimeField('Fecha:',auto_now_add = False)
	idSemana       = models.ForeignKey(SemanaAnio, on_delete = models.CASCADE)
	horaEntrada    = models.TimeField('Hora de entrada:', auto_now_add = False)
	detalleEntrada = models.CharField('Detalle de la entrada:', max_length = 200, null = False, blank = False)
	horaSalida     = models.TimeField('Hora de Salida:', auto_now_add = False)
	detalleSalida  = models.CharField('Detalle de la Salida:', max_length = 200, null = False, blank = False)
	Finca          = models.ForeignKey(Fincas, on_delete = models.CASCADE)
	Estado         = models.BooleanField(default = True)
	usuario        = models.ForeignKey(User ,on_delete = models.CASCADE)
	fecha_creacion = models.DateTimeField(auto_now = False, auto_now_add = True)
	idTipoTabla    = models.ForeignKey(tipoTabla, on_delete = models.CASCADE, default = 2)

	class Meta:
		verbose_name = "Entrada y salida de empleado"
		verbose_name = "Entradas y salidas de empleados"

	def __str__(self):
		return self.idEmpleado + "\t" + self.nombreApellido

class Programacion(models.Model):
	Fecha          = models.DateTimeField('Fecha de programacion:', auto_now_add = False)
	idSemana       = models.ForeignKey(SemanaAnio, on_delete = models.CASCADE)
	Finca          = models.ForeignKey(Fincas, on_delete = models.CASCADE)
	Estado         = models.BooleanField(default = True)
	usuario        = models.ForeignKey(User ,on_delete = models.CASCADE)
	fecha_creacion = models.DateTimeField(auto_now = False, auto_now_add = True)
	idTipoTabla    = models.ForeignKey(tipoTabla, on_delete = models.CASCADE, default = 2)
	

	class Meta:
		verbose_name        = "programacion"
		verbose_name_plural = "Programaciones"

	def __str__(self):
		return self.idSemana +"\t" + self.Fecha

class Labores(models.Model):
	Labor          = models.CharField('Labor:', max_length = 60, null = False, blank = False)
	Descripcion    = models.CharField('Descripcion de la labor:', max_length = 60)
	Finca          = models.ForeignKey(Fincas, on_delete = models.CASCADE)
	Estado         = models.BooleanField(default = True)
	usuario        = models.ForeignKey(User ,on_delete = models.CASCADE)
	fecha_creacion = models.DateTimeField(auto_now = False, auto_now_add = True)
	idTipoTabla    = models.ForeignKey(tipoTabla, on_delete = models.CASCADE , default = 1)


	class Meta:
		verbose_name        = "Labor"
		verbose_name_plural = "Labores"

	def __str__(self):
		return self.id +"\t"+ self.Labor

class Procesos(models.Model):
	Procesos       = models.CharField('Procesos:', max_length = 60, null = False, blank = False)
	Descripcion    = models.CharField('Descripcion del proceso:', max_length = 60)
	Finca          = models.ForeignKey(Fincas, on_delete = models.CASCADE)
	Estado         = models.BooleanField(default = True)
	usuario        = models.ForeignKey(User ,on_delete = models.CASCADE)
	fecha_creacion = models.DateTimeField(auto_now = False, auto_now_add = True)
	idTipoTabla    = models.ForeignKey(tipoTabla, on_delete = models.CASCADE, default = 1)


	class Meta:
		verbose_name        = "Proceso"
		verbose_name_plural = "Procesos"

	def __str__(self):
		return self.id +"\t"+ self.Procesos

class DetalleProgramacion(models.Model):
	idProgramacion = models.ForeignKey(Programacion, on_delete = models.CASCADE)
	idEmpleado     = models.ForeignKey(Empleados, on_delete = models.CASCADE)
	idLabor        = models.ForeignKey(Labores, on_delete = models.CASCADE)
	idProceso      = models.ForeignKey(Procesos, on_delete = models.CASCADE)
	Finca          = models.ForeignKey(Fincas, on_delete = models.CASCADE)
	Estado         = models.BooleanField(default = True)
	usuario        = models.ForeignKey(User ,on_delete = models.CASCADE)
	fecha_creacion = models.DateTimeField(auto_now = False, auto_now_add = True)
	idTipoTabla    = models.ForeignKey(tipoTabla, on_delete = models.CASCADE, default = 2)


	class Meta:
		verbose_name  = "Detalle de programacion"
		verbose_name_plural = "Detalles de programaciones"

	def __str__(self):
		return self.idProgramacion +"\t"+ self.idEmpleado +"\t"+ self.idLabor +"\t"+ self.idProceso

class FuncionesEmpleados(models.Model):
	Funcion        = models.CharField('Funcion:', max_length = 60, null = False, blank = False)
	Descripcion    = models.CharField('Descripcion de la funcion:', max_length = 300)
	Finca          = models.ForeignKey(Fincas, on_delete = models.CASCADE)
	Estado         = models.BooleanField(default = True)
	usuario        = models.ForeignKey(User ,on_delete = models.CASCADE)
	fecha_creacion = models.DateTimeField(auto_now = False, auto_now_add = True)
	idTipoTabla    = models.ForeignKey(tipoTabla, on_delete = models.CASCADE, default = 1)

	class Meta:
		verbose_name        = "Funcion del empleado"
		verbose_name_plural = "Funciones de los empleados"

	def __str__(self):
		return self.id +"\t"+ self.Funcion

class FuncionesXEmpleados(models.Model):
	idFuncion      = models.ForeignKey(FuncionesEmpleados, on_delete = models.CASCADE)
	idEmpleado     = models.ForeignKey(Empleados, on_delete = models.CASCADE)
	Finca          = models.ForeignKey(Fincas, on_delete = models.CASCADE)
	Estado         = models.BooleanField(default = True)
	usuario        = models.ForeignKey(User ,on_delete = models.CASCADE)
	fecha_creacion = models.DateTimeField(auto_now = False, auto_now_add = True)
	idTipoTabla    = models.ForeignKey(tipoTabla, on_delete = models.CASCADE , default = 2)

	class Meta:
		verbose_name = "FuncionesXEmpleado"

	def __str__(self):
		return self.id

class Visitantes(models.Model):
	nitCedula      = models.CharField('Nit / Cedula:', max_length = 60,)
	nombreApellido = models.CharField('Nombre y Apellidos', max_length = 60)
	Finca          = models.ForeignKey(Fincas, on_delete = models.CASCADE)
	Estado         = models.BooleanField(default = True)
	usuario        = models.ForeignKey(User ,on_delete = models.CASCADE)
	fecha_creacion = models.DateTimeField(auto_now = False, auto_now_add = True)
	idTipoTabla    = models.ForeignKey(tipoTabla, on_delete = models.CASCADE, default = 1)

	class Meta:
		verbose_name        = "Visitante"
		verbose_name_plural = "Visitantes"

	def __str__(self):
		return self.nitCedula +"\t"+ self.nombreApellido

class EntradaSalidaVisitas(models.Model):
	idVisitante    = models.ForeignKey(Visitantes, on_delete = models.CASCADE)
	Fecha          = models.DateTimeField('Fecha:', auto_now_add = False)
	idSemana       = models.ForeignKey(SemanaAnio, on_delete = models.CASCADE)
	horaEntrada    = models.TimeField('Hora de Entrada:', auto_now_add = False)
	detalleEntrada = models.CharField('Detalle de entrada:', max_length = 200, null = False, blank = False)
	horaSalida     = models.TimeField('Hora de salida:', auto_now_add = False)
	detalleSalida  = models.CharField('Detalle de la salida:', max_length = 200, null = False)
	Finca          = models.ForeignKey(Fincas, on_delete = models.CASCADE)
	Estado         = models.BooleanField(default = True)
	usuario        = models.ForeignKey(User ,on_delete = models.CASCADE)
	fecha_creacion = models.DateTimeField(auto_now = False, auto_now_add = True)
	idTipoTabla    = models.ForeignKey(tipoTabla, on_delete = models.CASCADE, default = 2)


	class Meta:
		verbose_name        = "Entrada y salida de visita"
		verbose_name_plural = "Entradas y salidas de visitas"

	def __str__(self):
		return self.idVisitante +"\t"+ self.Fecha

class EntradaVehiculos(models.Model):
	idVisitante    = models.ForeignKey(Visitantes, on_delete = models.CASCADE, null = True, blank = True)
	idEmpleado     = models.ForeignKey(Empleados , on_delete = models.CASCADE, null = True, blank = True)
	placaVehiculo  = models.CharField('Placa del vehiculo:', max_length = 20)
	cargaEntrada   = models.CharField('Carga de entrada:', max_length = 40, null = False, blank = False)
	cargaSalida    = models.CharField('Carga de la salida:', max_length = 40, null = False, blank = False)
	NPoma          = models.IntegerField(null = False, blank = False)
	cantidadPales  = models.IntegerField(null = False, blank = False)
	cajasSueltas   = models.IntegerField(null = False, blank = False)
	Finca          = models.ForeignKey(Fincas, on_delete = models.CASCADE)
	Estado         = models.BooleanField(default = True)
	usuario        = models.ForeignKey(User ,on_delete = models.CASCADE)
	fecha_creacion = models.DateTimeField(auto_now = False, auto_now_add = True)
	idTipoTabla    = models.ForeignKey(tipoTabla, on_delete = models.CASCADE, default = 2)

	class Meta:
		verbose_name        = "Entrada y salida de vehiculo"
		verbose_name_plural = "Entrada y salida de vehiculos"

	def __str__(self):
		return self.idVisitante +"\t"+ self.placaVehiculo



















 


