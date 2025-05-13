from rest_framework import viewsets
from .serializers import FornecedorSerializer
from .models import Fornecedor

class FornecedorViewSet(viewsets.ModelViewSet):
    queryset = Fornecedor.objects.all().order_by('-criado_em')
    serializer_class = FornecedorSerializer
