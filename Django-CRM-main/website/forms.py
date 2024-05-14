from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record, Bitacor, ClientesTb, Equipos

class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Correo'}))
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))
	username = forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre de usuario'}))
    


	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'User Name'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	



# form-control-plaintext
# Create Add Record Form
class AddRecordForm(forms.ModelForm):
	first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Nombre", "class":"col-sm-10"}), label="Nombre")
	last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Contacto", "class":"col-sm-10"}), label="Contacto")
	email = forms.EmailField(required=True, widget=forms.widgets.EmailInput(attrs={"placeholder":"Correo", "class":"col-sm-10"}))
	phone = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder":"Telefono", "class":"col-sm-10"}), label="Telefono")
	address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Direccion", "class":"col-sm-10"}), label="Direccion")
	city = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Ciudad", "class":"col-sm-10"}), label="Ciudad")
	RFC = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"RFC", "class":"col-sm-10"}), label="RFC")
	Equipo = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Equipo", "class":"col-sm-10"}), label="Equipo")
	Marca = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Marca", "class":"col-sm-10"}), label="Marca")
	Modelo = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Modelo", "class":"col-sm-10"}), label="Modelo")
	NoSerie = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Numero de Serie", "class":"col-sm-10"}), label="No. Serie")
	Lectura = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Lectura", "class":"col-sm-10"}), label="Lectura")
	Observaciones = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Observaciones", "class":"col-sm-10"}), label="Observaciones")
	Descripcion = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Descripcion", "class":"col-sm-10"}), label="Descripcion")
	PUnitario = forms.DecimalField(required=True, widget=forms.widgets.NumberInput(attrs={"placeholder":"Precio Unitario", "class":"col-sm-10"}), label="P. Unitario")
	Importe = forms.DecimalField(required=True, widget=forms.widgets.NumberInput(attrs={"placeholder":"Importe", "class":"col-sm-10"}), label="Importe")
	SubTotal = forms.DecimalField(required=True, widget=forms.widgets.NumberInput(attrs={"placeholder":"Subtotal", "class":"col-sm-10"}), label="Subtotal")
	Iva = forms.DecimalField(required=True, widget=forms.widgets.NumberInput(attrs={"placeholder":"Iva", "class":"col-sm-10"}), label="Iva")
	Total = forms.DecimalField(required=True, widget=forms.widgets.NumberInput(attrs={"placeholder":"Total", "class":"col-sm-10"}), label="Total")
	servicio = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Tipo de Servicio", "class":"col-sm-10	"}), label="Servicio")
	

	class Meta:
		model = Record
		exclude = ("user",)

		# def __init__(self, *args, **kwargs):
		# 	super().__init__(*args, **kwargs)
		# 	self.fields['last_name'].label = "Apellido"  # Modifica la etiqueta del campo 'last_name'
		# 	self.fields['last_name'].widget.attrs.update({'placeholder': 'Apellido', 'class': 'text-danger'})  # Actualiza los atributos del widget


class AddBitaForm(forms.ModelForm):
	nombre = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Nombre", "class":"form-control"}), label="")
	rfc = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"RFC", "class":"form-control"}), label="")
	razonS = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Razon Social", "class":"form-control"}), label="")
	direccion = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Direccion", "class":"form-control"}), label="")
	cuidad = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Ciudad", "class":"form-control"}), label="")
	cp = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Codigo postal", "class":"form-control"}), label="")
	correo = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Correo", "class":"form-control"}), label="")
	marca = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Marca", "class":"form-control"}), label="")
	modelo = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Modelo", "class":"form-control"}), label="")
	nserie = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Numero de Serie", "class":"form-control"}), label="")
	funciones = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Funciones", "class":"form-control"}), label="")
	servicio = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Servicio", "class":"form-control"}), label="")
	costo = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Costo", "class":"form-control"}), label="")
	moneda = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Tipo de moneda", "class":"form-control"}), label="")
	procesos = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Procesos", "class":"form-control"}), label="")
	excedente = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Excedente", "class":"form-control"}), label="")
	observaciones = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Observaciones", "class":"form-control"}), label="")
    

	class Meta:
		model = Bitacor
		exclude = ("user",)

class AddClientesForm(forms.ModelForm):	
	nombre = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Nombre", "class":"form-control"}), label="")
	contacto = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Contacto", "class":"form-control"}), label="")
	correo = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Correo", "class":"form-control"}), label="")
	telefono = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Telefono", "class":"form-control"}), label="")
	direccion = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Direccion", "class":"form-control"}), label="")
	cuidad = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Ciudad", "class":"form-control"}), label="")
	rfc = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"RFC", "class":"form-control"}), label="")	

	class Meta:
		model = ClientesTb
		exclude = ("user",)

class AddEquiposForm(forms.ModelForm):
	equipo = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Nombre", "class":"form-control"}), label="")
	marca = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Marca", "class":"form-control"}), label="")
	modelo = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Modelo", "class":"form-control"}), label="")	
	nserie = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Numero de serie", "class":"form-control"}), label="")
	lectura = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Lectura", "class":"form-control"}), label="")
	descripcion = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Descripcion", "class":"form-control"}), label="")

	class Meta:
		model = Equipos
		exclude = ("user",)
	



    

