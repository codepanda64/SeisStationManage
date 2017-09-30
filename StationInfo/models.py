from django.db import models

import django.utils.timezone as timezone

from Equipment.models import Collector, Seismograph


# Create your models here.
class Station(models.Model):
    """
    台站类
    """
    number = models.CharField(max_length=10, verbose_name=u'台站编号')
    name_en = models.CharField(max_length=50, verbose_name=u'台站英文名')
    name_cn = models.CharField(max_length=50, verbose_name=u'台站中文名')
    collector = models.ForeignKey(Collector, verbose_name=u'数据采集器')
    seismograph = models.ForeignKey(Seismograph, verbose_name=u'地震仪')
    cf_card1_total = models.FloatField(default=0.0, verbose_name=u'卡槽1卡容量')
    cf_card2_total = models.FloatField(default=0.0, verbose_name=u'卡槽2卡容量')
    create_date = models.TimeField(default=timezone.now, verbose_name=u'台站建设时间')
    updata_date = models.TimeField(default=timezone.now, verbose_name=u'台站信息更新时间')


