from cms.middleware.toolbar import ToolbarMiddleware
from crdj_cms_taggit.cms_toolbar import CMSToolbarTaggit

class ToolbarMiddlewareTaggit(ToolbarMiddleware):
    """
    Middleware to set up CMS Toolbar.
    copied from cms.middleware.toolbar.ToolbarMiddleware
    """

    def process_request(self, request):
        """
        copied from cms.middleware.toolbar.ToolbarMiddleware
        """
        if 'edit' in request.GET and not request.session.get('cms_edit', False):
            request.session['cms_edit'] = True
        request.toolbar = CMSToolbarTaggit(request)
