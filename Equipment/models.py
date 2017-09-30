from django.db import models


# Create your models here.
class SeismographMode(models.Model):
    """
    地震仪型号
    """
    name = models.CharField(max_length=20, verbose_name=u'地震仪型号')

    def __str__(self):
        return self.name

    class Meta():
        verbose_name = '地震仪型号'
        verbose_name_plural = verbose_name


class Seismograph(models.Model):
    """
    地震仪
    """
    serial = models.CharField(max_length=10, unique=True, blank=False, null=False, verbose_name=u'序列号')
    model = models.ForeignKey(SeismographMode, verbose_name=u'地震仪型号')
    status = models.IntegerField(choices=((1, u'库存'), (2, u'在用'), (3, u'故障'), (4, u'维修中')))


class Collector(models.Model):
    """
    数据采集器
    """
    serial = models.CharField(max_length=10, unique=True, blank=False, null=False, verbose_name=u'序列号')
    model = models.ForeignKey(CollectorMode, verbose_name=u'数据采集器型号')
    status = models.IntegerField(choices=((1, u'库存'), (2, u'在用'), (3, u'故障'), (4, u'维修中')))


class CollectorMode(models.Model):
    """
    数据采集器型号
    """
    name = models.CharField(max_length=20, verbose_name=u'数据采集器型号')

    def __str__(self):
        return self.name

    class Meta():
        verbose_name = '数据采集器型号'
        verbose_name_plural = verbose_name


class GPSAntennas(models.Model):
    """
    GPS天线
    """
    GPSAntenna_Type = models.IntegerField(choices=((1, u'老式'), (2, u'新式')), verbose_name=u'GPS天线类型')
    GPSAntenna_num = models.IntegerField(default=0, verbose_name=u'每种GPS天线的数量')






