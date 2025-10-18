from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.encoding import smart_str


class Music(models.Model):
    title = models.CharField(_(u'名称'), max_length=250)


author = models.CharField(_(u'作者'), max_length=250)
url = models.CharField(_(u'地址'), max_length=250)

createdate = models.DateTimeField(_
                                  (u'创建时间'),
                                  auto_now_add=True,
                                  blank=True
                                  )


def __unicode__(self):
    return smart_str(self.title)


class Meta:
    verbose_name = _(u'音乐库')
    verbose_name_plural = _(u'音乐库')
    ordering = ['-createdate']
