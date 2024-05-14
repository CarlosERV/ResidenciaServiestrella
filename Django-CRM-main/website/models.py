from django.db import models


class Record(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	first_name = models.CharField(max_length=50)
	last_name =  models.CharField(max_length=50)
	email =  models.EmailField(max_length=50)
	phone = models.CharField(max_length=20)
	address =  models.CharField(max_length=100)
	city =  models.CharField(max_length=50)
	RFC =  models.CharField(max_length=50)
	Equipo =  models.CharField(max_length=50)
	Marca =  models.CharField(max_length=50)
	Modelo =  models.CharField(max_length=50)
	NoSerie =  models.CharField(max_length=50)
	Lectura =  models.CharField(max_length=50)
	Observaciones =  models.CharField(max_length=50)
	Descripcion =  models.CharField(max_length=50)
	PUnitario =  models.DecimalField(max_digits=10, decimal_places=2)
	Importe =  models.DecimalField(max_digits=10, decimal_places=2)
	SubTotal =  models.DecimalField(max_digits=10, decimal_places=2)
	Iva =  models.DecimalField(max_digits=10, decimal_places=2)
	Total =  models.DecimalField(max_digits=10, decimal_places=2)
	servicio = models.CharField(max_length=50)
	

	def __str__(self):
		return(f"{self.first_name} {self.last_name}")
	

class Bitacor(models.Model):
	nombre = models.CharField(max_length=50)
	rfc =  models.CharField(max_length=50)
	razonS =  models.CharField(max_length=50)
	direccion = models.CharField(max_length=20)
	cuidad =  models.CharField(max_length=100)
	cp =  models.CharField(max_length=50)
	correo =  models.CharField(max_length=50)
	marca =  models.CharField(max_length=50)
	modelo =  models.CharField(max_length=50)
	nserie =  models.CharField(max_length=50)
	funciones =  models.CharField(max_length=50)
	servicio =  models.CharField(max_length=50)
	costo =  models.CharField(max_length=50)
	moneda =  models.CharField(max_length=50)
	procesos =  models.CharField(max_length=50)
	excedente =  models.CharField(max_length=50)
	observaciones =  models.CharField(max_length=50)

class ClientesTb(models.Model):
	nombre = models.CharField(max_length=50)
	contacto = models.CharField(max_length=50)
	correo = models.CharField(max_length=50)
	telefono = models.CharField(max_length=20)
	direccion = models.CharField(max_length=60)
	cuidad = models.CharField(max_length=50)
	rfc = models.CharField(max_length=50)	
	
			
class Equipos(models.Model):
	equipo = models.CharField(max_length=50)
	marca = models.CharField(max_length=50)
	modelo = models.CharField(max_length=50)
	nserie = models.CharField(max_length=35)
	lectura = models.CharField(max_length=30)
	descripcion = models.CharField(max_length=120)
	
