from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .fornecedores.views import FornecedorViewSet

router = routers.DefaultRouter()
router.register(r'fornecedores', FornecedorViewSet, basename='fornecedor')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
