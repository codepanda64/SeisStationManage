from django.db import models

import django.utils.timezone as timezone

from StationInfo.models import Station


# Create your models here.
class Record(models.Model):
    """
    维护记录
    """
    station = models.ForeignKey(Station, unique=True, verbose_name=u'台站名')
    status = models.IntegerField(choices=((1, u'正常'), (2, u'异常')))
    cf_card1_used = models.FloatField(default=0.0, verbose_name=u'卡1使用量')
    cf_card2_used = models.FloatField(default=0.0, verbose_name=u'卡2使用量')
    input_voltage = models.FloatField(default=.0, verbose_name=u'输入电压')
    backup_voltabe = models.FloatField(default=.0, verbose_name=u'小电池电压')
    maintenance_date = models.DateTimeField(default=timezone.now, verbose_name=u'维护时间')
    old_card1_total = models.FloatField(default=0.0, verbose_name=u'数据回收前卡槽1卡容量')
    old_card2_total = models.FloatField(default=0.0, verbose_name=u'数据回收前卡槽2卡容量')
    new_card1_total = models.FloatField(default=0.0, verbose_name=u'数据回收后卡槽1卡容量')
    new_card2_total = models.FloatField(default=0.0, verbose_name=u'数据回收后卡槽2卡容量')

    describe = models.TextField()

