from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    #path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('record/<int:pk>', views.customer_record, name='record'),
    path('delete_record/<int:pk>', views.delete_record, name='delete_record'),
    path('add_record/', views.add_record, name='add_record'),
    path('update_record/<int:pk>', views.update_record, name='update_record'),
    path('bitacoravista/', views.bitarec, name='bitacoravista'),
    path('add_bita/', views.add_bita, name='add_bita'),
    path('clientesvista/', views.clien, name='clientesvista'),
    path('equiposvista/', views.equip, name='equiposvista'),
    path('usuariosvista/', views.usu, name='usuariosvista'),
    path('detalles_bitacora/<int:pk>', views.debita, name='detalles_bitacora'),
    path('update_bitacora/<int:pk>', views.update_bitacora, name='update_bitacora'),
    path('delete_bitacora/<int:pk>', views.delete_bitacora, name='delete_bitacora'),
    path('add_cliente', views.add_cliente, name='add_cliente'),
    path('detalles_cliente/<int:pk>', views.declien, name='detalles_cliente'),
    path('update_clientes/<int:pk>', views.update_clientes, name='update_clientes'),
    path('delete_clientes/<int:pk>', views.delete_clientes, name='delete_clientes'),
    path('add_equipos/', views.add_equipos, name='add_equipos'),
    path('detalles_equipos/<int:pk>', views.deequip, name='detalles_equipos'),
    path('update_equipos/<int:pk>', views.update_equipos, name='update_equipos'),
    path('delete_equipos/<int:pk>', views.delete_equipos, name='delete_equipos'),
    path('agregar_servicio/<int:pk>', views.agregar_servicio, name='agregar_servicio'),


]
