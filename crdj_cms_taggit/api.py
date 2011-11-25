from cms.models import Page
from crdj_cms_taggit.models import TaggedPage
from taggit.models import Tag

def get_tagged_pages(tags):
    # TODO: cache this
    return Page.objects.filter(taggedpage__tag__name__in=tags)

def get_page_tags(page):
    return Tag.objects.filter(crdj_cms_taggit_taggedpage_items__content_object=page)

def set_page_tags(page, tags):
    existing_tagged = dict([(tp.tag.name, tp) for tp in TaggedPage.objects.filter(content_object=page).select_related()])
    # TODO: cache this dict
    existing_tags = dict([(t.name, t) for t in Tag.objects.filter(name__in=tags)])
    for tag in tags:
        try:
            t = existing_tags[tag]
        except KeyError:
            t = Tag(name=tag)
            t.save()
        # OPTIMIZE: if tag was not found, don't bother checking in other dict
        try:
            tp = existing_tagged[tag]
            del existing_tagged[tag]
        except KeyError:
            tp = TaggedPage(tag=t, content_object=page)
            tp.save()
    # delete stale
    for _, tp in existing_tagged.items():
        tp.delete()
