from cms.cms_toolbar import CMSToolbar
from cms.toolbar.constants import LEFT, RIGHT
from cms.toolbar.items import TemplateHTML

class CMSToolbarTaggit(CMSToolbar):
    def get_items(self, *args, **kwargs):
        items = super(CMSToolbarTaggit, self).get_items(*args, **kwargs)
        if items:
            pos = 2 if len(items) > 2 else len(items) - 1
            items.insert(pos, TemplateHTML(RIGHT, 'taggit',
                                           'crdj_cms_taggit/toolbar/items/taggit.html'))
        return items
