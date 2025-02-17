"""SICAME URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

# Importamos los controles del settings
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
# Se importa el include para poder agregar los conjuntos de urls
from django.urls import path, include
from django.conf.urls import url

# Importamos las vistas para los PDF
from catalogo.views import Ficha_Kardex_PDF

urlpatterns = [
    path('', admin.site.urls),
    # Url's Para los PDF en Admin
    # Se crea el path para agregar los urls al sistema
    path('', include('core.urls')),
    path('', include('catalogo.urls')),
    path('', include('inventario.urls')),
    path('', include('registration.urls')),
    path('', include('movimientos.urls')),
]

# Truco para poder ver ficheros multimedia con el DEBUG=TRUE
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Custom titles para el admin
admin.site.site_header = 'Administrador Bodega Electricidad'
#  admin.site.index_title = 'No se que poner XD'
admin.site.site_title = 'Bodega Electricidad'
