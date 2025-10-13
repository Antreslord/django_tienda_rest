"""
URL configuration for apitienda project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api.views import crear_compra, crear_cliente, compras_por_cliente, gasto_total_por_cliente, gastos_por_tipo_entrega

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/compras/', crear_compra, name='crear_compra'),
    path('api/clientes/', crear_cliente, name='crear_cliente'),
    path('api/compras/<int:cliente_id>/', compras_por_cliente, name='compras_por_cliente'),
    path('api/cliente/gasto_total/<int:cliente_id>/', gasto_total_por_cliente, name='gasto_total_por_cliente'),
    path('api/cliente/tipo/<int:cliente_id>/', gastos_por_tipo_entrega, name='gasto_por_tipo_entrega'),
]