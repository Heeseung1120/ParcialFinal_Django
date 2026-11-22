from django.contrib import admin
from django.urls import path, include
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # INCLUIR LAS RUTAS HIJAS
    path('profiles/', include("myapp.urls")),
    path('programas/crear/', views.crear_programa, name='crear_programa'),
]