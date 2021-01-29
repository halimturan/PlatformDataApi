from django.contrib.gis.db import models


class PazarYerleri(models.Model):
    ilce = models.CharField(max_length=50, verbose_name="İlçe")
    count = models.SmallIntegerField(verbose_name="Sayı")
    point = models.PointField(verbose_name="Nokta (Geometry)")

    class Meta:
        verbose_name_plural = "Pazar Yerleri"
