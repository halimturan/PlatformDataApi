from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from zabita.serializers.pazar_yerleri_serializer import PazarYerleriSerializer, PazarYerleriSerializerGeojson
from zabita.models import PazarYerleri


class PazarYerleriViewSet(viewsets.ModelViewSet):
    queryset = PazarYerleri.objects.all()
    serializer_class = PazarYerleriSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter,)
    filterset_fieldset = ('ilce',)

    @action(detail=False)
    def type_geojson(self, request, *args, **kwargs):
        qs = PazarYerleri.objects.all()
        queryset = self.filter_queryset(qs)
        serializer = PazarYerleriSerializerGeojson(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def count_only(self, request, *args, **kwargs):
        qs = PazarYerleri.objects.all()
        return Response({"count": qs.count()})

