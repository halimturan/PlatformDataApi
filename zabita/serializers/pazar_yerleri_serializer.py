from zabita.models import PazarYerleri
from rest_framework_gis.serializers import GeoFeatureModelSerializer, ModelSerializer


class PazarYerleriSerializer(ModelSerializer):

    class Meta:
        model = PazarYerleri
        fields = ('id', 'ilce', 'count',)


class PazarYerleriSerializerGeojson(GeoFeatureModelSerializer):

    class Meta:
        model = PazarYerleri
        geo_field = "point"
        fields = ('id', 'ilce', 'count', 'point')
