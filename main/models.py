from django.db import models


class DataRegion(models.Model):
    name = models.CharField('Region name', max_length=256)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Data Region'
        verbose_name_plural = 'Data Regions'


class DataValue(models.Model):
    country = models.CharField('Country', max_length=256)
    value = models.IntegerField('Value')
    region = models.ForeignKey(DataRegion, related_name='values')

    def __str__(self):
        return '{0} => {1} => {2}'.format(self.region, self.country, self.value)

    class Meta:
        verbose_name = 'Data Value'
        verbose_name_plural = 'Data Values'
