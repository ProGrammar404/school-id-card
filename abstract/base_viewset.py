from rest_framework import viewsets
from .serializers import BaseModelSerializer
from .pagination import BasePagination


class BaseModelViewSet(viewsets.ModelViewSet):
    serializer_class = BaseModelSerializer
    pagination_class = BasePagination
    http_method_names = ["get", "post", "patch"]
    ordering_fields = ["created_at", "updated_at"]
    ordering = ["-created_at"]
