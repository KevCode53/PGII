from django.urls import path
from django.conf.urls import url
# Llamando a las views de registros
from .views import Ingreso_PDF
from .views import *
from django.conf.urls import url


urlpatterns = [
   url(r"^Ingreso_PDF/(?P<id>)", Ingreso_PDF.as_view(), name='ingerso_pdf'),
    # path('<int:id>/', Listado_Material.as_view(), name='listadoPDF'),
    # path para la impresion de listado de Ingresos
    url(r"^PDF_Ingresos/", Listado_Ingresos.as_view()),
    # path para la impresion de listado de materiales
    url(r"^PDF_Materiales/", Listado_Detalle_Materiales.as_view()),
    # path para la impresion de listado de materiales
    url(r"^PDF_Equipos/", Listado_Detalle_Equipos.as_view()),
   ]
