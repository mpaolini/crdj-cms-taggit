from django.conf.urls.defaults import url, patterns

urlpatterns = patterns(
    'crdj_cms_taggit.views',
    url(r'^update_tags/(?P<page_id>\d+)/$', 'update_tags', name='crdj_cms_taggit_update_tags'),
    )

