from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from crdj_cms_taggit.models import TaggedPage

admin.site.register(TaggedPage)

