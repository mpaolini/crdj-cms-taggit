from django.db import models
from django.utils.translation import ugettext_lazy as _
from taggit.models import TaggedItemBase
from taggit.managers import TaggableManager
from cms.models.pagemodel import Page

class TaggedPage(TaggedItemBase):
    content_object = models.ForeignKey(Page, verbose_name=_('Page'))
    class Meta:
        verbose_name = _('Page Taggit')
        verbose_name_plural = _('Page Taggits')

    def __unicode__(self):
        return u'Taggit for {0}'.format(self.content_object)
