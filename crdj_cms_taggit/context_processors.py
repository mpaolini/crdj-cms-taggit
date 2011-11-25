from crdj_cms_taggit.api import get_page_tags
from taggit.utils import edit_string_for_tags

def taggit(request):
    if request.current_page:
        tags = get_page_tags(request.current_page)
        return {'taggit':
                    {'tags': tags,
                     'edit_string': edit_string_for_tags(tags)}
                }
