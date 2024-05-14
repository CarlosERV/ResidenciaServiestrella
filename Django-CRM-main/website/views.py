from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm, AddBitaForm, User, AddClientesForm, AddEquiposForm
from .models import Record, ClientesTb, Equipos, Bitacor
from django.http import HttpResponse
import mysql.connector
from django.template import loader
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from django.db.models import Q


def home(request):
	records = Record.objects.all()
	# Check to see if logging in
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		# Authenticate
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, "Bienvenido "+username)
			return redirect('home')
		else:
			messages.success(request, "ha ocurrido un error, por favor intenta nuevamente")
			return redirect('home')
	else:
		return render(request, 'home.html', {'records':records})	



def logout_user(request):
	logout(request)
	messages.success(request, "Sesion cerrada...")
	return redirect('home')


def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "Usuario registrado con exito, bienvenido "+username)
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})

def customer_record(request, pk):
	if request.user.is_authenticated:
		# Look Up Records
		customer_record = Record.objects.get(id=pk)
		return render(request, 'record.html', {'customer_record':customer_record})
	else:
		messages.success(request, "Iniciar sesion para ver esa pagina...")
		return redirect('home')

def bitarec(request):
	if request.user.is_authenticated:

		bitarec=Bitacor.objects.all()
		return render(request, 'bitacoravista.html', {'bitarec':bitarec})
	else:
		messages.success(request, "Error")
		return redirect("home")		
	
def debita(request, pk):
	if request.user.is_authenticated:

		debita=Bitacor.objects.get(id=pk)
		return render(request, 'detalles_bitacora.html', {'debita':debita})
	else:
		messages.success(request, "Error")
		return redirect("bitacoravista.html")	

def clien(request):
	if request.user.is_authenticated:
		clien=ClientesTb.objects.all()	
		return render(request, 'clientesvista.html', {'clien':clien})		
	else:
		messages.success(request, "Error")
		return redirect("home")
	
def declien(request, pk):
	if request.user.is_authenticated:
		declien=ClientesTb.objects.get(id=pk)	
		return render(request, 'detalles_cliente.html', {'declien':declien})		
	else:
		messages.success(request, "Error")
		return redirect("clientesvista.html")	
	
def usu(request):
	if request.user.is_authenticated:
		usu=User.objects.all()	
		return render(request, 'usuariosvista.html', {'usu':usu})		
	else:
		messages.success(request, "Error")
		return redirect("home")	

def equip(request):
	if request.user.is_authenticated:
		equip=Equipos.objects.all()	
		return render(request, 'equiposvista.html', {'equip':equip})		
	else:
		messages.success(request, "Error")
		return redirect("home")
	
def deequip(request, pk):
	if request.user.is_authenticated:
		deequip=Equipos.objects.get(id=pk)	
		return render(request, 'detalles_equipos.html', {'deequip':deequip})		
	else:
		messages.success(request, "Error")
		return redirect("equiposvista.html")		

class views():
	def home(self):
		return HttpResponse('HOlaaa')		

def delete_record(request, pk):
	if request.user.is_authenticated:
		delete_it = Record.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Registro eliminado con exito...")
		return redirect('home')
	else:
		messages.success(request, "Debes iniciar sesion primero...")
		return redirect('home')
	
def delete_bitacora(request, pk):
	if request.user.is_authenticated:
		delete_it = Bitacor.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Registro eliminado con exito...")
		return redirect('bitacoravista')
	else:
		messages.success(request, "Debes iniciar sesion primero...")
		return redirect('home')	
	
def delete_clientes(request, pk):
	if request.user.is_authenticated:
		delete_it = ClientesTb.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Registro eliminado con exito...")
		return redirect('clientesvista')
	else:
		messages.success(request, "Debes iniciar sesion primero...")
		return redirect('home')		
	
def delete_equipos(request, pk):
	if request.user.is_authenticated:
		delete_it = Equipos.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Registro eliminado con exito...")
		return redirect('equiposvista')
	else:
		messages.success(request, "Debes iniciar sesion primero...")
		return redirect('home')			


def add_record(request):
	form = AddRecordForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_record = form.save()
				messages.success(request, "Registro agregado con el id...")
				return redirect('home')
		return render(request, 'add_record.html', {'form':form})
	else:
		messages.success(request, "Debes iniciar sesion primero...")
		return redirect('home')
		
def add_bita(request):
	form = AddBitaForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_bita = form.save()
				messages.success(request, "Registro agregado con el id...")
				return redirect('bitacoravista')
		return render(request, 'add_bita.html', {'form':form})
	else:
		messages.success(request, "Debes iniciar sesion primero...")
		return redirect('home')
	
def add_cliente(request):
	form = AddClientesForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_cliente = form.save()
				messages.success(request, "Registro agregado")
				return redirect('clientesvista')
		return render(request, 'add_cliente.html', {'form':form})
	else:
		messages.success(request, "Debes iniciar sesion primero...")
		return redirect('home')	
	
def add_equipos(request):
	form = AddEquiposForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_equipo = form.save()
				messages.success(request, "Registro agregado")
				return redirect('equiposvista')
		return render(request, 'add_equipo.html', {'form':form})
	else:
		messages.success(request, "Debes iniciar sesion primero...")
		return redirect('home')	


def update_record(request, pk):
	if request.user.is_authenticated:
		current_record = Record.objects.get(id=pk)
		form = AddRecordForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Registro actualizado exitosamente")
			return redirect('home')
		return render(request, 'update_record.html', {'form':form})
	else:
		messages.success(request, "Debes iniciar sesion primero...")
		return redirect('home')
	

def update_bitacora(request, pk):
	if request.user.is_authenticated:
		current_record = Bitacor.objects.get(id=pk)
		form = AddBitaForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Registro actualizado exitosamente")
			return redirect('bitacoravista')
		return render(request, 'update_bitacora.html', {'form':form})
	else:
		messages.success(request, "Debes iniciar sesion primero...")
		return redirect('home')
	
def update_clientes(request, pk):
	if request.user.is_authenticated:
		current_record = ClientesTb.objects.get(id=pk)
		form = AddClientesForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Registro actualizado exitosamente")
			return redirect('clientesvista')
		return render(request, 'update_cliente.html', {'form':form})
	else:
		messages.success(request, "Debes iniciar sesion primero...")
		return redirect('home')
	
def update_equipos(request, pk):
	if request.user.is_authenticated:
		current_record = Equipos.objects.get(id=pk)
		form = AddEquiposForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Registro actualizado exitosamente")
			return redirect('equiposvista')
		return render(request, 'update_equipos.html', {'form':form})
	else:
		messages.success(request, "Debes iniciar sesion primero...")
		return redirect('home')	

def agregar_servicio(request, pk):
	if request.user.is_authenticated:
		current_record = ClientesTb.objects.get(id=pk)
		form = AddRecordForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Registro actualizado exitosamente")
			return redirect('home')
		return render(request, 'add_record.html', {'form':form})
	else:
		messages.success(request, "Debes iniciar sesion primero...")
		return redirect('home')	
